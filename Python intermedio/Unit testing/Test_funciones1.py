import pytest
from Funciones1_test import sum_numbers_list

def test_sum_number_list_sum_numbers():

    #Arrange
    numbers_list = [20, 23, 84, 9, 45, 72]

    #Act
    result = sum_numbers_list(numbers_list)

    #Assert
    assert result == 253