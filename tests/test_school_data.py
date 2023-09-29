import os

import pytest
import time
from selenium.webdriver.common.by import By
from Utilities.test_base import TestBase
from Constants.constant import Constant
from Page_Objects.home_page import SchoolLocators
from Page_Objects.home_page import SearchItem
import pdb


@pytest.fixture(scope="module")
def test_base(driver):
    return TestBase(driver)


@pytest.mark.usefixtures("test_base")
def test_open_website(driver, test_base):
    test_base.clear_previous_reports_and_screenshots()

    logger = test_base.get_logger("test_school_data")
    logger.info("Starting the test_open_website function")
    screenshot_counter = 1

    search_item = SearchItem(driver)
    # pdb.set_trace()

    logger.info("Opening URL: %s", Constant.BASE_URL)
    search_item.open(Constant.BASE_URL)
    logger.info("Capturing screenshot: After opening website")
    test_base.capture_screenshot(f"website_opened_{screenshot_counter}", "test_open_website")
    screenshot_counter += 1

    search_item.wait_for_element(SchoolLocators.DROPDOWN_STATE)

    logger.info("Selecting a random state")
    selected_state = search_item.select_random_state()
    logger.info("Entering the selected state name: %s", selected_state)

    logger.info("Capturing screenshot: After Selecting State Name")
    test_base.capture_screenshot(f"Selected_State_{screenshot_counter}", "test_open_website")
    screenshot_counter += 1

    search_item.wait_for_element(SchoolLocators.DROPDOWN_CITY)

    logger.info("Selecting a random city")
    search_item.select_random_city()

    search_item.wait_for_element_interactable(SchoolLocators.CITY_LIST)

    main_window_handle = driver.window_handles[0]
    new_window_handle = driver.window_handles[1]
    driver.switch_to.window(new_window_handle)

    search_item.wait_for_element_interactable(SchoolLocators.CITY_NAMES)
    time.sleep(2)
    selected_city_name = search_item.make_city_list()
    driver.switch_to.window(main_window_handle)

    logger.info("Entering the selected city name: %s", selected_city_name)

    search_item.wait_for_element_interactable(SchoolLocators.CITY_INPUT)
    search_item.send_city_names(selected_city_name)
    time.sleep(2)
    logger.info("Capturing screenshot: After Selecting City Name")
    test_base.capture_screenshot(f"Selected_City_{screenshot_counter}", "test_open_website")
    screenshot_counter += 1

    search_item.search()
    search_item.wait_for_element(SchoolLocators.DATA_PAGE)
    time.sleep(5)

    header = ["no. ", " School Name ", " Phone ", " Country ", " Students ", " Grades "]
    test_base.create_csv_file("school_data.csv", header)
    logger.info("csv file is created")

    school_number = 1
    # Loop through multiple pages
    while True:
        # Fetch and write data from the current page
        search_item.fetch_and_write_data(test_base.csv_writer, school_number)
        school_number += len(driver.find_elements(By.XPATH, "//font[@face='Times']"))
        logger.info("data has been entered in csv file")

        logger.info("Capturing screenshot: After School Data is loaded")
        test_base.capture_screenshot(f"School_Data_{screenshot_counter}", "test_open_website")
        screenshot_counter += 1

        # Check if the "Next" button is available
        try:
            next_button = driver.find_element(By.XPATH, "//a[text()='Next >>']")
            next_button.click()
            time.sleep(4)  # Wait for the next page to load (adjust as needed)

        except Exception:
            break  # No more pages

    # Close the CSV file
    test_base.close_csv_file()
    logger.info("Finishing the test_open_website function")

    if __name__ == "__main__":
        report_dir = os.path.join(os.getcwd(), "..", "Reports")
        test_report_path = os.path.join(report_dir, "test_report.html")
        pytest.main(["-v", f"--html={test_report_path}"])







