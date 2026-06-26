from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from functions.consultation import consultar_ip
from functions.port_scanner import iniciar_scan
from time import sleep


console = Console()

def menu():
    while True:

        #Limpar a tela para o menu ficar sempre no topo
        console.clear()


        console.print(Panel(f"[bold blue] CENTER OF THREAT INTEL [/bold blue]", expand=False ))
        print()

        console.print("[bold white][1][/bold white] -> Reconhecimento OSINT")
        console.print("[bold white][2][/bold white] -> Varredura de Portas")
        console.print("[bold white][3][/bold white] -> Sair do Programa\n")

        #Aqui o usuário fará sua escolha. Não é necessario tratarmos o erro, o console em si faz o trabalho
        # caso o usuário tente digitar algo fora das opções
        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3"])


        if opcao == "1":

            console.clear()
            print()

            ip_usuario = input("Digite o IP para investigação: ").strip()

            if not ip_usuario:
                console.print("\n[bold red][!] Erro: Você não digitou nenhum IP.[/bold red]")
                input("\nPressione Enter para voltar ao menu...")
                continue

            console.print(f"\n[yellow]Buscando informações sobre o IP {ip_usuario}...[/yellow]")
            

            dados = consultar_ip(ip_usuario)

            if dados is None:
                print()
                console.print("[bold red][!] Erro de rede:[/bold red] Não foi possível alcançar o servidor.")
            elif dados.get("status") == "fail":
                print()
                console.print("[bold red][!] Erro:[/bold red] O IP digitado é inválido ou privado.")
            else:
                print()
                console.print(f"[green]Dados obtidos para o IP: {ip_usuario}[/green]")

                tabela = Table(show_header=True, header_style="bold blue",title=f"[bold blue] RESULTADO DA INVESTIGAÇÃO [/bold blue]")

                tabela.add_column("Campo", justify="center", style="cyan")
                tabela.add_column("Informação", justify="center",style="green")

                tabela.add_row("IP Investigado", ip_usuario)
                tabela.add_row("País", dados.get("country"))
                tabela.add_row("Cidade", dados.get("city"))
                tabela.add_row("Provedor (ISP)", dados.get("isp"))

                console.print(tabela)


            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "2":
            console.clear()
            print()

            ip_usuario = input("Digite o IP/Domínio para o Port Scan: ").strip()

            if not ip_usuario:
                console.print("\n[bold red][!] Erro: O alvo não pode ficar em branco.[/bold red]")
                input("\nPressione Enter para voltar ao menu...")
                continue

            console.print(f"\n[yellow] Iniciando Varredura TCP no alvo {ip_usuario}...[/yellow]")

            # Roda a nossa função de scan
            resultado_portas = iniciar_scan(ip_usuario)

            # Criando a tabela para exibir as portas
            tabela_scan = Table(show_header=True, header_style="bold yellow",
                                title=f"[bold yellow] MAPA DE PORTAS DO ALVO [/bold yellow]")
            tabela_scan.add_column("Porta", justify="center", style="cyan")
            tabela_scan.add_column("Serviço Padrão", justify="left", style="white")
            tabela_scan.add_column("Status", justify="center")

            for porta, info in resultado_portas.items():
                status_texto = info["status"]

                if status_texto == "Aberta":
                    status_formatado = f"[bold green] {status_texto}[/bold green]"

                else:
                    status_formatado = f"[red] {status_texto}[/red]"

                tabela_scan.add_row(str(porta), info["servico"], status_formatado)

            console.print(tabela_scan)
            input("\nPressione Enter para voltar ao menu...")



        elif opcao == "3":
            console.clear()
            console.print("\n[bold red]Desconectando do sistema... Até logo![/bold red]")
            sleep(1.5)
            break

menu()


