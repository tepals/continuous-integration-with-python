from maths import multiple, add


def test_multiple_3_4():
    assert multiple(3, 4) == 12


def test_add_3_4():
    assert add(3, 4) == 7


def test_failing_test():
    assert add(3, 4) == 5
