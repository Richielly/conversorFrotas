import sys
from colorama import Fore, Style, init

class Messages:

    # Inicializa o colorama para habilitar a formatação de cores no terminal.
    init(autoreset=True)

    def mensagem_erro(self, mensagem):
        return (Fore.RED + "[ERRO] " + Style.RESET_ALL + mensagem)

    def mensagem_info(self, mensagem):
        return (Fore.BLUE + "[INFO] " + Style.RESET_ALL + mensagem)

    def mensagem_aviso(self, mensagem):
        return (Fore.YELLOW + "[AVISO] " + Style.RESET_ALL + mensagem)

    def mensagem_sucesso(self, mensagem):
        return (Fore.GREEN + "[SUCESSO] " + Style.RESET_ALL + mensagem)

