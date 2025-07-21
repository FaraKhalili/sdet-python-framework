import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Fixture for browser setup and teardown
from fixtures.browser_fixture import browser

# Test that uses the browser
def test_google_search(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("SDET tutorial")
    search_box.submit()
    assert "SDET" in browser.title
