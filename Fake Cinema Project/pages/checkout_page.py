from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Formulario(BasePage):
    """Selectores Formulario de nombre y datos de tarjeta"""

    nombre_input = (By.ID, "firstName")
    apellido_input = (By.ID, "lastName")
    email_input = (By.ID, "email")
    tarjeta_nombre = (By.ID, "cardName")
    numero_de_tarjeta = (By.ID, "cardNumber")
    cvv = (By.ID, "cvv")
    confirm_payment = (By.XPATH, "/html[1]/body[1]/div[1]/main[1]/form[1]/button[1]")


    """Inicializar drivers"""


    def __init__(self, driver):
        super().__init__(driver)

    def campo_nombre(self, nombre: str):
        self.type(self.nombre_input, nombre)

    def campo_apellidos(self, apellidos: str):
        self.type(self.apellido_input, apellidos)

    def campo_email(self, email : str):
        self.type(self.email_input, email)

    def nombre_tarjeta(self, name: str):
        self.type(self.tarjeta_nombre, name)

    def num_de_tarjeta(self, number: str):
        self.type(self.numero_de_tarjeta, number)

    def numero_cvv(self, cv: str):
        self.type(self.cvv, cv)

    def scroll_confirmar_pago(self):
        self.scroll_to_element(self.confirm_payment)

    def click_confirmar_pago(self):
        self.scroll_confirmar_pago()
        self.click(self.confirm_payment)


