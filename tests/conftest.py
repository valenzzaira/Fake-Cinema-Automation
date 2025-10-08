import pytest
from selenium import webdriver
from pages.home_page import HomePage
import os


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    if os.getenv("CI"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)


    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def cinema_driver(driver):
    """Fixture que siempre va a la página del cinema"""
    driver.get("https://fake-cinema.vercel.app/")

    return driver




