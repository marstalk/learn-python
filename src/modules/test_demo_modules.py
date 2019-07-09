"""Modules.

As your program gets longer, you may want to split it into several files for easier maintenance.
You may also want to use a handy function that you've written in several programs without copying
it's definition into each program.

To support this, Python has a way to put definitions in a file and use them in a script or in an
interactive instance or the interpreter. Such a file is called a module; definitions from a module
can be imported into other modules or into the main module ( the collection of variables that you
have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name
with the suffix .py appended, Within a module, the module's name (as a string) is available as the
value of the global variable __name__.

When the interpreter executes the import statement, it searches for module in a list of
directories assembled from the following sources:

- The directory from which the input script was run or the current directory if the interpreter is
being run interactively
- The list of directories contained in the PYTHONPATH environment variable, if it is set. (The
format for PYTHONPATH is OS-dependent bu should mimic the PATH environment varaible.)
- An installation-dependent list of directories configured at the time Python is installed

The resulting search path is acceesbile in the Python variable sys.path, which is obtained from a
module named sys:

>>> import sys
>>> sys.path
"""

#This does not enter the name of the functions defined in fibonacci_module directly in the 
# current symbol table; it only enters the module name fibonacci_module there.
import demo_fibonacci_module

# There is a variant of the import statement that imports names from a module directly into the
# importing module's symbol table. For example.
from demo_fibonacci_module import hello, say_hi

# There is even a rariant to import all names that a module defined. This imports all names except
# those beginning with an underscore(_). In most cases Python programmer do not use this facility
# since it introduces an unknow set of names into the interpreter, possibly hiding some things you
# have already defined.
# >>> from fibonacci_module import *


# If the module name is followed by as, then the name following as is bound directly to the 
# imported module.
# pylint: disable=reimported
import demo_fibonacci_module as greetings

# It can also be used when utlising from with similar effects:
from demo_fibonacci_module import hello as hello_rename

# When a module named spam is imported, the interpreter frist searches for a built-in module with
# that name. If not found, it then searches for a file named spam.py in a list of directories
# giben by the variables sys.path. sys.path is initialized from these locations:
#
# - The directory containing the input script(or the current directory when no file is specified).
# - PYTHONPATH ( a list of directory names, with the same syntax as the shell variable PATH).
# - The installation-dependent default

def test_modules():
    """Modules"""

    assert demo_fibonacci_module.hello() == "hello!"
    assert demo_fibonacci_module.say_hi("jiacheng") == "hi, jiacheng"

    assert hello() == "hello!"
    assert say_hi("jiacheng") == "hi, jiacheng"

    assert greetings.hello() == "hello!"
    assert greetings.say_hi("jiacheng") == "hi, jiacheng"

    assert hello_rename() == "hello!"