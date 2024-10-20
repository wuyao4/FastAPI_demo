import os
import sys
import logging
from types import FrameType
from typing import cast
from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def init_logging(level):
    LOGGING_LEVEL = level
    LOGGER_NAMES = (
        "uvicorn",
        "uvicorn.access",
    )
    for logger_name in LOGGER_NAMES:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]
        logging_logger.propagate = False

    def format_record(record):
        path = os.path.abspath(record["file"].path)
        record["extra"]["abspath"] = path
        return (
            "{time:YYYY-MM-DD HH:mm:ss}\t{level}\t{extra[abspath]}:{line}\t{message}\n"
        )

    logger.configure(
        handlers=[{"sink": sys.stdout, "level": level}],
    )
    return logger
