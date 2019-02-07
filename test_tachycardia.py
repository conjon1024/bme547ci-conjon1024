# test_tachycardia.py


import pytest


def test_is_tachycardic_unit(): 
    from tachycardia import is_tachycardic

    result = is_tachycardic('tachycardic') #test lower case
    assert result == True


@pytest.mark.parametrize("in_word, expected", [
    ("TACHYCARDIC", True), #test upper case
    ("TaChyCarDIc", True), #test mixed case
    ("Bradycardic", False), #test different word
    ("  TachYcaRdic   ", True), #test leading/trailing spaces
    ("{!tAcHycArDIC; /", True), #test leading/trailing punctuation
    ("tachyac", False) #test misspelled word
])


def test_is_tachycardic_param(in_word, expected):
    from tachycardia import is_tachycardic

    answer = is_tachycardic(in_word)
    assert answer == expected