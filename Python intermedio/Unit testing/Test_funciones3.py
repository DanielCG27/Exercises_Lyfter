import pytest
from Funciones3_test import count_types_letters

def test_count_types_letters_upper():

    #Arrange
    uppercase_count = 0
    word = "CostA Rica"

    #Act
    result = count_types_letters(uppercase_count)

    #Assert
    assert result[0] == 3


def test_count_types_letters_lower():

    #Arrange
    lowercase_count = 0
    

    #Act
    result = count_types_letters(lowercase_count)

    #Assert
    assert result[1] == 6