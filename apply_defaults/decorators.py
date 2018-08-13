import inspect
from functools import wraps
from typing import Any, Callable


def apply_self(function: Callable):
    @wraps(function)
    def wrapper(self, *args: Any, **kwargs: Any):
        signature = inspect.signature(function)
        for arg in signature.parameters:
            if hasattr(self, arg) and arg not in kwargs:
                kwargs[arg] = getattr(self, arg)
        return function(self, *args, **kwargs)
    return wrapper


def apply_config(config):
    def real_decorator(function: Callable):
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any):
            signature = inspect.signature(function)
            for arg in signature.parameters:
                if config.has_option("general", arg) and arg not in kwargs:
                    kwargs[arg] = config.get("general", arg)
            return function(*args, **kwargs)
        return wrapper
    return real_decorator
