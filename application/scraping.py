import time
from typing import Dict
from typing import Optional

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from application.constants import BOOKING_SITE_URL
from application.constants import CATEGORY_FIELD_XPATH
from application.constants import CATEGORY_TEXT_MAPPING
from application.constants import DISPLAYED_WEEKS
from application.constants import DRIVER_PATH
from application.constants import ENGLISH_LANGUAGE_CHOICE_TEXT
from application.constants import INDEXES_FOR_DAYS_OF_THE_WEEK_DIV
from application.constants import LANGUAGE_FIELD_XPATH
from application.constants import NEXT_WEEK_BUTTON_CLASS_NAME
from application.constants import OFFICE_FIELD_XPATH
from application.constants import SEARCH_BUTTON_XPATH
from application.constants import SERVICE_FIELD_XPATH
from application.constants import SERVICE_TEXT_MAPPING


def scrape_booking_site(service_choice: str, office_choice: str) -> Optional[Dict[str, str]]:
    """
    Main scraping function that:
        - creates a driver,
        - goes to the booking site,
        - enters the search parameters
        - scrapes through the search results
        - and returns the result dict {'available_time': available_time_str, 'date': date_str}
    """
    driver = webdriver.Chrome(DRIVER_PATH)

    # Go to appointment page
    driver.implicitly_wait(3)
    driver.get(BOOKING_SITE_URL)

    driver = enter_search_parameters(
        driver=driver,
        service_choice=service_choice,
        office_choice=office_choice
    )
    result_dict = scrape_through_search_results(driver=driver)

    driver.quit()

    return result_dict


def enter_search_parameters(driver: WebDriver, service_choice: str, office_choice: str) -> WebDriver:
    """
    On the booking page, the search involves three choice fields:
        - Category: e.g. "Citizenship", "Residence Permit", etc.
        - Service: e.g. services of "Residence Permit" category are "Work", "Permanent Residence Permit", etc.
        - Office: e.g. "Lahti", "Oulu", "Lappeenranta", etc.
    """
    # Extract the textual representation of the choice parameters from the passed choices
    category_choice_text = CATEGORY_TEXT_MAPPING[service_choice]
    service_choice_text = SERVICE_TEXT_MAPPING[service_choice]

    # Change the language to English
    language_field = driver.find_element_by_xpath(LANGUAGE_FIELD_XPATH)
    language_field.click()
    english_language_element = driver.find_element_by_partial_link_text(ENGLISH_LANGUAGE_CHOICE_TEXT)
    english_language_element.click()
    time.sleep(2)

    # Enter the appointment parameters.
    # First, select category
    category_field = driver.find_element_by_xpath(CATEGORY_FIELD_XPATH)
    category_field.click()
    category_option = driver.find_element_by_partial_link_text(category_choice_text)
    category_option.click()
    time.sleep(2)

    # Second, select service
    service_field = driver.find_element_by_xpath(SERVICE_FIELD_XPATH)
    service_field.click()
    service_option = driver.find_element_by_partial_link_text(service_choice_text)
    service_option.click()
    time.sleep(2)

    # Third, choose the office location of the service
    office_field = driver.find_element_by_xpath(OFFICE_FIELD_XPATH)
    office_field.click()
    office_option = driver.find_element_by_partial_link_text(str(office_choice))
    office_option.click()
    time.sleep(2)

    # Search availability
    search = driver.find_element_by_xpath(SEARCH_BUTTON_XPATH)
    search.click()
    time.sleep(5)  # Initial wait until everything loads

    return driver


def scrape_through_search_results(driver: WebDriver) -> Optional[Dict[str, str]]:
    """
    Loop through each week displayed, through each day of the week, to find possible available times.
    If available appointment time is displayed in a div, then return a dict with the available time and date.
    Otherwise, return None.
    """
    for _ in DISPLAYED_WEEKS:
        for day_index in INDEXES_FOR_DAYS_OF_THE_WEEK_DIV:
            possible_available_time_div = driver.find_element_by_xpath(
                get_xpath_for_possible_available_time_element(day_index)
            )

            # Primitive way of checking if available time is displayed in a div
            if ':' in possible_available_time_div.text:
                # There is an available time displayed in this div
                available_time_str = possible_available_time_div.text
                # Get the date of that available time, knowing that:
                # the day_index of the available date will be the same as day_index of available time.
                date_of_available_time = driver.find_element_by_xpath(
                    get_xpath_for_date_of_available_time_element(day_index)
                )
                date_str = date_of_available_time.text

                result_dict = {'available_time': available_time_str, 'date': date_str}
                return result_dict

        # Week finished, nothing found, click next.
        next_week_button = driver.find_element_by_class_name(NEXT_WEEK_BUTTON_CLASS_NAME)
        next_week_button.click()
        time.sleep(2)  # wait until next page loads

    return None  # No available appointments found


# xpath for divs showing the possible available times:
def get_xpath_for_possible_available_time_element(day_index: int) -> str:
    """
    The element showing potential available times displayed in the results are found in divs having the xpath:

    '/html/body/div[4]/div[2]/div/div[5]/div/div[3]/div/div[2]/div[N]/div[1]/a'
                                                                   ^
    where N is the day of the week from 2 to 8. So, div[2] is Mon, div[3] is Tue. and so on.
    """
    return f'/html/body/div[4]/div[2]/div/div[5]/div/div[3]/div/div[2]/div[{day_index}]/div[1]/a'


# xpath for divs showing the date of available times:
def get_xpath_for_date_of_available_time_element(day_index: int) -> str:
    """
    The element showing date of the available time is found in the div having the xpath:

    '/html/body/div[4]/div[2]/div/div[5]/div/div[2]/div[3]/div[N]/span'
                                                               ^
    where N is the day of the week from 2 to 8.
    """
    return f'/html/body/div[4]/div[2]/div/div[5]/div/div[2]/div[3]/div[{day_index}]/span'
