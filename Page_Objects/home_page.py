from selenium.webdriver.common.by import By

from Utilities.test_base import TestBase
from Page_Objects.locators import SchoolLocators
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class SearchItem(TestBase):
    def __init__(self, driver):
        super().__init__(driver)  # used to call the __init__ method of the parent class TestBase
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def select_state(self, ):
        self.driver.find_element(*SchoolLocators.DROPDOWN_STATE).click()

    def select_city(self):
        self.driver.find_element(*SchoolLocators.DROPDOWN_CITY).click()

    def get_state_name(self):
        state_name = os.environ.get('STATE_NAME')
        default_state = "Hawaii"  # Default state here
        return state_name.strip() if state_name is not None and state_name.strip() != "" else default_state

    def get_city_name(self):
        city_name = os.environ.get('CITY_NAME')
        default_city_name = "Kailua"  # Default city name
        return city_name.strip() if city_name is not None and city_name.strip() != "" else default_city_name


    # def make_city_list(self):
    #     city_name = self.get_city_name()
    #     city_elements = self.driver.find_elements(*SchoolLocators.CITY_NAMES)
    #     selected_city_element = None
    #     for i in city_elements:
    #         if i.text == city_name:
    #             selected_city_element = i
    #             break
    #     if selected_city_element:
    #         selected_city_element.click()
    #         return selected_city_element.text

    def make_city_list(self):
        city_name = self.get_city_name()
        city_elements = self.driver.find_elements(*SchoolLocators.CITY_NAMES)
        for i in city_elements:
            if i.text == city_name:
                i.click()
                return i.text

    def send_city_names(self, city_name):
        city_input = self.driver.find_element(*SchoolLocators.CITY_INPUT)
        city_input.clear()
        city_input.send_keys(city_name)

    def search(self):
        self.driver.find_element(*SchoolLocators.SEARCH_BUTTON).click()

    def next_btn(self):
        self.driver.find_element(*SchoolLocators.NEXT_BUTTON).click()

    def fetch_and_write_data(self, csv_writer):
        num_elements = self.driver.find_elements(*SchoolLocators.NUMBERS)

        school_name_elements = self.driver.find_elements(*SchoolLocators.SCHOOL_NAMES)
        phone_elements = self.driver.find_elements(*SchoolLocators.PHONE_NUMBERS)
        county_elements = self.driver.find_elements(*SchoolLocators.COUNTRY_NAMES)
        student_elements = self.driver.find_elements(*SchoolLocators.STUDENTS_COUNT)
        grade_elements = self.driver.find_elements(*SchoolLocators.GRADES)

        loop_length = min(len(school_name_elements), len(phone_elements), len(county_elements), len(student_elements),
                          len(grade_elements), len(num_elements))

        for i in range(loop_length):
            school_num = num_elements[i].text
            school_name = school_name_elements[i].text
            phone = phone_elements[i].text
            country = county_elements[i].text
            students = student_elements[i].text
            grades = grade_elements[i].text

            # Write the data to the CSV file
            csv_writer.writerow([school_num, school_name, phone, country, students, grades])

    def number_count(self):
        names = self.driver.find_elements(*SchoolLocators.SCHOOL_NAMES)
        return names
