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

# Migri booking page has Categories and Services:
# Example: Category --> "Citizenship"; Service --> "Work", "Permanent Residence Permit", etc.
# Note: only "Citizenship" and "Residence Permit" categories are supported for now

# Service choices - the machine readable ones used for the choices and the mappings
CITIZENSHIP_APPLICATION = 'citizenship_application'
CITIZENSHIP_DECLARATION = 'citizenship_declaration'
CITIZENSHIP_RELEASE = 'citizenship_release'
CITIZENSHIP_MAARIANHAMINA = 'citizenship_maarianhamina'
RP_WORK = 'rp_work'
RP_FAMILY = 'rp_family'
RP_STUDIES = 'rp_studies'
RP_OTHER_GROUNDS = 'rp_other_grounds'
RP_PERMANENT_RESIDENCE = 'rp_permanent'
RP_RENEWAL = 'rp_renewal'

# Category choices
CITIZENSHIP_CATEGORY = 'Citizenship'
RESIDENCE_PERMIT_CATEGORY = 'Residence'

# Citizenship category service texts, as appearing on the booking website:
# This will be the text with which the search for the elements will happen in scraping.py's find_element.
CITIZENSHIP_SERVICE_APPLICATION = 'Citizenship application'
CITIZENSHIP_SERVICE_DECLARATION = 'Citizenship declaration'
CITIZENSHIP_SERVICE_RELEASE = 'Release'
CITIZENSHIP_SERVICE_MAARIANHAMINA_MATTERS = 'Ahvenanmaa/Maarianhamina: Citizenship matters'

# Residence permit category service texts, as appearing on the booking website:
# This will be the text with which the search for the elements will happen in scraping.py's find_element.
RESIDENCE_PERMIT_SERVICE_WORK = 'Work'
RESIDENCE_PERMIT_SERVICE_FAMILY = 'Family'
RESIDENCE_PERMIT_SERVICE_STUDIES = 'Studies'
RESIDENCE_PERMIT_SERVICE_OTHER_GROUNDS = 'Other grounds'
RESIDENCE_PERMIT_SERVICE_PERMANENT = 'Permanent'
RESIDENCE_PERMIT_SERVICE_RENEWAL = 'Renewal'

# Mapping between choice of the service and the Category field
# format: {<Service choice>: <Text of corresponding category as it appears on the webpage>}
CATEGORY_TEXT_MAPPING = {
    CITIZENSHIP_APPLICATION: CITIZENSHIP_CATEGORY,
    CITIZENSHIP_DECLARATION: CITIZENSHIP_CATEGORY,
    CITIZENSHIP_RELEASE: CITIZENSHIP_CATEGORY,
    CITIZENSHIP_MAARIANHAMINA: CITIZENSHIP_CATEGORY,
    RP_WORK: RESIDENCE_PERMIT_CATEGORY,
    RP_FAMILY: RESIDENCE_PERMIT_CATEGORY,
    RP_STUDIES: RESIDENCE_PERMIT_CATEGORY,
    RP_OTHER_GROUNDS: RESIDENCE_PERMIT_CATEGORY,
    RP_PERMANENT_RESIDENCE: RESIDENCE_PERMIT_CATEGORY,
    RP_RENEWAL: RESIDENCE_PERMIT_CATEGORY,
}

# Mapping between choice of the service and the Service field
# format: {<Service choice>: <Text of corresponding service as it appears on the webpage>}
SERVICE_TEXT_MAPPING = {
    CITIZENSHIP_APPLICATION: CITIZENSHIP_SERVICE_APPLICATION,
    CITIZENSHIP_DECLARATION: CITIZENSHIP_SERVICE_DECLARATION,
    CITIZENSHIP_RELEASE: CITIZENSHIP_SERVICE_RELEASE,
    CITIZENSHIP_MAARIANHAMINA: CITIZENSHIP_SERVICE_MAARIANHAMINA_MATTERS,
    RP_WORK: RESIDENCE_PERMIT_SERVICE_WORK,
    RP_FAMILY: RESIDENCE_PERMIT_SERVICE_FAMILY,
    RP_STUDIES: RESIDENCE_PERMIT_SERVICE_STUDIES,
    RP_OTHER_GROUNDS: RESIDENCE_PERMIT_SERVICE_OTHER_GROUNDS,
    RP_PERMANENT_RESIDENCE: RESIDENCE_PERMIT_SERVICE_PERMANENT,
    RP_RENEWAL: RESIDENCE_PERMIT_SERVICE_RENEWAL,
}

# Office choices:
HELSINKI_KAENKUJA = 'helsinki_kaenkuja'
HELSINKI_MALMI = 'helsinki_malmi'
KUOPIO = 'kuopio'
LAHTI = 'lahti'
LAPPEENRANTA = 'lappeenranta'
OULU = 'oulu'
ROVANIEMI = 'rovaniemi'
TAMPERE = 'tampere'
TURKU = 'turku'
VAASA = 'vaasa'

OFFICE_CHOICES = (
    (HELSINKI_KAENKUJA, 'Helsinki : K'),
    (HELSINKI_MALMI, 'Helsinki : M'),
    (KUOPIO, 'Kuopio'),
    (LAHTI, 'Lahti'),
    (LAPPEENRANTA, 'Lappeenranta'),
    (OULU, 'Oulu'),
    (ROVANIEMI, 'Rovaniemi'),
    (TAMPERE, 'Tampere'),
    (TURKU, 'Turku'),
    (VAASA, 'Vaasa'),
)

# Usually, the the results of the next 14 weeks are displayed,
# but we loop 16 times each search just in case more weeks are added.
DISPLAYED_WEEKS = range(1, 16)

# The days of the week displayed in the results are found in elements having the xpath:
# '/html/body/div[4]/div[2]/div/div[5]/div/div[3]/div/div[2]/div[N]/div[1]/a'
#                                                                ^
# where N is the day of the week from 2 to 8. So, div[2] is Mon, div[3] is Tue. and so on.
INDEXES_FOR_DAYS_OF_THE_WEEK_DIV = range(2, 8)
