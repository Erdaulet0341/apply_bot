import os
import sys
import traceback
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

LOG_FILE_PATH = '../logs.txt'


def log(message, e=None):  # Log to console and file
    print(message)
    try:
        with open(LOG_FILE_PATH, 'a') as f:
            f.write(f'{datetime.now()} - {message}\n')
            if e:
                f.write(f'{datetime.now()} - {format_exception(e)}\n')
    except Exception as log_error:
        print(f"Logging failed: {log_error}")


def format_exception(e) -> str:
    return ''.join(
        traceback.format_exception(*(sys.exc_info()))
    ) + '\n' + f'{e.__class__}\n' + f'{e.__str__()}\n' + f'{e}\n'


def get_env(key):  # Get environment variable from .env file
    return os.getenv(key)


def is_valid_fullname(fullname: str) -> bool:  # Check if fullname is valid
    return len(fullname.split()) == 2 and all(map(str.isalpha, fullname.split()))


def is_valid_phone(phone: str) -> bool:  # Check if phone number is valid
    return phone.isdigit() and len(phone) >= 10 and phone[0] == '7'
