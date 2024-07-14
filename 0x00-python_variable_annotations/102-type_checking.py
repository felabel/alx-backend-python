#!/usr/bin/env python3

from typing import List, Tuple
'''Task 102's module.
'''

def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    '''
    Zooms in on an array by repeating each element a given number of times.

    Parameters:
    lst (List[int]): The list of integers to be zoomed in on.
    factor (int): The factor by which to repeat each element.

    Returns:
    List[int]: The zoomed-in list.
    '''
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
