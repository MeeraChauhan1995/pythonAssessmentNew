import pytest

@pytest.mark.usefixtures("setup")

class TestExample:
    def test_fixtureDemo(self):
        print("I will execute steps in fixture demo method....")
    def test_fixtureDemo1(self):
        print("I will execute steps in fixture demo method....")
    def test_fixtureDemo2(self):
        print("I will execute steps in fixture demo method....")


