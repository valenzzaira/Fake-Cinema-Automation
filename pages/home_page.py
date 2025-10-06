from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage




class HomePage(BasePage):

    FOOD_BUTTON = (By.XPATH, "//a[normalize-space()='Alimentos']")
    HOME_BUTTON = (By.XPATH, "//a[@href='/movies/fantastic-four']")
    URL = "https://fake-cinema.vercel.app/"

    def __init__(self, driver):
        super().__init__(driver)


    def open_home_page(self):
        self.visit(self.URL)


    def click_adquirir_entradas(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.HOME_BUTTON)
        ).click()

    def click_alimentos(self):
        self.click(self.FOOD_BUTTON)










