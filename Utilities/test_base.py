import csv
import logging
import inspect
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from selenium.webdriver.support.ui import Select


class TestBase:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_interactable(self, locator, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        return element

    def select(self, locator, option_text):
        element = self.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(option_text)

    def create_csv_file(self, filename):
        self.csv_file = open(filename, "w", newline="", encoding="utf-8")
        self.csv_writer = csv.writer(self.csv_file)

    def write_to_csv(self, data):
        self.csv_writer.writerow(data)

    def close_csv_file(self):
        self.csv_file.close()

    @staticmethod
    def get_logger(self):
        calling_function_name = inspect.stack()[1][3]
        logger = logging.getLogger(calling_function_name)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        report_dir = os.path.join(os.getcwd(), "..", "Reports")
        log_dir = os.path.join(report_dir, "Logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file_path = os.path.join(log_dir, "logfile.log")

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def capture_screenshot(self, name, test_case_name):
        report_dir = os.path.join(os.getcwd(), "..", "Reports")  # Move one level up (. .)
        screenshot_dir = os.path.join(report_dir, "Screenshots")

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")

        screenshot_path = os.path.join(screenshot_dir, f"{test_case_name}_{timestamp}.png")

        self.driver.save_screenshot(screenshot_path)

    def clear_previous_reports_and_screenshots(self):
        report_dir = os.path.join(os.getcwd(), "..", "Reports")
        screenshot_dir = os.path.join(report_dir, "Screenshots")
        log_dir = os.path.join(report_dir, "Logs")

        # Delete existing screenshots
        if os.path.exists(screenshot_dir):
            for file in os.listdir(screenshot_dir):
                file_path = os.path.join(screenshot_dir, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print("Error while deleting file:", e)

        # Delete existing logs
        if os.path.exists(log_dir):
            for file in os.listdir(log_dir):
                file_path = os.path.join(log_dir, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print("Error while deleting file:", e)




