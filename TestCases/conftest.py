from selenium import webdriver
# import pytest
#
import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()  # Default to Chrome if no browser specified
    return driver

# Correcting the hook implementation to pytest_addoption

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# #### Generate HTML Report ####
# 
# it is a hook for adding environment info to HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if hasattr(config,'_metadata'):
        config._metadata['project Name'] = 'Nop Commerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Madhavi'

    @pytest.hookimpl(tryfirst=True)
    def pytest_metadata(metadata):
        metadata['Project Name'] = 'Nop Commerce'

# it is hook for delete/modify environment info to HTML report
# i want to delete 'JAVA HOME' asd 'Plugins' details from report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA HOME",None)
#     metadata.pop("Plugins",None)


import pytest
import logging

# log generation configuration
@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fh = logging.FileHandler("test.log")
    fh.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger


@pytest.fixture(scope="function")
def logger(configure_logging):
    return configure_logging
