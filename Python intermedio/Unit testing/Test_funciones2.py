import pytest
from Funciones2_test import word

def test_word_reversed_text1():

    #Arrange
    first_text = "Programming"

    #Act
    result = word(first_text)

    #Assert
    assert result == "gnimmargorP"


def test_word_reversed_text2():

    #Arrange
    first_text = "Sun"

    #Act
    result = word(first_text)

    #Assert
    assert result == "nuS"


def test_word_reversed_text3():

    #Arrange
    first_text = "Happy"

    #Act
    result = word(first_text)

    #Assert
    assert result == "yppaH"