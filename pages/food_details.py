from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CompraComida(BasePage):

    AgregarBtn = (By.XPATH, "//button[contains(text(),'Agregar al carrito')]")

    def agregar_al_carrito(self):
        self.click(self.AgregarBtn)

    def click_pago_comida(self):
        self.click(self.food_payment_bttn)


