"""Function Definition

The Keyword def introduce a function definition. It must be followed by the function name and the
parenthesized list of normal parameters. The statement that form the body of the function start at
the next line, must be intended.
"""

name = "louisl"

def fibonacci_function_example(number_limit):
    """Generate a Fibonacci series up to the number_limit.

    The first statement of the function boy can optionally be a string literal; this string
    literal is the function's documentation string, or docstring. There are tools which use docstrings
    to automatically produce online or printed documentation, or to let the user interactively brows though code;
    it's good practise to include docstrings in code that you write, so make a habit of it.
    """


    # The execution of a function introduces a new symbol table used for the local variables of the function.
    # More precisely, all variable assignments in a function store the value in the local symbole table;
    # whereas variable references
    # 1, first look in the local symbol table,
    # 2, then in the local symbol tables of enclosing functions,
    # 3, then in the global symbol table,
    # 4, and finally in the table of build-in names.
    # Thuse, global variables cannot be directly assigned a value
    # within a function(unless named in a global statement), although they may be referenced.
    fibonacci_list = []
    previous_number, current_number = 0, 1
    while previous_number < number_limit:
        # The statement result.append(a) calls a method of the list object result. A method is a
        # function that 'belongs' to an object and is named obj.methodname, where obj is some
        # object( this may be an expression), and methodname is the name of a method that is
        # define by the object's type. Different types define different methods. Methods of
        # different types may have the same name without causing ambiguity. (It is possible to
        # define your own object types and methods, using classes, see Classes) The method
        # append() shown in the example is defined for list objects; it adds a new element at
        # the end of the list. In this example it is equivalent to result = result + [a], but
        # more efficient
        fibonacci_list.append(previous_number)
        #This is multiple assignment statement. We make current number to be precous one and the
        # sum of previous and current to be a new current.
        previous_number, current_number = current_number, previous_number + current_number


    # The return statement returns with a value from a function. return without an expression
    # argument returns None. Falling off the end of a function also returns None.
    return fibonacci_list

def test_function_definition():
    """Function Definition"""


    # Now call the function we just defined.
    assert fibonacci_function_example(5) == [0, 1, 1 , 2, 3]


    # A function definition introduces the function name in the current symbol table. The value of
    # the function name has a tye that is recognized by the interpreter as a user-defined function.
    # This value can be assigned to another name which can then also be used as a function. This
    # serves as a general renaming mechanism.
    fibonacci_function_clone = fibonacci_function_example
    assert fibonacci_function_clone(5) == fibonacci_function_example(5)


    # In Python, functions are first class citizens, they are objects and that means we can do a
    # lot of useful stuff with them

    # Assign functions to variables.
    def greet(name):
        return "hello " + name

    greet_someone = greet
    assert greet_someone("louisl") == "hello louisl"


    #Define functions inside other functions
    def greet_again(name):
        def get_message():
            return "hello,"
        result = get_message() + name
        return result

    assert greet_again("louis") == "hello,louis"

    #Functions can be passed as parameters to other functions.
    def greet_one_more(func):
        other_name = "louis"
        return func(other_name)

    assert greet_one_more(greet_again) == "hello,louis"


    # Functions can return other functions.
    # In other words, functions generate other functions

    def compose_greet_func():
        def get_message():
            return "Hello there!"
        return get_message

    greet_function = compose_greet_func()
    assert greet_function() == "Hello there!"


    # Inner functions have access to the enclosing scope.

    # More commonly known as a  closure. A very powerful pattern that we will come across while
    # building decorators. Another thing to note, Python only allows read access to the outer
    # scope and not assignment. Notice how we modified the example above to read a "name" argument
    # from the enclosing scope of the inner function and return the new function.


    def compose_greet_func_with_closure(name):
        def get_message():
            return "hello there " + name
        return get_message


    greet_with_closure = compose_greet_func_with_closure("louis")
    assert greet_with_closure() == "hello there louis"













