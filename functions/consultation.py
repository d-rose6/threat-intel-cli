import requests

def consultar_ip(ip):
    try:
        resposta = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        return resposta.json()  # Devolve o dicionário pronto
    except requests.exceptions.RequestException:
        return None  # Se der erro, devolve "Nada"