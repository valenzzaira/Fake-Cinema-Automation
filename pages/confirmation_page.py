from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Confirmacion(BasePage):

    #Selector para confirmar
    car_button_check = (By.XPATH, "//a[normalize-space()='Carrito']")
    confirmation_button = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/a[1]/button[1]")


    def __init__(self, driver):
        super().__init__(driver)

    def confirmacion_de_pedido(self):
        if self.element_is_visible(self.confirmation_button):
            self.click(self.confirmation_button)

    def click_en_carrito(self):
        self.click(self.car_button_check)

