import pytest

@pytest.fixture()
def setUp():
    print("once before every method")


def testmethod1(setUp):
    print("test method 1")

def second(SetUp):
    print("second")