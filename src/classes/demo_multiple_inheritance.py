"""Class and Instance Variable

Generally speaking, instance variables are for data unique to each instance and class variables are
for attributes and methods shared by all instances of the class.
"""


def test_class_and_intance_variable():
    """Class and Instance Variables."""

    class Dog:
        """Dog class example"""
        kind = "canine"

        def __init__(self, name):
            self.name = name

    fido = Dog("Fido")
    buddy = Dog("Buddy")

    # Shared by all dogs
    assert fido.kind == "canine"
    assert buddy.kind == "canine"
