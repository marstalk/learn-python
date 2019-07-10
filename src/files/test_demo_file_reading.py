"""Reading and Writing Files

@see: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

The process of reading and writing to a file is like finding a book and opening a book.
First, the file is located, opened to the first pagem the reading/writing begins until it reaches
the end of the file.
"""


def test_file_open():
    """Open files

    open() return a file object, and is most commonly used with two arguments:
    open(filename, mode).

    The first argument is a string containing the file name. The second argument is another string
    containing a few characters describing the way in which the file will be used. mode can be:

    - 'r' when the file will only be read.
    - 'w' for only writing (an existing file with the same sname will be erased),
    - 'a' opens the file for appending; any data written to the file is automatically added to end.
    - 'r+' opens the file for both reading and writing.

    The mode argument is optioal; 'r' will be assumed if it's omitted.

    Normally, files are opened in text mode, that means, you read and write string from and to the 
    file, which are encoded in a specific encoding. If encoding is not specified, the default is
    platform dependent(see open()). 'b' appended to the mode opens the file in binary mode: now
    the data is read and written in the form of bytes objects. This mode should be used for all
    files that don't contain text.

    In text mode, the default when reading is to conver platform-specific line ending(\n on 
    Unix, \r\n on Windows) to just \n. When writing in text mode, the default is to convert
    occurrence of \n back to paltform-spefici line endings. This behind-the-scenes modification
    