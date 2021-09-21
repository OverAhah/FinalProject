from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "ru":
        print("\nstart ru browser for test..")
        browser = webdriver.Chrome()
    elif language == "en":
        print("\nstart en browser for test..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--language should be ru or en")
    yield browser
    print("\nquit browser..")
    browser.quit()