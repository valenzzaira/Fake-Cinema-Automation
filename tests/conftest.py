import pytest
from selenium import webdriver
from pages.home_page import HomePage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def cinema_driver(driver):
    """Fixture que siempre va a la página del cinema"""
    driver.get("https://fake-cinema.vercel.app/")
    return driver


