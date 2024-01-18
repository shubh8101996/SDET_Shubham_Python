import sys
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome"], scope="class")
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()  # Provide the correct path
    else:
        raise ValueError("Invalid browser specified in fixture")

    driver.get("https://www.google.co.in/")
    yield driver  # This is the value that will be returned to the test function

    # Teardown - Close the browser
    driver.quit()


@pytest.mark.run(order=1)
@pytest.mark.dependency
def test_title(browser):
    title = browser.title
    assert "Google" in title
    print("title checked  ")
    return title


@pytest.mark.run(order=2)
# @pytest.mark.dependency(depends=["test_title"])
@pytest.mark.parametrize("search, expected_output",
                         [("java", "java - Google Search"), ("api testing", "api testing - Google Search"),
                          ("database", "database - Google Search")])
def test_click_on_search_btn(browser, search, expected_output):
    # if test_title is not None:
    #     pytest.skip("Skipping test_click_on_search_btn because title is None")
    # Example: Assert that the title contains "WebDriverManager"
    # searchBtn = WebDriverWait(browser, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//textarea[@class='gLFyf']"))
    # )
    textinput = browser.find_element(By.XPATH, "//textarea[@class='gLFyf']")
    WebDriverWait(browser, 20).until(EC.visibility_of(textinput))
    textinput.send_keys(search)
    textinput.send_keys(Keys.ENTER)

    time.sleep(3)

    assert expected_output in browser.title

    # Click on the element
