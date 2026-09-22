import pytest
from Funciones3_test import count_types_letters

def test_count_types_letters_upper():

    #Arrange
    

    #Act
    result = count_types_letters()

    #Assert
    assert result[0] == 3


def test_count_types_letters_lower():

    #Arrange
    
    

    #Act
    result = count_types_letters()

    #Assert
    assert result[1] == 6


def test_count_types_all_letters():

    #Arrange
    
    

    #Act
    result = count_types_letters()

    #Assert
    assert result[2] == 9