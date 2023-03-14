import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executing first....")
    yield
    print("I will excute last")
