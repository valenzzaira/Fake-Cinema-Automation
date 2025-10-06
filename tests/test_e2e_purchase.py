import pytest
from pages.home_page import HomePage
from pages.movie_page import SelectShowTime
from pages.booking_page import BoletosAsientos
from pages.cart_pages import Pago
from pages.checkout_page import Formulario
from pages.confirmation_page import Confirmacion


@pytest.mark.e2e
def test_user_open_home(driver):
    # Paso 1: Abrir home y navegar a selección de película
    home = HomePage(driver)
    movie = SelectShowTime(driver)
    boletos = BoletosAsientos(driver)
    payment = Pago(driver)
    form = Formulario(driver)
    confirm = Confirmacion(driver)


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

    # Paso 7:  Llenar formulario
    form.campo_nombre("Zaira Elizabeth")
    form.campo_apellidos("Valenzuela Martinez")
    form.campo_email("lazai@gmail.com")
    form.nombre_tarjeta(" Zaira Elizabeth Valenzuela Martinez")
    form.num_de_tarjeta("2345 2112 5566")
    form.numero_cvv("465")
    form.click_confirmar_pago()

    # Paso 8: Confirmar el pago total de la cuenta
    confirm.confirmacion_de_pedido()






