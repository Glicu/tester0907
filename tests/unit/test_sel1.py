import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_basic_options_chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(2)
    driver.quit()


def test_basic_options_edge():
    driver = webdriver.Edge()
    driver.get("https://www.google.com")
    time.sleep(2)
    driver.quit()
