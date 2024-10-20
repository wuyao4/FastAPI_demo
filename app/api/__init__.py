from fastapi import APIRouter
from app.api.convert.resources import convert

restful_api = APIRouter()

restful_api.include_router(convert, prefix="/v1/chat", tags=["Chat"])
