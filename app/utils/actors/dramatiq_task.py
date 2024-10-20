import os
import asyncio
import dramatiq
import requests
from app.config import Config
from app.utils.common.helper import (
    generate_date_dir,
    seconds_to_hms,
    async_open_file,
)


@dramatiq.actor
def media_slice_handle(file_id: int, filename: str, filepath: str):
    pass


if __name__ == "__main__":
    filename = "202409041809_tmp.wav"
    filepath = (
        r"D:\project-3.10.4\media_handle\app\upload\tmp\2024\9\5\202409051854_tmp.wav"
    )
    media_slice_handle(1, filepath)
