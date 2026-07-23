import time

from fastapi import Request

from src.logger import logger


async def log_requests(request: Request, call_next):

    start_time = time.time()

    logger.info(
        f"Incoming Request | {request.method} | {request.url.path}"
    )

    response = await call_next(request)

    process_time = round(
        time.time() - start_time,
        4
    )

    logger.info(
        f"Completed | Status={response.status_code} | Time={process_time}s"
    )

    return response