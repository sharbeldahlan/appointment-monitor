from unittest.mock import call
from unittest.mock import patch

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


@patch('application.scraping.enter_search_parameters')
@patch('application.scraping.scrape_through_search_results')
@patch('application.scraping.webdriver')
def test_scrape_booking_site__calls_sub_methods_with_correct_parameters(mock_driver_before_search,
                                                                        mock_scrape_through_search_results,
                                                                        mock_enter_search_parameters):
    """
    Test scrape_booking_site runs sanely by calling the sub methods:
        - enter_search_parameters()
        - scrape_through_search_results()
    with the correct parameters.
    """
    scrape_booking_site(service_choice='foo', office_choice='bar')

    # Assert that the Chrome driver with its state *before* the search is passed to enter_search_parameters()
    assert mock_enter_search_parameters.call_args == call(driver=mock_driver_before_search.Chrome(),
                                                          service_choice='foo',
                                                          office_choice='bar')

    mock_driver_after_search = mock_enter_search_parameters.return_value
    # Assert that the Chrome driver with its state *after* the search is passed to scrape_through_search_results()
    assert mock_scrape_through_search_results.call_args == call(driver=mock_driver_after_search)


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


def test_get_xpath_for_possible_available_time_element():
    """ Basic test to check that the get xpath for the possible available time works as expected """
    expected_xpath = '/html/body/div[4]/div[2]/div/div[5]/div/div[3]/div/div[2]/div[3]/div[1]/a'
    # This is what we are looking for --------------------------------------------> ^
    assert get_xpath_for_possible_available_time_element(3) == expected_xpath


def test_get_xpath_for_date_of_available_time_element():
    """ Basic test to check that the get xpath for the date of the available time works as expected"""
    expected_xpath = '/html/body/div[4]/div[2]/div/div[5]/div/div[2]/div[3]/div[5]/span'
    # This is what we are looking for ----------------------------------------> ^
    assert get_xpath_for_date_of_available_time_element(5) == expected_xpath
