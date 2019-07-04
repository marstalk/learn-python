"""Function Decorators.

Function decorators are simply wrappers to existing functions. In the context of design patterns,
decorators dynamically alter the functionality of a function, method or class without having to
directly usr subclasses. This is ideal when you need to extend the functionality of functions that
you don't want to modify. We can implement the decorator pattern anywhere, bu Python facilitates
the implementation by providing much more expressive features and syntax for that.
"""

def test_function_decorator():
    """Function Decorators."""

    # Function decorators are simply wrappers to existing functions. Putting the ideas mentioned
    # above together, we can build a decorator. In this example let's consider a function that
    # wraps the string output of another function by p tags.

    # This is the function that we want to decorate
    def greeting(name):
        return "Hello, {0}!".format(name)

    # This function decorates another functions output with <p> tag.
    def decorate_with_p(func):
        def function_wrapper(name):
            return "<p>{0}</p>".format(func(name))
        return function_wrapper

    # Now, let's call our decorator and pass the function we want decorator to it.
    my_get_text = decorate_with_p(greeting)

    # Here we go, we've just decoreated the function output without changing the function itself.
    assert my_get_text("John") == '<p>Hello, John!</p>'  # With decorator.
    assert greeting("John") == 'Hello, John!'  # Without decorator.


    # Now, Python makes creating and using decorators a bit cleaner and nicer for the programmer
    # through some syntactic sugar, There is a neat shortcut for that, which is to mention the
    # name of the decorating function before the function to be decorated. The name of the
    # decorator should be prepended with an @ symbol

    @decorate_with_p
    def greeting_with_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_p('John') == '<p>Hello, John!</p>'

    # Now, let's consider we wanted to decorate our greeting function by one more functions to wrap a
    # div the string output
    def decorator_with_div(func):
        def wrapper(name):
            return "<div>{0}</div>".format(func(name))
        return wrapper

    # With Python's decorator syntax, same thing can be achieved with much more expressive power.
    @decorator_with_div
    @decorate_with_p
    def greeting_with_p_div(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_p_div("John") == '<div><p>Hello, John!</p></div>'

    # One important thing to notice here is that the order of setting our decorators matters.
    # If the order was different in the example above, the output would have beed different.

    # Passing arguments to decorators.

    # Looking back at the example before, you can notice how redundant the decorators  in the
    # examples are. 2 decorators(decorator_with_div, decorator_with_p) each with the same
    # functionality but wrapping the string with different tags. We can definitely do much better
    # than that. Why not have a more general implementation for one that takes the tag to wrap
    # with as a string? yes please!

    def tag(tag_name):
        def tag_decorator(func):
            def wraper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))
            return wraper
        return tag_decorator

    @tag("div")
    @tag("p")
    def greeting_with_tag(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_tag("John") == '<div><p>Hello, John!</p></div>'
