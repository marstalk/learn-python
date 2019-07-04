"""Sets.


A set is a collection which is unordered and unindexed.
In Python sets are written with curly brackets

Set objects also support mathematical operations like union,
insertion, difference, and symmetric difference.
"""

def test_sets():
    """Sets"""
    fruit_set = {"apple", "banana", "cherry"}

    assert isinstance(fruit_set, set)


    # It is also possible to use the set() constructor to make a set
    # Note the double brackets
    fruit_set_with_constructor = set(("apple", "banana", "cherry"))
    assert isinstance(fruit_set_with_constructor, set)

def test_set_methods():
    """Set methods"""

    fruit_set = {"apple", "banana", "cherry"}

    #You can check if the item is in set using the "in" statement
    assert "apple" in fruit_set
    assert "pineapple" not in fruit_set

    # Use len() method to return the length of a set
    assert len(fruit_set) == 3

    # You can use the add() method to add an item.
    fruit_set.add("pineapple")
    assert len(fruit_set) == 4


    # You can use remove() method to remove an item.
    fruit_set.remove("pineapple")
    assert "pineapple" not in fruit_set
    assert len(fruit_set) == 3


    # Demonstrate set operations on unique letters from two word:
    first_char_set = set("abracadabra")
    # VS frist_char_set = set(("abracadabra))
    assert first_char_set == {"a", "r", "b", "c", "d"}

    second_char_set = set("alacazam")
    assert second_char_set == {"a", "l", "c", "z", "m"}

    # Letter in frist word but not in second
    assert first_char_set - second_char_set == {"r", "b", "d"}

    # Letter in first word or in second word or both
    assert first_char_set | second_char_set == {"a", "c", "r", "d", "b", "m", "z", "l"}

    # Common letters in both words
    assert first_char_set & second_char_set == {"a", "c"}

    # Letter in first or in second but not both
    assert first_char_set ^ second_char_set == {"r", "d", "b", "m", "z", "l"}

    #Similarly to list comprehensions, set comprehensions are also supported:
    word = {char for char in "abracadabra" if char not in "abc"}
    assert word == {"r", "d"}





































