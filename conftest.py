import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
Work with terminal
"""
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose language: ru or es or other")

"""
Fixture
"""
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    """
    Work with browser header language
    """
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)

    yield browser

    print("\nquit browser..")
    browser.quit()