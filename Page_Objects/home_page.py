import time
from selenium.webdriver.common.by import By
from Utilities.test_base import TestBase
from Page_Objects.locators import SchoolLocators
from selenium.webdriver.support.ui import Select
import random
from Constants.constant import Constant


class SearchItem(TestBase):
    def __init__(self, driver):
        super().__init__(driver)    # used to call the __init__ method of the parent class TestBase
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def select_state(self,):
        self.driver.find_element(*SchoolLocators.DROPDOWN_STATE).click()

    def select_random_state(self):
        dropdown_element = self.driver.find_element(*SchoolLocators.DROPDOWN_STATE)
        select = Select(dropdown_element)
        options = select.options
        random_index = random.randint(1, len(options) - 1)
        select.select_by_index(random_index)
        selected_option = select.options[random_index]
        # print("Selected State:", selected_option.text)
        state_name = selected_option.text
        return state_name

    def select_random_city(self):
        self.driver.find_element(*SchoolLocators.DROPDOWN_CITY).click()

    def make_city_list(self):
        city_elements = self.driver.find_elements(*SchoolLocators.CITY_NAMES)
        random_index = random.randint(0, len(city_elements) - 1)
        selected_city_element = city_elements[random_index]
        selected_city_element.click()
        city_name = selected_city_element.find_element(By.TAG_NAME, "a").text
        # print("Selected City:", city_name)
        return city_name

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

        students_list = []
        grade_list = []

        for i in range(len(school_name_elements) * 2):
            if i % 2 == 1:
                xpath_expression = f"/html/body/div[1]/div[3]/table[3]/tbody/tr[{i + 1}]/td/table/tbody/tr/td[5]/font"
                students_elements = self.driver.find_element(By.XPATH, xpath_expression)
                if students_elements:
                    students = students_elements.text
                else:
                    students = ''
                students_list.append(students)

        for i in range(len(school_name_elements) * 2):
            if i % 2 == 1:
                xpath_expn = f"/html/body/div[1]/div[3]/table[3]/tbody/tr[{i + 1}]/td/table/tbody/tr/td[6]/font"
                grade_elements = self.driver.find_element(By.XPATH, xpath_expn)
                if grade_elements:
                    grades = grade_elements.text
                else:
                    grades = ''
                grade_list.append(grades)

        for i in range(len(school_name_elements)):

            school_name = school_name_elements[i].text
            phone = phone_elements[i].text
            if i+1 < len(county_elements):
                county = county_elements[i+1].text
            else:
                county = "N/A"
            students = students_list[i]
            grades = grade_list[i]

            # Write the data to the CSV file
            csv_writer.writerow([school_number, " ", school_name, " ", phone, county, students, grades])

            school_number += 1






