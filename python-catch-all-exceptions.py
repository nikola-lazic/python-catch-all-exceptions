# Reference: https://stackoverflow.com/questions/4990718/how-can-i-write-a-try-except-block-that-catches-all-exceptions
import traceback
import logging
from datetime import datetime


def main_function():
    print(something_undefined_or_any_error)  # Function with error (d is not defined)


if __name__ == "__main__":
    # time format for log filename
    log_time = datetime.today().strftime("%Y-%m-%d_%H-%M-%S")
    try:
        main_function()
    except Exception as e:
        # This will export log into defined TXT file
        logging.basicConfig(filename="./crash_log_" + log_time + ".txt")
        logging.error(traceback.format_exc())
