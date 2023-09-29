import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    try:
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver_instance = webdriver.Chrome(service=chrome_service)
        driver_instance.maximize_window()
        yield driver_instance
    except Exception as e:
        print("An error occurred during driver setup:", e)


