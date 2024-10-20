import os
import httpx
import aiofiles
from datetime import datetime
from typing import Dict, Any, Optional, Tuple


def generate_date_dir(origin_dir, create_flag=False, tag=None):
    """生成日期文件夹"""
    now = datetime.now()
    date_str = f"{now.year}/{now.month}/{now.day}"
    if tag is not None:
        create_dir = os.path.join(origin_dir, date_str, tag)
    else:
        create_dir = os.path.join(origin_dir, date_str)
    if create_flag and not os.path.exists(create_dir):
        try:
            os.makedirs(create_dir)
        except FileExistsError:
            pass
    return create_dir


def seconds_to_hms(seconds):
    """秒转为时间"""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"


def time_to_milliseconds(time_str):
    """
    将时间字符串转换为毫秒数。
    参数:
    time_str (str): 表示时间的字符串，格式为 "HH:MM:SS"。
    返回:
    int: 总的毫秒数。
    """
    parts = time_str.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_milliseconds = (hours * 3600 + minutes * 60 + seconds) * 1000
    return total_milliseconds


async def make_request(
    method: str,
    url: str,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, str]] = None,
    json: Optional[Dict[str, Any]] = None,
    # data: Optional[Dict[str, Union[Dict[str, Any], Tuple]]] = None,
    data: Optional[dict] = None,
    files: Optional[Dict[str, Tuple[str, Any, str]]] = None,
    timeout: Optional[int] = None,
) -> Any:
    """请求函数"""
    proxies = {
        "http:": "http://127.0.0.1:7890",
        "https:": "http://127.0.0.1:7890",
    }
    try:
        async with httpx.AsyncClient(timeout=timeout, proxies=proxies) as client:
            response = await client.request(
                method=method.upper(),
                url=url,
                headers=headers,
                params=params,
                json=json,
                data=data,
                files=files  # 添加文件上传支持
            )
            print(response.text)
            response.raise_for_status()  # 抛出 HTTP 错误状态码的异常
            return response.json()
    except httpx.RequestError as exc:
        return {"choices": [{"message": {"content": "联系管理员"}}]}
    except httpx.HTTPStatusError as exc:
        return {"choices": [{"message": {"content": "联系管理员"}}]}


async def async_open_file(filepath):
    """异步文件读取"""
    async with aiofiles.open(filepath, mode="rb") as f:
        return await f.read()


async def async_write_file(filepath, data):
    """异步文件保存"""
    async with aiofiles.open(filepath, mode="wb") as f:
        await f.write(data)
