from typing import Literal
from pydantic import BaseModel, Field, field_validator


class FileType(BaseModel):
    file_type: Literal["mp3", "wav", "mp4", "mkv"]


class TimeRange(BaseModel):
    start_time: str = Field(..., description="开始时间")
    end_time: str = Field(..., description="结束时间")


class Summarize(BaseModel):
    label: list = Field(..., title="标签")
    summarize: str = Field(..., title="总结")
