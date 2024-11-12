import pytest


# fixture provide pre- and post-test execution steps
# It can be done using @pytest.fixture and then mention the method as argument in the test method.
# If you want to create teardown then add yield in the fixture method. Anything added after yield will execute post test execution.
# conftest.py has all the fixture which is common to all the test method
# Fixture also can be on class level in case you don't want to add same fixture on the test method. By add @pytest.make.usefixtures('fixturename') above the class.
# We can provide the scope to the fixture as well by @pytest.fixture(scope="class")
# For multiple data set also can be provided using fixture e.g. @pytest.fixture(params=[("Chrome", "Rishab"), ("Firefox", "Rishab"), ("Edge", "Rishab")])

@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture
def data_load():
    print('User profile data is being created')
    return ["Rishab", "Singh", "singhrishab166@carrd.co"]


@pytest.fixture(params=[("Chrome", "Rishab"), ("Firefox", "Rishab"), ("Edge", "Rishab")])  # For multiple data sets
def cross_browser(request):
    return request.param
