import time

from selenium.webdriver.remote.webdriver import WebDriver

from application.constants import CATEGORY_FIELD_XPATH
from application.constants import LANGUAGE_FIELD_XPATH
from application.constants import ENGLISH_LANGUAGE_CHOICE_TEXT
from application.constants import OFFICE_FIELD_XPATH
from application.constants import SEARCH_BUTTON_XPATH
from application.constants import SERVICE_FIELD_XPATH


def enter_search_parameters(driver: WebDriver,
                            category_choice_text: str,
                            service_choice_text: str,
                            office_choice_text: str) -> WebDriver:
    """
    On the booking page, the search involves three choice fields:
        - Category: e.g. "Citizenship", "Residence Permit", etc.
        - Service: e.g. services of "Residence Permit" category are "Work", "Permanent Residence Permit", etc.
        - Office: e.g. "Lahti", "Oulu", "Lappeenranta", etc.
    """
    # Change the language to English
    language_field = driver.find_element_by_xpath(LANGUAGE_FIELD_XPATH)
    language_field.click()
    time.sleep(1)
    english_language_element = driver.find_element_by_partial_link_text(ENGLISH_LANGUAGE_CHOICE_TEXT)
    english_language_element.click()

    # Enter the appointment parameters.
    # First, select category
    time.sleep(1)
    category_field = driver.find_element_by_xpath(CATEGORY_FIELD_XPATH)
    category_field.click()
    time.sleep(1)
    category_option = driver.find_element_by_partial_link_text(category_choice_text)
    category_option.click()
    time.sleep(1)

    # Second, select service
    service_field = driver.find_element_by_xpath(SERVICE_FIELD_XPATH)
    service_field.click()
    time.sleep(1)
    service_option = driver.find_element_by_partial_link_text(service_choice_text)
    service_option.click()
    time.sleep(1)

    # Third, choose the office location of the service
    office_field = driver.find_element_by_xpath(OFFICE_FIELD_XPATH)
    office_field.click()
    time.sleep(1)
    office_option = driver.find_element_by_partial_link_text(office_choice_text)
    office_option.click()
    time.sleep(1)

    # Search availability
    search = driver.find_element_by_xpath(SEARCH_BUTTON_XPATH)
    search.click()
    time.sleep(3)  # Initial wait until everything loads

    return driver
