"""Class Definition Syntax"""

def test_instance_object():
    """Instance Objects.

    Now what can we do with instance objects? The only operations understood by instace objects
    are attribute references. There are two kinds of valid attributes names:
    - data attributes
    - methods.
    """

    class DummyClass:
        """Dummy class"""
        pass

    dummy_instace = DummyClass()
    dummy_instace.temporary_attribute = 1
    assert dummy_instace.temporary_attribute == 1
    del dummy_instace.temporary_attribute