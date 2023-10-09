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

    NUMBERS = (By.XPATH, "//div[@class='sfsContent']/table[3]/tbody/tr/td/table/tbody/tr/td[1]")
    SCHOOL_NAMES = (By.XPATH, "//div[@class='sfsContent']/table[3]/tbody/tr/td/table/tbody/tr/td[2]")
    PHONE_NUMBERS = (By.XPATH, "//div[@class='sfsContent']/table[3]/tbody/tr/td/table/tbody/tr/td[3]")
    COUNTRY_NAMES = (By.XPATH, "//div[@class='sfsContent']/table[3]/tbody/tr/td/table/tbody/tr/td[4]")
    STUDENTS_COUNT = (By.XPATH, "//div[@class='sfsContent']/table[3]/tbody/tr/td/table/tbody/tr/td[5]")
    GRADES = (By.XPATH, "//div[@class='sfsContent']/table[3]/tbody/tr/td/table/tbody/tr/td[6]")

    SCHOOL_NUMBERS = (By.XPATH, "//font[@face='Times']")

    CITY_CLICK = (By.XPATH, "html/body/ul/li")















