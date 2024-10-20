import json
import httpx
import asyncio
from app.config import Config
from app.utils.common.helper import make_request


async def oai_chat(messages):
    url = "https://api.aabao.vip/v1/chat/completions"
    headers = {
       'Authorization': 'Bearer sk-E1he9SH571rWmP0F40827dDaC59d4143A4D4E5C0CdDa9694',
       'content-type': 'application/json'
    }
    payload = {
       "messages": messages,
       "temperature": 0.6,
       "password": "",
       "model": "gpt-4o-mini",
    }
    async with httpx.AsyncClient() as client:
        async with client.stream("POST", url=url, headers=headers, json=payload) as response:
            response.raise_for_status()

            # 用来存储完整的消息内容
            full_content = ""

            # 异步逐块读取响应内容
            async for chunk in response.aiter_lines():
                if chunk.startswith("data:"):
                    data_str = chunk.lstrip("data: ").strip()

                    # 忽略 '[DONE]' 标志
                    if data_str == '[DONE]':
                        break

                    try:
                        # 尝试将字符串解析为 JSON 对象
                        json_data = json.loads(data_str)
                        delta = json_data['choices'][0]['delta']

                        # 如果 "content" 字段存在，拼接内容
                        if 'content' in delta:
                            full_content += delta['content']

                    except json.JSONDecodeError:
                        print(f"无法解析的块: {data_str}")

            # 最终的完整响应内容
            return full_content


if __name__ == '__main__':
    a = asyncio.run(oai_chat(""))
    print(a)
