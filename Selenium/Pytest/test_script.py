import pytest
from selenium import webdriver
from datetime import datetime
import os


@pytest.fixture
def browser():
    # Replace 'path/to/chromedriver' with the actual path to your chromedriver executable
    chrome_driver_path = r'C:\Users\HP\PycharmProjects\SDET_shubham\Selenium\browser_drivers\chromedriver\chromedriver.exe'

    # Create a new instance of the Chrome driver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    yield driver

    # After the test, quit the browser
    driver.quit()


def test_open_website(browser):
    # Navigate to a website
    browser.get("https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com")
    screenshot_directory = r"C:\Users\HP\Desktop\screenshots"

    # Wait for a few seconds (optional)
    browser.implicitly_wait(5)

    # Perform assertions
    assert "Log in - W3Schools" in browser.title

    username = browser.find_element("name", "email")
    passowrd = browser.find_element("id", "current-password")

    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# Capture a screenshot and save it with the current date and time in the filename

    screenshot_filename = os.path.join(screenshot_directory, f"screenshot_{current_time}.png")
    browser.save_screenshot(screenshot_filename)

    assert username.is_displayed() is True
    username.send_keys("shubham")
    passowrd.send_keys("admin")

# Run the test with the following command in your terminal:
# c pytest your_test_script.py
