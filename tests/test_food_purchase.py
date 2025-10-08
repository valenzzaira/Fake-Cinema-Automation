import pytest
from pages.home_page import HomePage
from pages.food_page import Comida
from pages.food_details import CompraComida
from pages.confirmation_page import Confirmacion
from pages.cart_pages import  Pago
from pages.checkout_page import Formulario



def test_flujo_completo(driver):
    home = HomePage(driver)
    comida = Comida(driver)
    detalle = CompraComida(driver)
    checkout = Confirmacion(driver)
    pago = Pago(driver)
    form = Formulario(driver)

    home.open_home_page()
    home.click_alimentos()

    # Paso 1. Escoger Palomitas
    comida.click(Comida.Palomitas)
    detalle.agregar_al_carrito()
    driver.back()

    # Paso 2. Escoger Sandwich
    comida.click(Comida.Sandwich)
    detalle.agregar_al_carrito()
    driver.back()

    # Paso 3. Escoger Agua
    comida.click(Comida.Agua)
    detalle.agregar_al_carrito()
    driver.back()

    # Paso 4. Hacer check out de carrito
    checkout.click_en_carrito()
    pago.pago_de_entradas()


    # Paso 5. Llenar formulario
    form.campo_nombre("Olivia")
    form.campo_apellidos("Cazares Valadez")
    form.campo_email("oliviacazar@gmail.com")
    form.nombre_tarjeta(" Olivia Cazares")
    form.num_de_tarjeta("2345 2112 5566")
    form.numero_cvv("465")
    form.click_confirmar_pago()

