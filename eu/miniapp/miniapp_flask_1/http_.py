import jsonschema
from functools import wraps
from types import FunctionType
from flask import request
import json




def validate_schema(schema) -> FunctionType:
    def wrapper(func: FunctionType) -> FunctionType:
        @wraps(func)
        def decorated_func(*args, **kwargs):
            try:
                jsonschema.validate(
                    instance=request.json,
                    schema=schema
                )
            except jsonschema.ValidationError as validate_error:
                return {'Error': validate_error.message}, 400

            return func(*args, **kwargs)
        return decorated_func
    return wrapper
