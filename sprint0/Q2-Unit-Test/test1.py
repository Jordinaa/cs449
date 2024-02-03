# Author Jordan Taranto
# Source: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

import pytest

# Unit Test 1
# def capital_case(x):
#     return x.capitalize()

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
        