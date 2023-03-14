import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("Hello...........")
@pytest.mark.xfail
def test_secondProgram():
    print("Hello....PYTEST.......")
