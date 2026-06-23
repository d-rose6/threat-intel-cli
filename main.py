from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from functions.consultation import consultar_ip
from time import sleep


console = Console()

def menu():
    while True:

        #Limpar a tela para o menu ficar sempre no topo
        console.clear()


        console.print(Panel(f"[bold blue] CENTER OF THREAT INTEL [/bold blue]", expand=False ))
        print()

        console.print("[bold white][1][/bold white] -> Analisar IP Suspeito")
        console.print("[bold white][2][/bold white] -> Sair do Programa\n")

        #Aqui o usuário fará sua escolha. Não é necessario tratarmos o erro, o console em si faz o trabalho
        # caso o usuário tente digitar algo fora das opções
        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2"])


        if opcao == "1":

            console.clear()
            print()

            ip_usuario = input("Digite o IP para investigação: ").strip()

            if not ip_usuario:
                console.print("\n[bold red][!] Erro: Você não digitou nenhum IP.[/bold red]")
                input("\nPressione Enter para voltar ao menu...")
                continue

            console.print(f"\n[yellow]Buscando informações sobre o IP {ip_usuario}...[/yellow]")
            sleep(0.9)

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
            console.print("\n[bold red]Desconectando do sistema... Até logo![/bold red]")
            sleep(1.5)
            break

menu()


