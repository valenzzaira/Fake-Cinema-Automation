import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.movie_page import SelectShowTime
from pages.booking_page import BoletosAsientos
from pages.cart_pages import Pago
from pages.checkout_page import Formulario
from test_data.customer_data import CustomerTestData


class TestCustomerData:

    def navigate_to_checkout(self, driver):

        home = HomePage(driver)
        movie = SelectShowTime(driver)
        boletos = BoletosAsientos(driver)
        payment = Pago(driver)


        home.open_home_page()
        home.click_adquirir_entradas()

        # Paso 2: Seleccionar día y función
        movie.select_day()
        movie.select_showtime()

        # Paso 3: Seleccionar asientos
        boletos.seleccionar_asientos()
        boletos.confirmar_compra()

        # Paso 4: Ingresar cantidad de boletos
        boletos.ingresar_boletos(adultos="2", niños="1")

        # Paso 5: Confirmar compra
        boletos.confirmar_boletos()

        # Paso 6: Pagar boletos
        payment.pago_de_entradas()

    @pytest.mark.parametrize("customer", CustomerTestData.VALID_CUSTOMERS)
    def test_valid_customer_data(self, driver, customer):
        """ clientes válidos """

        #  Navegar hasta checkout
        self.navigate_to_checkout(driver)
        form_page = Formulario(driver)

        # Llenar formulario con datos del cliente
        form_page.campo_nombre(customer["firstName"])
        form_page.campo_apellidos(customer["lastName"])
        form_page.campo_email(customer["email"])
        form_page.nombre_tarjeta(customer["cardName"])
        form_page.num_de_tarjeta(customer["cardNumber"])
        form_page.numero_cvv(customer["cvv"])


        form_page.click_confirmar_pago()


        # El formulario debería avanzar
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("/confirmation")
            )
        except TimeoutException:
            print("La URL no cambió a /confirmation en 10 segundos.")

        # Assert
        current_url = driver.current_url
        assert "/checkout" not in current_url, \
            f"Caso límite falló: {customer['test_case']}"
        assert "/confirmation" in current_url, \
            f"URL no es la esperada: {current_url}"

    @pytest.mark.parametrize("customer", CustomerTestData.BOUNDARY_CASES)
    def test_boundary_customer_data(self, driver, customer):
        """ casos límite """

        # Navegar hasta checkout
        self.navigate_to_checkout(driver)
        form_page = Formulario(driver)


        form_page.campo_nombre(customer["firstName"])
        form_page.campo_apellidos(customer["lastName"])
        form_page.campo_email(customer["email"])
        form_page.nombre_tarjeta(customer["cardName"])
        form_page.num_de_tarjeta(customer["cardNumber"])
        form_page.numero_cvv(customer["cvv"])

        form_page.click_confirmar_pago()

        # Los casos límite válidos deberían funcionar
        current_url = driver.current_url
        assert "/checkout" not in current_url or "/confirmation" in current_url, \
            f"Caso límite falló: {customer['test_case']}"

    @pytest.mark.parametrize("customer", CustomerTestData.INVALID_CUSTOMERS)
    def test_invalid_customer_data(self, driver, customer):


        # Navegar hasta checkout
        self.navigate_to_checkout(driver)
        form_page = Formulario(driver)

        # Llenar formulario con datos inválidos
        form_page.campo_nombre(customer["firstName"])
        form_page.campo_apellidos(customer["lastName"])
        form_page.campo_email(customer["email"])
        form_page.nombre_tarjeta(customer["cardName"])
        form_page.num_de_tarjeta(customer["cardNumber"])
        form_page.numero_cvv(customer["cvv"])

        form_page.click_confirmar_pago()

        #  El formulario NO debería avanzar
        current_url = driver.current_url

        # Debería quedarse en checkout o mostrar error
        assert "/checkout" in current_url or "error" in current_url.lower(), \
            f"El formulario avanzó incorrectamente para: {customer['expected_error']}"

    def test_empty_form_submission(self, driver):
        """ formulario completamente vacío"""

        #  Navegar hasta checkout
        self.navigate_to_checkout(driver)
        form_page = Formulario(driver)

        # Intentar enviar sin llenar nada
        form_page.click_confirmar_pago()

        #  No debería avanzar
        current_url = driver.current_url
        assert "/checkout" in current_url, \
            "El formulario vacío no debería procesarse"

    def test_partial_form_submission(self, driver):
        """ formulario parcialmente lleno"""


        self.navigate_to_checkout(driver)
        form_page = Formulario(driver)


        form_page.campo_nombre("Juan")
        form_page.campo_email("juan@test.com")


        form_page.click_confirmar_pago()


        current_url = driver.current_url
        assert "/checkout" in current_url, \
            "El formulario parcial no debería procesarse"

    @pytest.mark.smoke
    def test_typical_customer_flow(self, driver):
        """Prueba flujo típico de un cliente normal (smoke test)"""

        # Arrange - Navegar hasta checkout
        self.navigate_to_checkout(driver)

        # Cliente típico
        customer = {
            "firstName": "Ana",
            "lastName": "Martínez",
            "email": "ana.martinez@email.com",
            "cardName": "Ana Martínez",
            "cardNumber": "4111111111111111",
            "cvv": "123"
        }

        form_page = Formulario(driver)

        # Act - Flujo completo
        form_page.campo_nombre(customer["firstName"])
        form_page.campo_apellidos(customer["lastName"])
        form_page.campo_email(customer["email"])
        form_page.nombre_tarjeta(customer["cardName"])
        form_page.num_de_tarjeta(customer["cardNumber"])
        form_page.numero_cvv(customer["cvv"])

        form_page.click_confirmar_pago()

        # Assert - Debería completarse exitosamente


        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("/confirmation")
            )
        except TimeoutException:
            print("La URL no cambió a /confirmation en 10 segundos.")

        # Assert - Ahora el test puede verificar la URL con confianza
        current_url = driver.current_url
        assert "/checkout" not in current_url, \
            f"Caso límite falló: {customer['test_case']}"
        assert "/confirmation" in current_url, \
            f"URL no es la esperada: {current_url}"
