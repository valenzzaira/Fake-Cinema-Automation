from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from pages.movie_page import SelectShowTime
from pages.home_page import HomePage
from pages.booking_page import BoletosAsientos
import time

driver = webdriver.Chrome()
home = HomePage(driver)
home.open_home_page()
home.click_adquirir_entradas()

movie = SelectShowTime(driver)
movie.select_day()
movie.select_showtime()

boletos = BoletosAsientos(driver)
boletos.seleccionar_asientos()
boletos.ingresar_boletos(adultos="2", niños="1")
boletos.confirmar_compra()



input("Presiona Enter para cerrar el navegador...")