#!/usr/bin/env python3
'''Task 101's module.
'''
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    '''
    Safely gets a value from a dictionary.

    Parameters:
    dct (Mapping[Any, Any]): The dictionary to search.
    key (Any): The key to search for.
    default (Union[T, None]): The default value to return if the key is not found.

    Returns:
    Union[Any, T]: The value from the dictionary or the default value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
