import logging
from datetime import datetime
from typing import Any
from fastapi.responses import JSONResponse

logger = logging.getLogger("RetailOrderingSystem")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def log_message(message: str, level: str = "INFO"):
    if level == "DEBUG":
        logger.debug(message)
    elif level == "INFO":
        logger.info(message)
    elif level == "WARNING":
        logger.warning(message)
    elif level == "ERROR":
        logger.error(message)
    elif level == "CRITICAL":
        logger.critical(message)

# Function to get the current timestamp
def get_current_timestamp() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def custom_json_response(data: Any, status_code: int = 200) -> JSONResponse:
    return JSONResponse(content={"data": data}, status_code=status_code)

def custom_error_response(detail: str, status_code: int = 400) -> JSONResponse:
    return JSONResponse(content={"error": detail}, status_code=status_code)

def format_date(date: datetime, format_str: str = "%Y-%m-%d") -> str:
    return date.strftime(format_str)

def date_diff(start_date: datetime, end_date: datetime) -> int:
    delta = end_date - start_date
    return delta.days

