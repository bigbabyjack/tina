import time
import logging
from functools import wraps


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s",
    )
    # Silence noisy libraries
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def timemethod(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        logging.info(f"{func.__name__} took {elapsed_time:.4f} seconds to complete.")
        return result

    return wrapper
