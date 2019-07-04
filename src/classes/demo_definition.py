"""Class Definition Syntax

Python is an object oriented programming language.
Almost everything in Python is an object, with it's properties and method.
A class is like an object constructor, or a "blueprint" for creating object.
"""

def test_class_definition():
    """Class Definition."""

    # Class definitions, like function definitions (def statements) must be executed before they
    # have any effect. ( You could conveivably place a class definition in a branch of an if
    # statement, or inside a function.)

    class GreetingClass:
        """Example of the class definition

        This class contains two public methods and doesn't contain constructor.
        """

        name = "user"

        def say_hello(self):
            """Class method."""
            # The self parameter is a reference to the class itself, and is used to access variables
            # that belongs to the class. It does not have to be named self, you can call it
            # whatever you like, but it has to be the first parameter of ny function in the class.
            return "Hello " + self.name

        def say_goodbye(self):
            """Clsss method."""
            return "Goodbye " + self.name

    # When a class definition is entered, a new namespace is created, and used as the local scope -
    # Thus, all assignments to local variables go into this new namespace. In particular, function
    # definitions bind the name of the new function here.

    # Class instantiation uses function notation. Just pretend that the class boejct is a
    # parameterless function that returns a new instance of the local. For example the following
    # code will creates a new instance of the class and assigns this object to the local variable.

    greeter = GreetingClass()
    assert greeter.say_hello() == 'Hello user'
    assert greeter.say_goodbye() == 'Goodbye user'
    assert GreetingClass.name == "user"
    assert greeter.name == "user"

    greeter.name = "John"
    assert greeter.name == "John"
    assert greeter.say_hello() == "Hello John"

    assert GreetingClass.name == "user"
    assert GreetingClass.say_hello(greeter) == "Hello John"


