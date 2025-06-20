from src.math_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-2,3)==1
    assert add(2,-3)== -1

def test_sub():
    assert sub(2,3)==-1
    assert sub(-2,3)==-5
    assert sub(2,-3)== 5
    assert sub(20,3)== 17