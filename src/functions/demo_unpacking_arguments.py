"""Unpacking Argument Lists

Unpacking arguments may be executed via * and ** operators. See below for further details.
"""

import pytest

def test_function_unpacking_arguments():
    """Unpacking Arguments"""


    # The situation may occur when the arguments are already in a list or tuple but need to be
    # unpacked for a function call requiring separate positional arguments. For instance, the
    # build-in range() function expects separates start and stop arguments. If they are not
    # available separately, write the function call with the *-operator to unpack the arguments out
    # of a list or tuple:


    # Normal call with separate arguments;
    assert list(range(3, 6)) == [3, 4, 5]

    # Call with arguments unpacked from a list
    arguments_list =[3, 6]
    assert list(range(*arguments_list)) == [3, 4, 5]

    # In the same fashion, dictionaries can deliver keyword arguments with the **-operator
    def function_that_receives_names_arguments(first_w, second_w):
        return first_w + second_w + "!"

    with pytest.raises(Exception):
        arguments_dic = {"first_w": "first", "second_w": "second", "name": "name"}
        assert function_that_receives_names_arguments(**arguments_dic) == "firstsecond!"


    arguments_dic = {"first_w": "first", "second_w": "second"}
    assert function_that_receives_names_arguments(**arguments_dic) == "firstsecond!"