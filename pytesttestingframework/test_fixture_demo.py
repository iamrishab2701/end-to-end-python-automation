import pytest


@pytest.mark.usefixtures("setup")
class TestFixture_Demo:

    def test_fixture_demo(self):
        print("I will execute steps in fixture demo method")

    def test_fixture_demo1(self):
        print("I will execute steps in fixture demo1 method")

    def test_fixture_demo2(self):
        print("I will execute steps in fixture demo2 method")

    def test_fixture_demo3(self):
        print("I will execute steps in fixture demo3 method")
