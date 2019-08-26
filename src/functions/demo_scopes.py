"""Scopes and Namespace

A Namespace is a mapping from names to objects.


A Scope is a textual region of a python program where a namespace is directly accessible.


"""


test_variable = "initial global value"

def test_function_scope():

    test_variable = "initial value inside test function"

    def do_local():
        test_variable = "local value"
        return test_variable

    def do_nonlocal():
        nonlocal test_variable
        test_variable = "nonlocal value"
        return test_variable

    def do_global():
        global test_variable
        test_variable = "global value"
        return test_variable

    assert test_variable == "initial value inside test function"

    do_local()
    assert test_variable == "initial value inside test function"

    do_nonlocal()
    assert test_variable == "nonlocal value"

    do_global()
    assert test_variable == "nonlocal value"

def test_global_value():
    global test_variable
    test_variable = "global value"
    assert test_variable == "global value"

def test_value_pass(test_variable):
    test_variable = "test_value_pass"
    return
test_value_pass(test_variable)
print(test_variable)

def test_value_pass(test_variable):
    test_variable = "test_value_pass"
    return test_variable
test_variable = test_value_pass(test_variable)
print(test_variable)


"""
总结为以下几点：
1， 默认的变量是local级别，即在本方法中寻找变量，如果找不到，则去外面的方法找，如果找不到，则去global中找，如果找不到，则去build-in中找
2， 使用nonlocal修饰的变量，则直接去外面的方法找，如果找不到则去global中找，如果找不到，则去build-in中找。
3， 如果global修饰的变量，则直接去global中找，如果找不到，则去build-in中

慎用此种方式，尽量使用传递和返回的方式。value pass like Java.
"""