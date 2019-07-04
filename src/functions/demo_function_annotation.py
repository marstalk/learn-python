"""Function Annotation

Function annotations are completely optional metadata information about the types used by user-defined functions

Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no
effect on any other part of the function. Parameter annotations are defined by a colon after the
parameter name, followed by an expression evaluating to the value of the annotation. return
annotations are defined by a literal ->, followed by an expression, betwwen the parameter list and
the colon denoting the end of the def statement.
"""


def breakfast(ham: str, eggs: str = "eggs") -> str:
    """Breakfast creator.

    This function has a positional argument, a keyword argument, and the return value annotated.
    """
    return ham + " and " + eggs

def test_function_annotation():
    """Function Annotations."""

    assert breakfast.__annotations__ == {"ham": str, "eggs": str, "return": str}