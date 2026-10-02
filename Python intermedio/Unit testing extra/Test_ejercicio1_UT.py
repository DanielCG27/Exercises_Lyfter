import pytest

from Ejercicio1_UT_test import add_numbers, calculate_average, celsius_to_fahrenheit


def test_add_numbers_positive_numbers():
    assert add_numbers(15, 10) == 25
    assert calculate_average(5, 10, 12) == 9
    assert celsius_to_fahrenheit(15) == 59


def test_calculate_average_negative_numbers():
    assert add_numbers(-12, -40) == -52
    assert calculate_average(-2, -7, -3) == -4
    assert celsius_to_fahrenheit(-5) == 23


def celsius_to_fahrenheit_zero_numbers():
    assert add_numbers(0, 0) == 0
    assert calculate_average(0, 0, 0) == 0
    assert celsius_to_fahrenheit(0) == 32