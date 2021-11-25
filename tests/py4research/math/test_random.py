import numpy as np

from py4research.math import random

np.random.seed(0)


def test_generate_integer_random_number():
    integer_array = random.generate_integer_random_number(0, 1, None, 5)

    assert integer_array.shape == (5, )

    integer_array = random.generate_integer_random_number(0, 10, 1, 9)

    assert integer_array.shape == (9, )


def test_generate_gaussian_random_number():
    gaussian_array = random.generate_gaussian_random_number(0, 1, 3)

    assert gaussian_array.shape == (3, )
