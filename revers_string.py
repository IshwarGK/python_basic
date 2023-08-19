import pytest


def get_revers(str1):
    if str1 == None:
        return None
    
    str2 = str1[::-1]
    return str2


def test_get_revers():
    actual = "aidnI morf ma I"
    str1 = "I am from India"
    assert actual == get_revers(str1)

def test_get_revers_one_char():
    actual = "A"
    assert actual == get_revers("A")
    
def test_none_string():
    actual = None
    assert actual == get_revers(None)
    

def test_negative_case():
    actual = "I am from India"
    assert actual != get_revers(actual)

if __name__ == "__main__":
    str1 = "I am from India"
    print(get_revers(str1))
    