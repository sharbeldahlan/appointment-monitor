import pytest
from selenium import webdriver

from application.constants import BOOKING_SITE_URL
from application.constants import DRIVER_PATH
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
    driver.get(BOOKING_SITE_URL)
    yield driver
    # Teardown: we need to quit the driver at the end of the test.
    driver.quit()


@pytest.mark.parametrize(
    "service_choice, service_choice_text, office_choice",
    [
        ('rp_permanent', 'Permanent', 'Helsinki : Käenkuja'),
        ('citizenship_application', 'Citizenship application', 'Kuopio'),
    ]
)
def test_enter_search_parameters(service_choice, service_choice_text, office_choice, driver_in_booking_site):
    """
    Test that, after entering example search parameters and clicking search,
    the page shows:
     - the available weeks ("wk1", "wk2", "wk3", ...)
     - the search parameters that were entered
    """
    driver = enter_search_parameters(
        driver=driver_in_booking_site,
        service_choice=service_choice,
        office_choice=office_choice
    )
    # Assert that we get "wk" in the resulting page source.
    assert "wk" in driver.page_source
    assert office_choice in driver.page_source
    assert service_choice_text in driver.page_source


@pytest.mark.parametrize(
    "service_choice, office_choice",
    [
        ('rp_permanent', 'Helsinki : K'),
        ('citizenship_application', 'Kuopio'),
    ]
)
def test_scrape_booking_site(service_choice, office_choice):
    """
    Parametrized test for running the main scraping method using different service
    and office choices. Since the booking webpage content (driver.page_source)
    is hard to simulate, the test is written in a funky fashion to use conditionals
    for the two different possible outcomes of scrape_booking_site() function.
    """
    result_dict = scrape_booking_site(service_choice, office_choice)
    if result_dict:
        assert 'available_time' in result_dict.keys()
    else:
        assert result_dict is None


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
