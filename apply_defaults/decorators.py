from inspect import signature
from functools import wraps
from typing import Any, Callable


def apply_self(function: Callable) -> Callable:
    @wraps(function)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        for arg in signature(function).parameters:
            if hasattr(self, arg) and arg not in kwargs:
                kwargs[arg] = getattr(self, arg)
        return function(self, *args, **kwargs)

    return wrapper


def apply_config(config, section="general") -> Callable:
    def real_decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for name, param  in signature(function).parameters.items():
                if config.has_option(section, name) and name not in kwargs:
                    # Try to infer the type from the parameter's annotation
                    if param.annotation is int:
                        kwargs[name] = config.getint(section, name)
                    elif param.annotation is float:
                        kwargs[name] = config.getfloat(section, name)
                    elif param.annotation is bool:
                        kwargs[name] = config.getboolean(section, name)
                    else:
                        kwargs[name] = config.get(section, name)
            return function(*args, **kwargs)

        return wrapper

    return real_decorator
