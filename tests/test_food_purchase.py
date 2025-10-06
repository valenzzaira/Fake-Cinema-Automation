import pytest
from pages.home_page import HomePage
from pages.food_page import Comida
from pages.food_details import CompraComida



def test_flujo_completo(driver):
    home = HomePage(driver)
    comida = Comida(driver)
    detalle = CompraComida(driver)
    checkout =

    home.open_home_page()
    home.click_alimentos()

    # Palomitas
    comida.click(Comida.Palomitas)
    detalle.agregar_al_carrito()
    driver.back()

    # Sandwich
    comida.click(Comida.Sandwich)
    detalle.agregar_al_carrito()
    driver.back()

    # Agua
    comida.click(Comida.Agua)
    detalle.agregar_al_carrito()
    driver.back()

    # Check out de carrito

