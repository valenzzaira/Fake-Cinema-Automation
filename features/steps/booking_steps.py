from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



@given('el usuario se encuentra en la pagina base')
def step_def(context):
    #context.driver = webdriver.Chrome()
    context.driver.get("https://fake-cinema.vercel.app/" )



@when('el usuario selecciona una pelicula')
def step_def(context):
    context.
    print("Paso 2")

@then('el usuario puede ver los horarios disponibles')
def step_def(context):
    print("Paso 3")


