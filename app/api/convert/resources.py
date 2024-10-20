import os
from loguru import logger
from datetime import datetime
from app.config import Config
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from app.model.database import get_db
from app.model import UserModel, ChatModel
from fastapi import Form, File, UploadFile, Request, Depends, APIRouter
from app.schema import JsonResponse, StatusCode
from app.utils.common.helper import make_request

# from app.utils.oai.resouces import oai_chat

convert = APIRouter()
os.environ["OPENAI_API_KEY"] = "sk-d56b03b5e117328be2bc93896c75661b"


@convert.post("/completions")
async def chat(request: Request, db: Session = Depends(get_db)):
    try:
        auth_header = request.headers.get("authorization")
        if auth_header:
            code = auth_header.split(" ")[1]
            print(code)
            query = select(UserModel).where(UserModel.code == code).limit(1)
            print(query)
            result = await db.execute(query)
            user = result.scalars().first()
            if user is None:
                return "未经授权"

            data = await request.json()
            messages = data.get("messages", [])
            print(messages)
            payload = {"model": "gpt-4o-2024-08-06", "messages": messages}
            messages.insert(0, {"role": "system", "content": user.prompt.strip()})
            response = await make_request(
                "POST", url=Config.MODEL_URL, headers=Config.MODEL_HEADERS, json=payload
            )
            answer = response["choices"][0]["message"]["content"]
            system = [
                "使用四到五个字直接返回这句话的简要主题，不要解释、不要标点、不要语气词、不要多余文本，不要加粗，如果没有主题，请直接返回“闲聊”",
                "简要总结一下对话内容，用作后续的上下文提示 prompt，控制在 200 字以内"
            ]
            if messages[-1]["content"] not in system:
                new_chat = ChatModel(
                    message=messages[-1]["content"],
                    answer=answer,
                    creator=user.id,
                    creat_date=datetime.now().replace(microsecond=0),
                )
                db.add(new_chat)
                await db.commit()
            return answer
    except Exception as e:
        logger.error(e)
    return "不受支持的方式"


@convert.post("/convert", name="音视频转换")
async def media_slice_convert(
    file_id: int = Form(...),
    convert_type: int = Form(...),
    file: UploadFile = File(...),
):
    pass
    # try:
    #     if convert_type not in [0, 1]:
    #         return JsonResponse(code=StatusCode.FAILURE, message="转换类型不支持")
    #     file_path = await file_save(Config.FILE_PATH, file)
    #     file_type = file.filename.split(".")[-1]
    #     try:
    #         file_type = FileType(file_type=file_type).file_type
    #     except ValueError as e:
    #         return JsonResponse(code=StatusCode.FAILURE, message="文件类型不支持")
    #     if file_type in ["mp4", "mkv"]:
    #         _, file_path = handle_video(file_path)
    #     if convert_type == 0:
    #         media_handle.send(file_id=file_id, filepath=file_path)
    #     if convert_type == 1:
    #         media_slice_handle.send(
    #             file_id=file_id, filename=file.filename, filepath=file_path
    #         )
    #     return JsonResponse(code=StatusCode.SUCCESS, message="文件推送成功")
    # except Exception as e:
    #     logger.error(e)
    # return JsonResponse(code=StatusCode.FAILURE, message="fail")
