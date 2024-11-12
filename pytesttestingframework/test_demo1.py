# Any pytest file should start with test_
# Test method should start with test keyword
# Any code should be wrapped in method body only
# To run from terminal all the test cases py.test command
# py.test -v with verbose for more information about test cases.
# py.test -s for logs
# Run test using regex py.test -k method name keyword. e.g. py.test -k keyword
# Grouping the test cases and run we can use mark in pytest. Syntax - @pytest.mark.tag name. To run this py.test -m tagname
# To skip a test : add @pytest.mark.skip to the test method
# To skip reporting a test case in report file: @pytest.mark.xfail


import pytest


@pytest.mark.smoke
def test_first_program(setup):
    print('Hello')


# @pytest.mark.skip
def test_second_creditcard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"
