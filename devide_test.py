import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def test_divide_success():
    # Test case where division is successful
    result = divide(10, 2)
    assert result == 5

def test_divide_by_zero():
    # Test case where division by zero raises a ValueError
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        divide(10, 0)

# You can add more test cases as needed

if __name__ == "__main__":
    pytest.main()
