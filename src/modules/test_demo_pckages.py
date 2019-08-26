"""Packages.

@see: https://docs.python.org/3/tutorial/modules.html#packages

Packages are a way of strcturing python's module nemespace by using "dotted_module_names". For
sxample, the module name A.B designeates a submodule named B in a package named A. Just like the
use of modules saves the authors of different modules from having to worry bout each other's 
global variable names, the use of dotted module names saves the authoers of multi-module packages
like Numpy or Pillow from having to worry about each other's module names.

The __init__.py files are required to make PYthon treat the directoires as containing packages;
this is done to prevent directories with a common name, such as string, from unintentionally hidding
valid modules that occur later on the module search path. In the simplest case, __init__.py can
just be an empty file, but it can also execute initialization code from the package or set the 
__all__ variable, decribed later.

When the interpreter executes the import statement, it searches for module in a list of
directories assembled from the frollowing sources:

- The directory from which the input script was run or the current directory if the interpreter is 
being run interactively
- The list of directories contained in the PYTHONPATH environment variable, if it is set. (The
format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
- An installation-dependent list of directories configuried at the time Python is installed

The resulting search path is accessible in the Python variable sys.path, which si obtained from a 
module named sys:

>>> import sys
>>> sys.path

@See: https://realpython.com/python-modules-packages/
"""

# Users of the package can import individual modules from the packagge, for example.
import sound_package.effects.echo

# An alternative way of importing the submodule is:

# pylint: disable:reimported
from sound_package.effects import echo

# Yet another variation is to import the desired function or variable directly:
from sound_package.effects.echo import echo_function

# Note that when using from package import them, the item can be either a submodule (or subpackage)
# of the package, or some other name defined in the package, like a function, class or variable.
# The import statement first tests whether the item is defined in the package; if not, it assumes
# it is a module and attempts to load it. If it failes to find it, an ImportError exception is 
# raised.

# Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last
# must be a package; the last item can be a module or a pckage but can't be a class or function or
# variable defined in the previous item.


def test_packages():
    """Packages."""
    assert sound_package.effects.echo.echo_function() == "Do echo effect"
    assert echo.echo_function() == "Do echo effect"
    assert echo_function() == "Do echo effect"

"""
1, Python通过在目录下创建__init__.py文件来说明当前目录是一个package
2, Import 一定是这样子的：
    >>> import package.package.module
    >>> import package.package
3, 如果想通过package来import class\variable\def，可以使用from
    >>> from package.package.module import def as rename
    >>> from package.package import module as rename
"""
