import socket

def escanear_porta(ip, porta):
    # Cria um objeto de socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define um tempo limite de 1.0 segundo para não travar o programa esperando
    s.settimeout(1.0)

    # Tenta conectar. O connect_ex retorna 0 se a conexão deu certo
    resultado = s.connect_ex((ip, porta))
    s.close()

    return resultado == 0

def iniciar_scan(ip):
    # Portas clássicas que geralmente são monitoradas
    portas_comuns = {
        21: "FTP (Transferência de Arquivos)",
        22: "SSH (Acesso Remoto Seguro)",
        23: "Telnet (Inseguro)",
        25: "SMTP (Envio de E-mail)",
        80: "HTTP (Web Não Segura)",
        110: "POP3 (Recebimento de E-mail)",
        443: "HTTPS (Web Segura)",
        3389: "RDP (Área de Trabalho Remota)",
        8080: "HTTP-Proxy / Tomcat"
    }

    resultados_scan = {}

    for porta, servico in portas_comuns.items():
        aberta = escanear_porta(ip, porta)

        if aberta == True:
            status_final = "Aberta"
        else:
            status_final = "Fechada"

        resultados_scan[porta] = {
            "servico": servico,
            "status": status_final
        }


    return resultados_scan
