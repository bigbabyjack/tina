import time
import logging
from functools import wraps


def setup_logging(logging_level=logging.DEBUG, log_to_console=False, log_to_file=True):
    # Define the log format
    log_format = "%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s"

    # Set up basic configuration
    logging.basicConfig(
        level=logging_level,
        format=log_format,
        handlers=[logging.FileHandler("./logs/application.log")],
    )  # Default handler for file output

    # Conditionally add console output
    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging_level)
        console_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(console_handler)

    # Conditionally add console output
    if log_to_file:
        file_handler = logging.FileHandler("./logs/application.log", mode="w")
        file_handler.setLevel(logging_level)
        file_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(file_handler)
    # Silence noisy libraries
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def timemethod(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        logging.info(
            f"{func.__name__} took {elapsed_time:.4f} seconds to complete.")
        return result

    return wrapper
