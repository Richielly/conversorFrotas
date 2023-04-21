import sys
from colorama import Fore, Style, init

class Messages:

    # Inicializa o colorama para habilitar a formatação de cores no terminal.
    init(autoreset=True)

    def mensagem_erro(self, mensagem):
        print(Fore.RED + "[ERRO] " + Style.RESET_ALL + mensagem, file=sys.stderr)

    def mensagem_info(self, mensagem):
        print(Fore.BLUE + "[INFO] " + Style.RESET_ALL + mensagem)

    def mensagem_aviso(self, mensagem):
        print(Fore.YELLOW + "[AVISO] " + Style.RESET_ALL + mensagem)

    def mensagem_sucesso(self, mensagem):
        print(Fore.GREEN + "[SUCESSO] " + Style.RESET_ALL + mensagem)

