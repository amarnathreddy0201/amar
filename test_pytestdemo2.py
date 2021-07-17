import pytest

@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield
    print("once after every method")

def test1(setup):
    print("test 1")

def test2(setup):
    print("test 2")