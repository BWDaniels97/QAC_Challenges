''' 
Challenge of the Day

I have a function called string_gen() that will return a random 5-character-long string of 
lowercase letters. Write some tests for this function.

To reiterate, the output should always be:

- a string 
- 5 characters long 
- comprised of lowercase letters 

'''


import pytest
from programs import string_gen

def test_string_gen1():
	assert type(string_gen.string_gen()) is str

def test_string_gen2():
    assert len(string_gen.string_gen()) == 5

def test_string_gen3():
    assert (string_gen.string_gen()).islower() == True

