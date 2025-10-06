from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Pago(BasePage):
    b_pago = (By.XPATH,"//button[text()='Proceder al pago']")

    def __init__(self, driver):
        super().__init__(driver)

    def pago_de_entradas(self):
        if self.element_is_visible(self.b_pago):
            self.click(self.b_pago)


