import pytest


@pytest.mark.usefixtures('data_load')  # accessing the data driven fixture
class TestExample2:

    def test_edit_profile(self, data_load):  # data from the fixture
        print(data_load)

    @pytest.mark.usefixtures('cross_browser')  # Multiple data set
    def test_cross_test(self, cross_browser):
        print(cross_browser)