from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, Optional, Union


class StatusCode:
    SUCCESS = 0  # 处理成功
    FAILURE = -1  # 处理失败


class Response(BaseModel):
    code: int
    msg: Optional[str] = ""
    data: Optional[Any] = None
    meta: Optional[Dict] = {}


class JsonResponse(JSONResponse):
    def __init__(self, code: int, message: str = "", data: Union[Any] = "", meta: Dict = {}, ** kwargs: Any):
        content = Response(code=code, msg=message, data=data, meta=meta)
        super().__init__(content=content.model_dump(), **kwargs)
