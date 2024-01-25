# Author Jordan Taranto
# Sprint 0
# Source: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest


def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'