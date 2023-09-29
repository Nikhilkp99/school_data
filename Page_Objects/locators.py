from selenium.webdriver.common.by import By


class SchoolLocators:
    DROPDOWN_STATE = (By.XPATH, "//select[@name='State']")
    DROPDOWN_CITY = (By.XPATH, "//a[contains(text(),'Browse')]")
    CITY_LIST = (By.XPATH, "(//body)[1]")
    CITY_NAMES = (By.XPATH, "(//li)")
    SEARCH_BUTTON = (By.XPATH, "//input[@value='  Search  ']")
    DATA_PAGE = (By.XPATH, "//*[@class='nces']")
    CITY_INPUT = (By.XPATH, "//input[@name='City']")
    NEXT_BUTTON = (By.XPATH, "//a[text()='Next >>']")

    SCHOOL_NAMES = (By.XPATH, "//font[@face='Times']")
    PHONE_NUMBERS = (By.XPATH, "//font[contains(text(), '(') and contains(text(), ')')]")
    COUNTRY_NAMES = (By.XPATH, "//*[contains(text(), 'County')]")

    SCHOOL_NUMBERS = (By.XPATH, "//font[@face='Times']")










