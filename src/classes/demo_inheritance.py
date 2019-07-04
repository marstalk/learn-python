"""Inheritance

Inheritance is noe of the principles of object-oriented programming. Since classes may share a lot
of the same code, inheritance allows a derived class to reuse the same code and modify accordingly
"""


class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# The syntax for a derived class definition looks like this.
class Employee(Person):
    """Example of the devrived class

    The Base Class(in our case Person) must be defined in a scope containing the derived class
    definition. In place of a base class name, other arbitrary expressions are also allowed.

    Derived classes may oeverride methods of their base classes. Beacuase methods have no special
    privileges when calling other mthods of teh same object, a method of a base class that calls
    another method defined in teh same base class may end up calling a method of a derived classs
    that overrides it.

    An overriding method in a derived class may in fact want to extend rather than simply replace
    the base class method of the same name. There is a simple way to call the base class method
    directly: just call BaseClassName.methodname(self, arguments). This is occasionally useful to
    clients as well. (Note that this only works if the base class is accessible as BaseClassName
    in the global scope.)
    """

    def __init__(self, name, staff_id):
        Person.__init__(self, name)
        # You may also use super() here in order to avoid explicit using of paraent class ame:
        # >> supper().__init(name)
        self.staff_id = staff_id

    def get_full_id(self):
        return self.get_name() + ", " + self.staff_id


def test_inheritance():

    person = Person("Bill")
    employee = Employee("John", "A23")

    assert person.get_name() == "Bill"
    assert employee.get_name() == "John"
    assert employee.get_full_id() == "John, A23"

    assert isinstance(employee, Employee)
    assert not isinstance(person, Employee)

    assert issubclass(Employee, Person)