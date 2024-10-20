from app.api import restful_api
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from starlette.middleware.cors import CORSMiddleware


__version__ = "2024.09"


def create_app() -> FastAPI:
    app = FastAPI(
        title="Teacher Xiao Wu",
        version=__version__,
        description="Teacher Xiao Wu answers questions online",
    )
    register_cors(app)
    register_routers(app)
    return app


def register_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def limit_payload_size(request: Request, call_next):
        max_payload_size = 500 * 1024 * 1024
        content_length = request.headers.get('content-length')

        if content_length and int(content_length) > max_payload_size:
            return PlainTextResponse("Request entity too large", status_code=413)

        return await call_next(request) 


def register_routers(app: FastAPI) -> None:
    app.include_router(restful_api)
