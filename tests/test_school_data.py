import os
import pytest
import time
from Utilities.test_base import TestBase
from Constants.constant import Constant
from Page_Objects.home_page import SchoolLocators
from Page_Objects.home_page import SearchItem
# import pdb
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

    selected_state = search_item.get_state_name()
    logger.info("Entering the selected state name: %s", selected_state)
    # Find the dropdown element
    dropdown_element = search_item.find_element(*SchoolLocators.DROPDOWN_STATE)

    state_locator = SchoolLocators.DROPDOWN_STATE
    selected_state = test_base.select(state_locator, selected_state)

    logger.info("Capturing screenshot: After Selecting State Name")
    test_base.capture_screenshot(f"Selected_State_", "test_open_website")

    search_item.select_city()
    search_item.wait_for_element_interactable(SchoolLocators.CITY_LIST)

    main_window_handle = driver.window_handles[0]
    new_window_handle = driver.window_handles[1]
    driver.switch_to.window(new_window_handle)
    search_item.wait_for_element_interactable(SchoolLocators.CITY_NAMES)

    selected_city_name = search_item.make_city_list()
    driver.switch_to.window(main_window_handle)

    logger.info("Entering the selected city name: %s", selected_city_name)

    search_item.wait_for_element_interactable(SchoolLocators.CITY_INPUT)
    search_item.send_city_names(selected_city_name)
    time.sleep(2)
    logger.info("Capturing screenshot: After Selecting City Name")
    test_base.capture_screenshot(f"Selected_City_", "test_open_website")

    search_item.search()
    search_item.wait_for_element(SchoolLocators.DATA_PAGE)
    time.sleep(5)

    test_base.create_csv_file("school_data.csv")
    logger.info("csv file is created")

    # Loop through multiple pages
    while True:
        # Fetch and write data from the current page
        search_item.fetch_and_write_data(test_base.csv_writer)
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
