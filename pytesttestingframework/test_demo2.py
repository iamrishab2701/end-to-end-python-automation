import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_third_program():
    msg = "hello"
    assert msg == "Hello", "Test failed because strings do not match"
