from typing import Dict, Type, List, Iterable, get_args, get_origin, Any, Protocol, Awaitable, Callable, Union, Tuple, Optional, runtime_checkable
from collections import abc
from functools import wraps
import inspect

def validate_data_structure(data, expected_type: Type):
    origin = get_origin(expected_type)
    if origin is Union:
        # Check if data matches any of the unioned types entirely
        return any(validate_data_structure(data, arg) for arg in get_args(expected_type))
    elif origin is dict:
        key_type, value_type = get_args(expected_type)
        return all(
            (isinstance(k, key_type) if key_type is not Any else True) and 
            validate_data_structure(v, value_type) if value_type is not Any else True
            for k, v in data.items()
        )
    elif origin is abc.Iterable:
        item_type = get_args(expected_type)[0]
        return all(validate_data_structure(item, item_type) for item in data)
    
    elif origin is abc.Callable:
        return check_callable(data, expected_type)

    elif origin in [list, set, tuple]:
        item_type = get_args(expected_type)[0]
        if origin is tuple and len(get_args(expected_type)) != len(data):
            return False  # Tuple must have exactly the number of elements specified
        # Ensure all elements in the iterable match the specified item type
        return all(validate_data_structure(item, item_type) for item in data)
    else:
        return isinstance(data, expected_type)
    
def check_callable(data, expected_type: Type) -> bool:
    if not callable(data):
        return False
    
    sig = inspect.signature(data)
    expected_param_types = get_args(expected_type)[0]
    return_type = get_args(expected_type)[1]

    if len(sig.parameters) != len(expected_param_types):
        return False  # Check if number of parameters matches

    for (param_name, param), expected_param_type in zip(sig.parameters.items(), expected_param_types):
        if param.annotation is not param.empty:
            if not param.annotation == expected_param_type:
                return False  # Check parameter types
    if sig.return_annotation is not sig.empty and not sig.return_annotation == return_type:
        return False  # Check return type
    return True

def typecheck(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        expected_return_type = annotations.pop('return', None)  # Remove the return type annotation
        all_args = kwargs.copy()
        all_args.update(dict(zip(func.__code__.co_varnames, args)))
        
        for arg, expected_type in annotations.items():
            if not validate_data_structure(all_args[arg], expected_type):
                raise TypeError(f"Expected type {expected_type} for argument {arg}, got {type(all_args[arg])}")
        result = func(*args, **kwargs)
        if expected_return_type is not None:
            if not validate_data_structure(result, expected_return_type):
                raise TypeError(f"Expected return type {expected_return_type}, got {type(result)}")
        return result
    return wrapper


