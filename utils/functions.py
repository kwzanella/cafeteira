from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler


def set_path(*, file_name: str, file_dir: str) -> str:
    current_dir = Path(__file__).parent     # Takes parent directory                   

    return str(((current_dir) / (f"..//{file_dir}//{file_name}")).resolve())   # Goes into root dir and into "file_dir"


def set_logger(name: str, *, file_name: str):
    logger = logging.getLogger(name)    # Define log name as file name
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")  # Defines log format

    file_handler = RotatingFileHandler(set_path(file_name=file_name, file_dir="logs"),      
                                            mode='a', maxBytes=5*1024*1024, backupCount=2, encoding="utf-8", delay=0)

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger