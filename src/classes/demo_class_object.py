"""Class Definition Syntax

After defining the class attribute to a class, the class object can be created by assigning the
object to a variable. The created object would have instance attributes associated with it.
"""

def test_class_object():
    """Class Object.

    Class objects support two kinds of operation:
    - attribute references
    - instantiation.
    """

    # ATTRIBUTE REFERENCES use the standard syntax used for all attribute references in
    # Python: obj.name. Valid attribute names are all the names that were in the class'  namespace
    # when the class object was created. For class MyCounter the following references are valid
    # attribute references:

    class ComplexNumber:
        """Example of the complex numbers class"""

        real = 0
        imaginary = 0

        def get_real(self):
            return self.real

        def get_imaginary(self):
            return self.imaginary

    assert ComplexNumber.real == 0

    assert ComplexNumber.__doc__ == """Example of the complex numbers class"""

    # Class attribute can also be assigned to, so you can change the value of
    # ComplexNumber.counter by assignment
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10

    # Class INSTANTIATION uses function notation. Just pretend that the class object is a
    # parameterless function that returns a new instance of the class. For example
    # (assuming the above class):

    complex_number = ComplexNumber()
    assert complex_number.real == 10
    assert complex_number.get_real() == 10

    # Let's change counter default value back.
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10


    # The instantiation operation("calling" a class object) creates anempty object. Many classes
    # like to create object with instances customized toa specific initial state. Therefore a
    # class may define a special method named __init(), like this:

    class ComplexNumberWithConstructor:
        """Example of the class with constructor"""
        def __init__(self, real_part, imaginary_part):
            self.real = real_part
            self.imaginary = imaginary_part

        def get_real(self):
            return self.real

        def get_imaginary(self):
            return self.imaginary


    complex_number = ComplexNumberWithConstructor(3.0, -4.5)
    assert complex_number.real, complex_number.imaginary == (3.0, -4.5)
