from Utilities.test_base import TestBase
from Page_Objects.locators import SchoolLocators
from selenium.webdriver.support.ui import Select

class SearchItem(TestBase):
    def __init__(self, driver):
        super().__init__(driver)    # used to call the __init__ method of the parent class TestBase
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def select_state(self,):
        self.driver.find_element(*SchoolLocators.DROPDOWN_STATE).click()

    def select_random_city(self):
        self.driver.find_element(*SchoolLocators.DROPDOWN_CITY).click()

    def send_city_names(self, city_name):
        city_input = self.driver.find_element(*SchoolLocators.CITY_INPUT)
        city_input.clear()
        city_input.send_keys(city_name)

    def search(self):
        self.driver.find_element(*SchoolLocators.SEARCH_BUTTON).click()

    def next_btn(self):
        self.driver.find_element(*SchoolLocators.NEXT_BUTTON).click()

    def fetch_and_write_data(self, csv_writer, school_number):

        school_name_elements = self.driver.find_elements(*SchoolLocators.SCHOOL_NAMES)
        phone_elements = self.driver.find_elements(*SchoolLocators.PHONE_NUMBERS)
        county_elements = self.driver.find_elements(*SchoolLocators.COUNTRY_NAMES)
        student_elements = self.driver.find_elements(*SchoolLocators.STUDENTS_COUNT)
        grade_elements = self.driver.find_elements(*SchoolLocators.GRADES)

        for i in range(len(school_name_elements)):
            school_name = school_name_elements[i].text
            phone = phone_elements[i].text
            if i+1 < len(county_elements):
                county = county_elements[i+1].text
            else:
                county = "N/A"
            students = student_elements[i].text
            grades = grade_elements[i].text

            # Write the data to the CSV file
            csv_writer.writerow([school_number, " ", school_name, " ", phone, county, students, grades])

            school_number += 1

    def number_count(self):
        names = self.driver.find_elements(*SchoolLocators.SCHOOL_NAMES)
        return names











