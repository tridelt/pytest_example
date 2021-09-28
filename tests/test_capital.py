# test_capitalize.py

from app.capital import capital_case


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'