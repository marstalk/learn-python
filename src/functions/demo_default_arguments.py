


def power_of(number, power=2):
    return number ** power

def non_argument(number):
    return 2


def test_default_argument():
    assert power_of(3) == 9
    assert power_of(3, 3) == 27
    assert non_argument(3) == 2

"""
总结为以下：
1， 可快速实现方法重载，相比Java而言。
2， 如果参数没有默认值，那么该参数是必传的。
3， 如果参数有默认值，那么该参数是可选的。
"""