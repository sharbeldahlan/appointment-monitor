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

# Language choice
ENGLISH_LANGUAGE_CHOICE_TEXT = 'English'
