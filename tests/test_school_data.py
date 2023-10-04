import os
import pytest
import time
from Utilities.test_base import TestBase
from Constants.constant import Constant
from Page_Objects.home_page import SchoolLocators
from Page_Objects.home_page import SearchItem
# import pdb
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@pytest.fixture(scope="module")
def test_base(driver):
    return TestBase(driver)


@pytest.mark.usefixtures("test_base")
def test_open_website(driver, test_base):
    test_base.clear_previous_reports_and_screenshots()

    logger = test_base.get_logger("test_school_data")
    logger.info("Starting the test_open_website function")

    search_item = SearchItem(driver)
    # pdb.set_trace()

    logger.info("Opening URL: %s", Constant.BASE_URL)
    search_item.open(Constant.BASE_URL)
    logger.info("Capturing screenshot: After opening website")
    test_base.capture_screenshot(f"website_opened_", "test_open_website")

    search_item.wait_for_element(SchoolLocators.DROPDOWN_STATE)

    # getting the value of an environment variable named "STATE_NAME"
    state_name = os.environ.get('STATE_NAME')

    default_state = "Hawaii"  # default state here

    selected_state = state_name.strip() if state_name is not None and state_name.strip() != "" else default_state

    # Find the dropdown element
    dropdown_element = search_item.find_element(*SchoolLocators.DROPDOWN_STATE)

    # Use the Select class to work with the dropdown
    select = Select(dropdown_element)

    select.select_by_visible_text(selected_state)
    selected_state = select.first_selected_option.text

    logger.info("Entering the selected state name: %s", selected_state)

    logger.info("Capturing screenshot: After Selecting State Name")
    test_base.capture_screenshot(f"Selected_State_", "test_open_website")

    # getting the value of an environment variable named "CITY_NAME"
    city_name = os.environ.get('CITY_NAME')

    default_city_name = "Kailua"  # default city name
    selected_city_name = city_name.strip() if city_name is not None and city_name.strip() != "" else default_city_name

    logger.info("Entering the selected city name: %s", selected_city_name)

    search_item.wait_for_element_interactable(SchoolLocators.CITY_INPUT)
    search_item.send_city_names(selected_city_name)
    time.sleep(2)
    logger.info("Capturing screenshot: After Selecting City Name")
    test_base.capture_screenshot(f"Selected_City_", "test_open_website")

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
        school_number += len(search_item.number_count())
        logger.info("data has been entered in csv file")

        logger.info("Capturing screenshot: After School Data is loaded")
        test_base.capture_screenshot(f"School_Data_", "test_open_website")

        # Check if the "Next" button is available
        try:
            search_item.next_btn()
            time.sleep(4)
            test_base.wait_for_element_interactable(SchoolLocators.SCHOOL_NAMES)

        except Exception:
            break  # No more pages

    # Close the CSV file
    test_base.close_csv_file()
    logger.info("Finishing the test_open_website function")


if __name__ == "__main__":
    report_dir = os.path.join(os.getcwd(), "..", "Reports")
    test_report_path = os.path.join(report_dir, "test_report.html")
    pytest.main(["-v", f"--html={test_report_path}"])








