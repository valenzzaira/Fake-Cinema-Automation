from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


DEFAULT_WINDOW_SIZE = "1920,1088"
BASE_URL = "https://fake-cinema.vercel.app/"


def create_driver(headless: bool = False, maximized: bool = False):

    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")

    if maximized:
        options.add_argument("--start-maximized")
    else:
        options.add_argument(f"--window-size={DEFAULT_WINDOW_SIZE}")

    options.add_argument("--incognito")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options,
    )

    driver.implicitly_wait(5)
    return driver

