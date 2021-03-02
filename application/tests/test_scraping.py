import pytest
from selenium import webdriver

from application.constants import DRIVER_PATH
from application.constants import WEBLINK
from application.scraping import enter_search_parameters
from application.scraping import get_xpath_for_date_of_available_time_element
from application.scraping import get_xpath_for_possible_available_time_element
from application.scraping import scrape_booking_site


@pytest.fixture()
def driver_in_booking_site():
    """ Fixture for the web driver in a state after entering the booking site """
    driver = webdriver.Chrome(DRIVER_PATH)
    # Go to appointment page
    driver.implicitly_wait(3)
    driver.get(WEBLINK)
    yield driver
    # Teardown: we need to quit the driver at the end of the test.
    driver.quit()


def test_enter_search_parameters(driver_in_booking_site):
    """
    Test that, after entering example search parameters and clicking search,
    the page shows the available weeks ("wk1", "wk2", "wk3", ...)
    """
    driver = enter_search_parameters(
        driver=driver_in_booking_site,
        category_choice_text="Citizenship",
        service_choice_text="Citizenship application",
        office_choice_text="Helsinki"
    )
    # Assert that we get "wk" in the resulting page source.
    assert "wk" in driver.page_source


def test_scrape_booking_site():
    """
    Test for running the main scraping method.
    """
    result_dict = scrape_booking_site(category_choice_text="Citizenship",
                                      service_choice_text="Citizenship application",
                                      office_choice_text="Helsinki")
    assert 'available_time' in result_dict.keys()


def test_get_xpath_for_possible_available_time_element():
    """ Basic test to check that the get xpath for the possible available time works as expected"""
    expected_xpath = '/html/body/div[4]/div[2]/div/div[5]/div/div[3]/div/div[2]/div[3]/div[1]/a'
    # This is what we are looking for --------------------------------------------> ^
    assert get_xpath_for_possible_available_time_element(3) == expected_xpath


def test_get_xpath_for_date_of_available_time_element():
    """ Basic test to check that the get xpath for the date of the available time works as expected"""
    expected_xpath = '/html/body/div[4]/div[2]/div/div[5]/div/div[2]/div[3]/div[5]/span'
    # This is what we are looking for ----------------------------------------> ^
    assert get_xpath_for_date_of_available_time_element(5) == expected_xpath
