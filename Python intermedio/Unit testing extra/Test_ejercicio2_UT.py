import pytest

from Ejercicio2_UT_test import divide


def test_divide_positive_numbers():
    # Arrange
    number1 = 10
    number2 = 2

    #Act

    result = divide(number1, number2)

    #Assert
    assert result == 5


def test_divide_by_zero():
    #Arrange
    number1 = 12
    number2 = 0

    #Act / Assert
    with pytest.raises(ValueError):
        divide(number1, number2)


def test_divide_string():
    #Arrange
    number1 = 12
    number2 = "Hello"

    #Act / Assert
    with pytest.raises(TypeError):
        divide(number1, number2)

