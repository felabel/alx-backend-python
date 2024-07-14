#!/usr/bin/env python3
'''Task 100's module.
'''
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Returns the first element of a sequence if it exists, otherwise returns None.

    Parameters:
    lst (Sequence[Any]): A sequence of any type.

    Returns:
    Union[Any, None]: The first element of the sequence or None.
    '''
    if lst:
        return lst[0]
    else:
        return None
