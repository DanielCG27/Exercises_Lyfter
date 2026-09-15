#Cree los siguientes unit tests para el algoritmo bubble_sort:
#Funciona con una lista pequeña.
#Funciona con una lista grande (de más de 100 elementos.)
#Funciona con una lista vacía.
#No funciona con parámetros que no sean una lista.

import pytest
import random
from Ej1_bubble_sort_test import bubble_sort


def test_bubble_sort_small_list():
    #Arrange
    small_list = [5, 100, 1]

    #Act
    bubble_sort(small_list)

    #Assert
    assert small_list == [1, 5, 100]



def test_bubble_sort_large_list():
    #Arrange
    large_list = [numbers for numbers in range(1, 102)]
    random.shuffle(large_list)

    #Act
    bubble_sort(large_list)

    #Assert
    assert large_list == [numbers for numbers in range(1, 102)]


def test_bubble_sort_empty_list():

    #Arrange
    empty_list = []

    #Act
    bubble_sort(empty_list)

    #Assert
    assert empty_list == []


def test_bubble_sort_not_list():

    #Arrange
    not_list = "Is not a list"

    #Act - Assert
    with pytest.raises(TypeError):
        bubble_sort(not_list)



