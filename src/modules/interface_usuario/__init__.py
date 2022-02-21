import os
os.system("color")

class InterfaceUsuario:
    """
        Esta super classe inclui todos os métodos e atributos que são úteis para qualquer
        interface que pode ser feita com o usuário.
        
        Em partes adaptado de https://www.codegrepper.com/code-examples/python/python+ansi+colors
        Acesso em 02/01/2022
    """
    
    def __init__(self):
        """
            Inicializador da classe. Inicializa um dicionário que associa os indices de 0 a
            255 (inclusive) a todos os primeiros 256 caracteres que o cmd do windows reconhece.
            Também seta os atributos das cores ANSI. Eles são úteis para escrever caracteres 
            coloridos.

            Adaptado de https://www.codegrepper.com/code-examples/python/python+ansi+colors
            Acesso em 02/01/2022
        """
        self.tabelaCaracteres = {x : chr(x) for x in range(256)}
        self.pref = "\033["
        self.reset = f"{self.pref}0m"
        self.black = "30m"
        self.red = "31m"
        self.green = "32m"
        self.yellow = "33m"
        self.blue = "34m"
        self.magenta = "35m"
        self.cyan = "36m"
        self.white = "37m"
        
    def strANSI(self, text, color=None, is_bold=False):
        """
            Retorna a string 'text' na cor setada por 'color' e 'is_bold'.
        """
        if color == None or color.upper() == "WHITE": color = self.white
        elif color.upper() == "BLACK": color = self.black
        elif color.upper() == "RED": color = self.red
        elif color.upper() == "GREEN": color = self.green
        elif color.upper() == "YELLOW": color = self.yellow
        elif color.upper() == "BLUE": color = self.blue
        elif color.upper() == "MAGENTA": color = self.magenta
        elif color.upper() == "CYAN": color = self.cyan
        else: color == self.white
        return f'{self.pref}{1 if is_bold else 0};{color}' + text + self.reset
        
    def print(self, text, color=None, is_bold=False):
        """
            Printa na tela a string 'text' na cor setada por 'color' e 'is_bold'.
        """
        if color == None or color.upper() == "WHITE": color = self.white
        elif color.upper() == "BLACK": color = self.black
        elif color.upper() == "RED": color = self.red
        elif color.upper() == "GREEN": color = self.green
        elif color.upper() == "YELLOW": color = self.yellow
        elif color.upper() == "BLUE": color = self.blue
        elif color.upper() == "MAGENTA": color = self.magenta
        elif color.upper() == "CYAN": color = self.cyan
        else: color == self.white
        print(f'{self.pref}{1 if is_bold else 0};{color}' + text + self.reset)
        
    def printCaracteres(self):
        """
            Printa na tela o conteúdo do dicionario 'tabelaCaracteres', um item
            por linha.
        """
        for char in self.tabelaCaracteres.values():
            print(char)

    def render_menu_principal(self):
        """
            Printa na tela o menu principal.
        """
        os.system('cls')
        print("0. Sair")
        print("1. Novo Jogo")
        print("2. Carregar Jogo")
        print("3. Configurações")
        print("4. Ajuda")
        print("5. Sobre")
        print("6. Manual do Desenvolvedor")
        print("7. Estatística")
