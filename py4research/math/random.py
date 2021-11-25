"""Random-based mathematical generators.
"""

from typing import Optional, Union

import numpy as np


def generate_integer_random_number(low: Optional[int] = 0,
                                   high: Optional[int] = 1,
                                   exclude_value: Optional[int] = None, 
                                   size: Optional[Union[np.ndarray, int]] = None) -> Union[np.ndarray, int]:
    """Generates a random number or array based on an integer distribution.

    Args:
        low: Lower interval.
        high: Higher interval.
        exclude_value: Value to be excluded from array.
        size: Size of array.

    Returns:
        (Union[np.ndarray, int]): Integer random number or integer-based array.

    """

    integer_array = np.random.randint(low, high, size)

    # Checks if a value is supposed to be excluded
    if exclude_value is not None:
        # Creates a boolean array based on excluded value
        bool_array = (integer_array == exclude_value)

        # If the excluded value is present
        if np.any(bool_array):
            # Re-calls the function with same arguments
            return generate_integer_random_number(low, high, exclude_value, size)

    return integer_array


def generate_gaussian_random_number(mean: Optional[float] = 0.0,
                                    variance: Optional[float] = 1.0,
                                    size: Optional[Union[np.ndarray, int]] = 1) -> Union[np.ndarray, float]:
    """Generates a random number or array based on a gaussian distribution.

    Args:
        mean: Gaussian's mean value.
        variance: Gaussian's variance value.
        size: Size of array.

    Returns:
        (Union[np.ndarray, float]): Gaussian random number or gaussian-based array.

    """

    gaussian_array = np.random.normal(mean, variance, size)

    return gaussian_array
