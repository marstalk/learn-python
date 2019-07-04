"""For statement

The For statement in Python differs a bit from what you may be used to in C or Pascal.
Rather than always interating over an arithmetic progression of numbers(like in Pascal), or
giving the user the ability to define both the iteration step and halting condition(as C)
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

    assert words_length == (3+ 6+ 12)
    

    #If you need to modify the sequence you are interating over while inside the loop
    # (for example to duplicated selected items), it is recommended that you first make a copy.
    # Iterating over a sequence does not implicity make a copy. The slice notations makes this 
    # especially convinent:
    for word in words[:]:
        if(len(word) > 6):
            words.insert(0, word)

    # Otherwise with for w in words:, the example would attempt to create an infinite list,
    # inserting defenestrate over and over again.


    assert words == ['defenestrate', 'cat', 'window', 'defenestrate']
    
def hello(name):
    name += " Louisl"
    return "hello" + name
print(hello("jiacheng"))

