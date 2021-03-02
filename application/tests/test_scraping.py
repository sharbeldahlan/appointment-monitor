from selenium import webdriver

from application.constants import DRIVER_PATH
from application.constants import WEBLINK
from application.scraping import enter_search_parameters
from application.scraping import scrape_booking_site


def test_enter_search_parameters():
    """
    Test that, after entering example search parameters and clicking search,
    the page shows the available weeks ("wk1", "wk2", "wk3", ...)
    """
    # Create a WebDriver instance
    driver = webdriver.Chrome(DRIVER_PATH)

    # Go to appointment page
    driver.implicitly_wait(3)
    driver.get(WEBLINK)

    # Enter some search parameters such as "Citizenship application" and "Helsinki"
    driver = enter_search_parameters(
        driver=driver,
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
