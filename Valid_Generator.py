import random
import string
import datetime


def generate_valid_password(length=12):
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    all_characters = lower_letters + upper_letters + digits + symbols
    
    # Garante pelo menos um de cada tipo
    password = [random.choice(lower_letters), random.choice(upper_letters), random.choice(digits), random.choice(symbols)]
    
    # Preenche o restante da senha com caracteres aleatórios
    for _ in range(length - 4):
        password.append(random.choice(all_characters))
    
    # Embaralha a senha para que a ordem não seja previsível
    random.shuffle(password)
    
    return ''.join(password)

def generate_valid_date():
    start_date = datetime.date(1900, 1, 1)
    end_date = datetime.date.today()
    
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    
    random_date = start_date + datetime.timedelta(days=random_days)
    
    return random_date.strftime("%d/%m/%Y")

def generate_valid_cpf():
    base = [random.randint(0, 9) for _ in range(9)]

    # Cálculo do primeiro dígito verificador
    soma = 0
    for i, num in enumerate(base, start=1):
        soma += num * (10 - i)
    primeiro_digito = 11 - (soma % 11)
    primeiro_digito = primeiro_digito if primeiro_digito < 10 else 0

    # Adicionar o primeiro dígito verificador à lista
    base.append(primeiro_digito)

    # Cálculo do segundo dígito verificador
    soma = 0
    for i, num in enumerate(base, start=1):
        soma += num * (11 - i)
    segundo_digito = 11 - (soma % 11)
    segundo_digito = segundo_digito if segundo_digito < 10 else 0

    # Adicionar o segundo dígito verificador à lista
    base.append(segundo_digito)

    # Formatar o CPF
    cpf_formatado = f"{base[0]}{base[1]}{base[2]}.{base[3]}{base[4]}{base[5]}.{base[6]}{base[7]}{base[8]}-{base[9]}{base[10]}"

    return cpf_formatado

def generate_valid_email():
    username_length = random.randint(5, 10)
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))

    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com", "example.com", "mail.com"])
    
    email = f"{username}@{domain}"
    return email

def generate_valid_cnpj():
    # Gere os primeiros 12 dígitos aleatoriamente
    base = [random.randint(0, 9) for _ in range(12)]

    # Calcule o primeiro dígito verificador
    total = 0
    for i, num in enumerate(base):
        total += num * (i % 8 + 2)
    primeiro_digito = (total % 11) if (total % 11) < 2 else 11 - (total % 11)

    # Adicione o primeiro dígito verificador
    base.append(primeiro_digito)

    # Calcule o segundo dígito verificador
    total = 0
    for i, num in enumerate(base):
        total += num * (i % 8 + 2)
    segundo_digito = (total % 11) if (total % 11) < 2 else 11 - (total % 11)

    # Adicione o segundo dígito verificador
    base.append(segundo_digito)

    # Converta os números em uma string e insira os separadores
    cnpj_formatado = f"{base[0]}{base[1]}.{base[2]}{base[3]}{base[4]}.{base[5]}{base[6]}{base[7]}/{base[8]}{base[9]}{base[10]}{base[11]}-{base[12]}{base[13]}"

    return cnpj_formatado

def generate_valid_phone():
    # Gere os primeiros dígitos (DDD) aleatoriamente
    ddd = random.choice(["11", "21", "31", "41", "51", "61", "71", "81", "91"])

    # Gere os próximos 8 dígitos aleatoriamente
    numeros = [random.randint(0, 9) for _ in range(9)]

    # Converta os números em uma string e insira os separadores
    numero_formatado = f"({ddd}){''.join(map(str, numeros[:4]))}-{''.join(map(str, numeros[4:]))}"

    return numero_formatado