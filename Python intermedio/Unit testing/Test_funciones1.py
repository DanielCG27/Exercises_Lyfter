import pytest
from Funciones1_test import sum_numbers_list

def test_sum_number_list_sum_numbers1():

    #Arrange
    numbers_list = [20, 23, 84, 9, 45, 72]

    #Act
    result = sum_numbers_list(numbers_list)

    #Assert
    assert result == 253


def test_sum_number_list_sum_numbers2():

    #Arrange
    numbers_list = [5, 15, 2, 8]

    #Act
    result = sum_numbers_list(numbers_list)

    #Assert
    assert result == 30


def test_sum_number_list_sum_numbers3():

    #Arrange
    numbers_list = [3, 12, 9, 12]

    #Act
    result = sum_numbers_list(numbers_list)

    #Assert
    assert result == 36