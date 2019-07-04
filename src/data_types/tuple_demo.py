"""Tuples.

@See: https://www.w3chools.com/python/python_tuples.asp
@See: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

A tuple is collection which is ordered and unchangeable. In Python tuples are written with round brackets.

The Tuples have following properties:
- You cannot change values in a tuple.
- You cannot remove items in a tuple.
"""

import pytest

def test_tuples():
    """tuple"""
    fruits_tuple = ("apple", "banana", "cherry")
    assert isinstance(fruits_tuple, tuple)
    assert fruits_tuple[0] == "apple"
    assert fruits_tuple[1] == "banana"
    assert fruits_tuple[2] == "cherry"
    assert isinstance(fruits_tuple[0], str)

    #You cannot change values in a tuple
    with pytest.raises(Exception):
        fruits_tuple[0] = "pineapple"


    #It is also possible to use the tuple() constructor to make a tuple(not the double round-brackets)
    #The len() function returns the length of the tuple
    fruits_tuple_with_constructor = tuple(("apple", "banana", "cherry"))
    assert isinstance(fruits_tuple_with_constructor, tuple)
    assert len(fruits_tuple_with_constructor) == 3

    #It is also possible to omit brackets when initializing tuples
    another_tuple = 1234, 54321, "hello!"
    assert isinstance(another_tuple, tuple)

    #Tuple may be nested
    nested_tuple = another_tuple, "lol5", ("welcome", "to", "mars")
    assert isinstance(nested_tuple, tuple)
    assert len(nested_tuple) == 3
    assert len(nested_tuple[0]) == 3
    assert len(nested_tuple[1]) == 4


    """
    As you see, on output tuples are always enclosed in parenthesis, 
    so that nested tuples are interpreted correctly;
    They my be input with or without surrounding parentheses, although
    often parenthesis are necessary anyway(if the tuple is part of a large expression).
    It is not possible to assign to the individual, however it is possible to create
    tuples which contain mutable objects, such as lists.
    """

    """
    A special problem is the construction of tuples containing 0 or 1 items: 
    the syntax has some extra quirks ao accommodate these, Empty tuples are
    constructed by an empty pair of parenthesis; 
    a tuple with one item is constructed by following a value with a comma(it 
    is ont sufficient to enclose a single value in parenthesis).
    Ugly, but effective, For example:
    """
    empty_tuple = ()
    assert len(empty_tuple) == 0

    singleton_tuple = "hello",
    assert singleton_tuple == ("hello",)

    # The following example is called tuple packing
    packed_tuple = 12345, 54321, "hello!"
    assert isinstance(packed_tuple, tuple)

    #The reverse operation is also possible
    a, b, c = packed_tuple
    assert a == 12345
    assert b == 54321
    assert c == "hello!"

    """
    This is called, appropriately enough, sequence unpacking and works for any sequence on the 
    right-hand sight.
    Sequence unpacking requires that there are as many variables on the left
    side of the equals sign as there are elements in the sequence. 
    Note that multiple assignment is really just a combination of tuple
    packing ans sequence unpacking.
    """

    """
    Swapping using tuples.
    Data can be swapped from one variable to another in python using tuples
    This eliminates the nedd to use a temp variable
    """
    first_number = 123
    second_number = 456
    second_number, first_number = first_number, second_number
    assert first_number == 456
    assert second_number == 123

    assert 123 in packed_tuple


































