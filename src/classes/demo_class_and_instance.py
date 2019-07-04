"""Class and Instance Variables.

Generally speaking, instance variabless are for data unique to each instance and class variables are
for attributes and methods shared by all instances of the class.
"""


def test_class_and_instance_variable():
    """Class and Instance Variables."""


    class Dog:
        """Dog class example"""

        kind = "canine"

        def __init__(self, name):
            self.name = name


    fido = Dog("fido")
    buddy = Dog("buddy")

    # Shared by all dogs
    assert fido.kind == "canine"
    assert buddy.kind == "canine"


    #Unique to fido
    assert fido.name == "fido"

    #Unique to buddy
    assert buddy.name == "buddy"

    # Shared data can have possibly surprising effects with involving mutable objects such as lists
    # and dictionaries. For example, the tricks list in the following code should not be used as a
    # class variables because just a single list would be shared by all Dog instances.

    class DogWithSharedTricks:
        """Dog class wxample with wrong shared variables  usage"""
        tricks = []
        kind = "canine"

        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            """Add trick to the dog

            This function illustrate mistake use of mutable class variable tricks(see below)
            """
            self.tricks.append(trick)
            self.kind = trick

    fido = DogWithSharedTricks("Fido")
    buddy = DogWithSharedTricks("Buddy")

    fido.add_trick("roll over")
    buddy.add_trick("play dead")

    assert fido.tricks == ["roll over", "play dead"]
    assert buddy.tricks == ["roll over", "play dead"]

    assert fido.kind == "roll over"
    assert buddy.kind == "play dead"


    class DogWithTricks:
        """Dog class example"""

        def __init__(self, name):
            self.name = name # Instance variable unique to each instance
            self.tricks = [] # Create a new empty list for each dog

        def add_tricks(self, trick):
            """Add trick to the dog

            This function illustrate right use of mutable classes variable tricks(see below)
            """
            self.tricks.append(trick)

    fido = DogWithTricks("Fido")
    buddy = DogWithTricks("Buddy")

    fido.add_tricks("roll over")
    buddy.add_tricks("play dead")

    assert fido.tricks == ["roll over"]
    assert buddy.tricks == ["play dead"]















