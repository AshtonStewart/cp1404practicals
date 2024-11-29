"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    #print(repeat_string("hi", 2))
    assert repeat_string("hi", 2) == "hi hi"

    # Test car fueling
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"
    assert car.fuel == 0
    car = Car(fuel=10)
    assert car.fuel == 10


run_tests()
doctest.testmod()

def correct_sentence(input):
    """Adds full stop to end of sentence if missing and capitalizes first character"""
    """
    >>> correct_sentence("hello")
    'Hello.'
    >>> correct_sentence("hello world")
    'Hello world.'
    >>> correct_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> correct_sentence(
    """
    if input[-1] != ".":
        input +="."
        input = input.capitalize()
    return input
