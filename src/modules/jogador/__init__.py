class Jogador:
    """
        Esta classe representa a funcionalidade do Jogador. 
    """
    __nome = ''
    __pontuacao = 0
    __vitorias = 0
    __derrotas = 0
    __empate = 0
    
    def __init__(self, nome, pontuacao = 0, vitorias = 0, derrotas = 0, empate = 0):
        """
            O construtor cria um novo jogador a partir das informações passadas:

            - Nome do jogador
            - Pontuação do jogador (DEFAULT: 0)
            - Quantidade de vitórias do jogador (DEFAULT: 0)
            - Quantidade de derrotas do jogador (DEFAULT: 0)
            - Quantidade de empates do jogador (DEFAULT: 0)
            
            (str, int?, int?, int?, int?) -> Jogador
        """
        self.__nome = nome
        self.__pontuacao = pontuacao
        self.__vitorias = vitorias
        self.__derrotas = derrotas
        self.__empate = empate

    def __str__(self):
        """
            Método de representação em String.
            
            (MancalaBoard) -> str
        """
        return None

    def get_nome(self):
        """
           Retorna o nome do jogador.

            (None) -> str
        """
        return self.__nome
    
    def get_pontuacao(self):
        """
            Retorna a pontuação do jogador.

            (None) -> int
        """
        return self.__pontuacao

    def get_vitorias(self):
        """
            Retorna a quantidade de vitórias do jogador.

            (None) -> int 
        """
        return self.__vitorias

    def get_derrotas(self):
        """
            Retorna a quantidade de derrotas do jogador.

            (None) -> int 
        """
        return self.__derrotas
    
    def get_empate(self):
        """
            Retorna a quantidade de empates do jogador.

            (None) -> int 
        """
        return self.__empate

    def get_manual():
        """
            Esta função estática (chamada sempre através de Tela.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__'] = Jogador.__init__.__doc__
        manual['__str__'] = Jogador.__str__.__doc__
        manual['get_nome'] = Jogador.get_nome.__doc__
        manual['get_pontuacao'] = Jogador.get_pontuacao.__doc__
        manual['get_vitorias'] = Jogador.get_vitorias.__doc__
        manual['get_derrotas'] = Jogador.get_derrotas.__doc__
        manual['get_empate'] = Jogador.get_empate.__doc__
        manual['__nome'] = '# Representa o nome do Jogador'
        manual['__pontuacao'] = '# Representa a pontuação do Jogador'
        manual['__vitorias'] = '# Representa a quantidade de vitórias do Jogador'
        manual['__derrotas'] = '# Representa a quantidade de derrotas do Jogador'
        manual['__empate'] = '# Representa a quantidade de empates do Jogador'
        return manual