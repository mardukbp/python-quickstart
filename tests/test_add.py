from proj.add import add


def test_add():
    assert add(3, 4) == 7

def test_add2():
    assert add(10, 0) == 10

def test_add3():
    assert add(-1, 1) == 0
