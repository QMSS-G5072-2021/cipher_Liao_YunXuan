#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pytest

def cipher(text, shift, encrypt=True):
    assert not isinstance(shift, str), 'Shift should not be a string'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

def test_cipher_word():
    example = 'test'
    expected = 'vguv'
    actual = cipher(example,2)
    assert actual == expected,"The word should be vguv"
    
def test_cipher_negative():
    example = 'test'
    expected = 'sdrs'
    actual = cipher(example,-1)
    assert actual == expected,"The word should be sdrs"
    
def test_cipher_symbol():
    example = 'test!'
    expected = 'vguv!'
    actual = cipher(example,2)
    assert actual == expected,"The word should be vguv!"

def test_cipher_exception():
    with pytest.raises(AssertionError):
        cipher('test', 'one')


