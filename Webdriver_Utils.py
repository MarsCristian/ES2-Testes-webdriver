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

def preencher_locadora(driver):
    import Valid_Generator as vg

    link_cadastrar_locadora = driver.find_element("link text", "Cadastrar")
    link_cadastrar_locadora.click()
    resposta = []
    try:
        #gerar tuplas
        nome= vg.generate_valid_password()
        cidade= vg.generate_valid_password()
        telefone= vg.generate_valid_phone()
        cnpj= vg.generate_valid_cnpj()
        senha= vg.generate_valid_password()
        email= vg.generate_valid_email()

        entrada = [nome,cidade,telefone,cnpj,senha,email]
        
        print('input de teste: '+nome+'\n'+cidade+'\n'+telefone+'\n'+cnpj+'\n'+senha+'\n'+email)
        # Localizar os campos de entrada e preencher os dados
        try:
            campo_nome = driver.find_element("id", "nome")
            campo_nome.send_keys(nome)
        except:
            resposta.append('Falhou no campo Nome: '+ nome)

        try:
            campo_cidade = driver.find_element("id", "cidade")
            campo_cidade.send_keys(cidade)
        except:
            resposta.append('Falhou no campo Cidade: '+cidade)


        try:
            campo_cnpj = driver.find_element("id", "CNPJ")
            campo_cnpj.send_keys(cnpj)
        except:
            resposta.append('Falhou no campo CNPJ: '+cnpj)

        try:
            campo_senha = driver.find_element("id","senha")
            campo_senha.send_keys(senha)
        except:
            resposta.append('Falhou no campo Senha: '+senha)

        try:
            campo_email = driver.find_element("id","email")
            campo_email.send_keys(email)
        except:
            resposta.append('Falhou no campo Email '+email)

        try:
            campo_telefone = driver.find_element("id", "telefone")
            campo_telefone.send_keys(telefone)
        except:
            resposta.append('Falhou no campo Telefone: '+telefone)

    except:
        pass

    print(resposta)
    botao_salvar = driver.find_element("css selector", 'button[type="submit"]')
    botao_salvar.click()

    return entrada, resposta