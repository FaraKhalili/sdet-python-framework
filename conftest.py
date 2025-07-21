import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("🚀 Setup: Launching browser")
    driver = webdriver.Chrome()
    yield driver
    print("🧹 Teardown: Closing browser")
    driver.quit()