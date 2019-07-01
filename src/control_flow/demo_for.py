"""For statement

The For statement in Python differs a bit from what you may be used to in C or Pascal.
Rather than always interating over an arithmetic progression of numbers(like in Pascal), or
giving the user the ability to define both the iteration step and halting condition(as C), 
Python's for statement iterates over the items of any sequence(a list or a string), in the 
order that they appear in the sequence. For example(no pun intended):

"""

def test_for_statement():
    """FOR statement"""

    #Measure some strings
    words = ["cat", "window", "defenestrate"]
    words_length = 0

    for word in words:
        words_length += len(word)

    assert words_length == ( 3+ 6+ 12)
    
