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

"""

import sys
for path in sys.path:
    print(path)