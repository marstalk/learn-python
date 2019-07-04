"""Keyword arguments

Functions ca be called usding keyword arguments of the form kwarg=value
"""


import pytest

def parrot(voltage, state="a stiff", action="voom", parrot_type="Norwegian Blue"):
    """Example of multi-argument function

    This function accepts one required argument(voltage) and three optional arguments(state, action, and type).
    """

    message = "This parrot wouldn't " + action + " "
    message += "if you put " + str(voltage) + " volts through it."
    message += "Lovely plumage, the " + parrot_type + ". "
    message += "It's " + state + "!"

    return message

def test_function_keyword_argument():
    """Test calling function with specifying keyword arguments"""

    # The parrot function accepts one required argument(voltage) and three optional arguments
    # (state, action, and type). This function can be called in any of the following ways:

    message = (
        "This parrot wouldn't voom if you put 1000 volts through it."
        "Lovely plumage, the Norwegian Blue. "
        "It's a stiff!"
    )

    # 1 positional argument
    assert parrot(1000) == message

    # keyword argument
    assert parrot(voltage=1000) == message


    # But all the following calls would be invalid
    with pytest.raises(Exception):
        # Required argument missing
        parrot()

    # Non-keyword argument after a keyword argument
    # parrot(voltage=30, 'dead')

    with pytest.raises(Exception):
        parrot(110, voltage=00)

    with pytest.raises(Exception):
        # unknown keyword argument
        parrot(actor="welcome")

    # In a function call, keyword arguments must follow positional arguments. All the keyword
    # arguments passed must match on of the arguments accepted by the function(e.g. actor is not
    # a valid argument for the parrot function), and their order is not important. This also
    # includes non-optional arguments(e.g. parrot(voltage==1000) is valid too). No argument may
    # receive a value more than once. Here's an example that fails due to this restriction:
    def function_with_on_argument(number):
        return number

    with pytest.raises(Exception):
        function_with_on_argument(0, number=0)

    # When a final formal parameter of the form **name is present, it receives a dictionary
    # containning all keyword arugments except for those corresponding to a formal parameter.
    # This may be combined with a formal parameter fo the form *name which receives a tuple
    # containing the positional arguments bbeyond the formal parameter list.
    # (*name must occur before **name) For example, if we define a function like this:

    def test_function(first_param, *arguments, **keywords):
        """This function accepts its arguments through"arguments" tuple and keyword dictionary."""

        assert first_param == "first param"
        assert arguments == ("second param", "third param", "four param")
        assert keywords == {
            "a": "nihao",
            "b": "buhao"
        }

    test_function("first param", "second param", "third param", "four param", a="nihao", b="buhao")


    def test_function_two(name, age, **info):
        assert name == "jiacheng"
        assert age == 24
        assert info == {
            "n": "jiacheng",
            "a": 24
        }
    test_function_two("jiacheng", 24, n="jiacheng", a=24)

    def test_function_three(**info):
        assert info == {
            "name": "jiacheng",
            "age": 24
        }
    test_function_three(name="jiacheng", age=24)

"""
总结：
1，两种传参方式：位置传参， 关键字传参， 
2，*name 表示name为tuple类型。
3，**name 表示name为dictionary类型。

"""







