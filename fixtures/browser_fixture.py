import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("🚀 Setup: Launching Chrome browser")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("🧹 Teardown: Closing browser")
    driver.quit()