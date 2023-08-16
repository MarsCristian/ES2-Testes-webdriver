from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium import webdriver



def open_site():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8080/")
    return driver

def login(email,senha,driver):
    # Encontrar o botão de login usando o seletor CSS
    botao_login = driver.find_element("css selector", 'input[value="Login"]')
    # Clicar no botão de login
    botao_login.click()

    #inserir dados
    #Encontrar o campo de entrada do nome de usuário e inserir o valor
    campo_usuario = driver.find_element("css selector", 'input[name="username"]')
    campo_usuario.send_keys(email)

    # Encontrar o campo de entrada da senha e inserir o valor
    campo_senha = driver.find_element("css selector", 'input[name="password"]')
    campo_senha.send_keys(senha)

    # Encontrar o botão "Entrar" e clicar nele
    botao_entrar = driver.find_element("css selector", 'input[value="Entrar"]')
    botao_entrar.click()

def cadastrar_locadora(driver):
    link_cadastrar_locadora = driver.find_element("link text", "Cadastrar")
    link_cadastrar_locadora.click()