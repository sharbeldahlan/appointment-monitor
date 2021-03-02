import os

from dotenv import load_dotenv

# To get the environment variables
load_dotenv()

# ----------------------
# scraping.py constants
# ----------------------
# path of the chrome web driver to be used by selenium
DRIVER_PATH = os.getenv('DRIVER_PATH')
# url to the appointment booking page
WEBLINK = os.getenv('WEBLINK')

# Constants passed to find_element_by_* methods in scraper.py
LANGUAGE_FIELD_XPATH = '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/ul[1]/li/a/span'
CATEGORY_FIELD_XPATH = '/html/body/div[4]/div[2]/div/div[3]/div[1]/div[4]/div[1]/div/div/button/span[2]'
SERVICE_FIELD_XPATH = '/html/body/div[4]/div[2]/div/div[3]/div[1]/div[4]/div[2]/div/button/span[2]'
OFFICE_FIELD_XPATH = '/html/body/div[4]/div[2]/div/div[3]/div[1]/div[7]/div/button/span[1]'
SEARCH_BUTTON_XPATH = '/html/body/div[4]/div[2]/div/div[3]/div[1]/button'
NEXT_WEEK_BUTTON_CLASS_NAME = 'glyphicon-step-forward'

# Language choice
ENGLISH_LANGUAGE_CHOICE_TEXT = 'English'


# Usually, the the results of the next 14 weeks are displayed,
# but we loop 16 times each search just in case more weeks are added.
DISPLAYED_WEEKS = range(1, 16)

# The days of the week displayed in the results are found in elements having the xpath:
# '/html/body/div[4]/div[2]/div/div[5]/div/div[3]/div/div[2]/div[N]/div[1]/a'
#                                                                ^
# where N is the day of the week from 2 to 8. So, div[2] is Mon, div[3] is Tue. and so on.
INDEXES_FOR_DAYS_OF_THE_WEEK_DIV = range(2, 8)
