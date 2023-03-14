import pytest
@pytest.mark.smoke
@pytest.mark.skip
def test_Program():
    msg = "class 222222"
    assert msg == "classs............"

def test_Creditcard():
    a=6
    b=2
    c=  a+ b
    print(c)
    
def test_Creditcardagain():
    print("testing -------------------")