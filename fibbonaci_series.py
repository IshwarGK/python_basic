import pytest


def get_fibbonachi_series(num):
    a = 0
    b = 1
    list1 = []
    for i in range(num):
        list1.append(a)
        a, b = b, a + b
    return list1

print(get_fibbonachi_series(5))

def test_get_fibbonachi_series():
    actual_list1 = [0, 1, 1, 2, 3]
    
    assert actual_list1 == get_fibbonachi_series(5)
    
if __name__ == "__main__":
    pytest.main()