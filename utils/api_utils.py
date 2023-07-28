import time
from functools import wraps
from exceptions.api_limit_exception import APILimitException

def rate_limited(max_per_second):
    """
    Decorator that limits the rate at which the function can be called.
    """
    min_interval = 1.0 / float(max_per_second)

    def decorate(func):
        last_time_called = [0.0]

        @wraps(func)
        def rate_limited_function(*args, **kwargs):
            elapsed = time.monotonic() - last_time_called[0]
            left_to_wait = min_interval - elapsed

            if left_to_wait > 0:
                time.sleep(left_to_wait)

            ret = func(*args, **kwargs)
            last_time_called[0] = time.monotonic()

            return ret

        return rate_limited_function

    return decorate

def handle_api_limit(func):
    """
    Decorator that handles OpenAI API limit by sleeping for a minute when the limit is reached.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except APILimitException:
                print("API limit reached. Sleeping for 1 minute.")
                time.sleep(60)
    return wrapper
