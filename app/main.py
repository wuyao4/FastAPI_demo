from app.utils.log import init_logging
from __init__ import create_app
from app.config import Config
import uvicorn

app = create_app()

if __name__ == "__main__":
    config = uvicorn.Config(
        app="main:app", host="0.0.0.0", port=Config.PORT, reload=True)
    server = uvicorn.Server(config)
    init_logging("DEBUG")
    server.run()
# fk-Os1i3VBRyApJL6iutDRVQyNz5uumArombpXruq5L5N8

# alembic revision --autogenerate -m "x"
# alembic upgrade head
