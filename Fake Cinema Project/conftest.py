import pytest
from utils.driver_factory import create_driver}
from time import sleep

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        help="Ejecutar pruebas en modo headless"
    )


@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")
    driver = create_driver(headless=headless)
    yield driver
    sleep(3)
    driver.quit()


@pytest.fixture
def cinema_driver(driver):
    driver.get("https://fake-cinema.vercel.app/")
    return driver