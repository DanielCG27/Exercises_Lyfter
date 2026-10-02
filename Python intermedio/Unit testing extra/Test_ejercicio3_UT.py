import pytest

from Ejercicio3_UT_test import read_lines

from unittest.mock import mock_open, patch

def test_read_lines():
    #Arrange

    expected_lines = ["Hello\n", "world\n", "python\n"]
    mock_file = mock_open(read_data= "Hello\nworld\npython\n")

    #Act
    with patch("Ejercicio3_UT_test.open", mock_file) as f:
        result = read_lines("test.txt")

    #Assert
    assert expected_lines == result