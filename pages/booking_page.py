from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BoletosAsientos(BasePage):

    # Locators
    btn_8 = (By.XPATH, "//div/main/div/div[1]/div[3]/div[2]/div[3]/button[7]")
    btn_9 = (By.XPATH, "//div/main/div/div[1]/div[3]/div[2]/div[3]/button[8]")
    btn_10 = (By.XPATH, "//div/main/div/div[1]/div[3]/div[2]/div[3]/button[9]")
    btn_11 = (By.XPATH, "//div/main/div/div[1]/div/div[1]/div[3]/div[2]/div[3]/button[10]")

    boton_comprar = (By.XPATH, "//button[text()='Comprar boletos']")
    input_kids = (By.ID, "kids")
    input_adults = (By.ID, "adults")
    b_confirm = (By.XPATH, "//button[text()='Confirmar']")

    def __init__(self, driver):
        super().__init__(driver)
        self.asientos_disponibles = [self.btn_8, self.btn_9, self.btn_10]

    def seleccionar_asiento(self, locator: tuple[By, str]):
        if self.element_is_visible(locator):
            self.click(locator)

    def seleccionar_asientos(self):
        for asiento in self.asientos_disponibles:
            self.seleccionar_asiento(asiento)

    def confirmar_compra(self):
        if not self.element_is_visible(self.boton_comprar):
            self.scroll_to_element(self.boton_comprar)
        self.click(self.boton_comprar)

    def ingresar_boletos(self, adultos: str, niños: str):
        self.type(self.input_adults, adultos)
        self.type(self.input_kids, niños)

    def confirmar_boletos(self):
        self.scroll_to_element(self.b_confirm)
        self.click(self.b_confirm)





        











