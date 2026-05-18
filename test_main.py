# test_main.py
import pytest
from main import add, subtract

def test_add():
    assert add(200, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5

if __name__ == '__main__':
    pytest.main()