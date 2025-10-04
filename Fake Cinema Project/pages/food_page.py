from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Comida(BasePage):

    Palomitas = (By.XPATH, "//img[@alt='Palomitas']")
    Sandwich = (By.XPATH,"//h3[normalize-space()='Sandwich de Pollo']")
    Agua = (By.XPATH, "//img[@alt='Agua Embotellada']")

    def select_Palomitas(self):
        self.click(self.Palomitas)

    def select_sandwich(self):
        self.click(self.Sandwich)

    def select_agua(self):
        self.click(self.Agua)
