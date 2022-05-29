from rich import print
from random import randint
from time import sleep

cash = 1000
print(f"[cyan]This is the simplest [bold yellow]dice game[/bold yellow].\nYou can bet and [bold green]win[/bold green] or [bold red]lose[/bold red].\nYou start with [yellow]${cash}[/yellow].\n[bold green]Good luck![/bold green]\n---------")
while True:
    while cash != 0 and cash > 0:
        while True:     
            print(f"[bold cyan]You have [yellow]${cash}[/yellow].")
            while True:
                try:
                    print("[bold green]Your bet?:", end=" ")
                    bet = int(input())

                except ValueError:
                    print("[bold red]Enter a number, please.\n")

                else:
                    break

            if bet > cash:
                print(f"[bold red]You have only [yellow]${cash}[/yellow]!\n")

            else:
                sleep(1)
                print(f"[bold green]OK, your bet is [yellow]${bet}[/yellow]...")
                break
                
        is_won = randint(1, 2)
        if is_won == 1:
            sleep(1)
            print(f"\n[bold green]Congratulations! You won [yellow]${bet}[/yellow]!\n")
            cash += bet
            sleep(1)

        else:
            sleep(1)
            print(f"\n[bold red]You lose [yellow]${bet}[/yellow]!\n")
            cash -= bet
            sleep(1)

    print("[bold red]You lost all your money.\nRestart game with [yellow]$1000[/yellow] ('y' or 'n')?:", end=" ")

    choice = input()
    if choice == 'y':
        print("[bold green]OK, restarting...")
        cash = 1000

    else:
        print("[bold red]Bye!")
        break
