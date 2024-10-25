from src.math_operations import add, sub

def test_add():
    assert add(2,3)==5
    assert add(5,8)==13
    assert add(-1,1)==0

def test_sub():
    assert sub(13,5)==8
    assert sub(4,3)==1
    assert(3,3)==0
    assert(2,3)==-1