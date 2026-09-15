import pytest
from Funciones2_test import word

def test_word_reversed_text():

    #Arrange
    first_text = "Programming"

    #Act
    result = word(first_text)

    #Assert
    assert result == "gnimmargorP"
