import os, re
from pyexpat.errors import messages
from matplotlib import pyplot
from time import sleep

from modules.errors.player_not_found import PlayerNotFoundError


class Jogador:
    """
        Esta classe representa a funcionalidade do Jogador. 
    """
    __nome = ''
    __pontuacao = [0]
    __vitorias = [0]
    __derrotas = [0]
    __empate = [0]
    
    def __init__(self):
        """
            O construtor cria um novo jogador a partir das informações passadas:

            - Nome do jogador (DEFAULT: '')
            - Pontuação do jogador (DEFAULT: 0)
            - Quantidade de vitórias do jogador (DEFAULT: 0)
            - Quantidade de derrotas do jogador (DEFAULT: 0)
            - Quantidade de empates do jogador (DEFAULT: 0)
            
            (MancalaBoard) -> Jogador
        """

        self.set_nome('')
        self.set_pontuacao([0])
        self.set_vitorias([0])
        self.set_derrotas([0])
        self.set_empate([0])

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

    def set_nome(self, nome):
        """
            Esta função recebe o nome do jogador.

            (str) -> Jogador
        """
        self.__nome = nome

        return self
    
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

    def set_pontuacao(self, pontuacao):
        """
            Esta função recebe a pontuação do jogador.

            (int) -> Jogador
        """
        self.__pontuacao = pontuacao

        return self
    
    def set_vitorias(self, vitorias):
        """
            Esta função recebe a quantidade de vitórias do jogador.

            (int) -> Jogador
        """
        self.__vitorias = vitorias

        return self
    
    def set_derrotas(self, derrotas):
        """
            Esta função recebe a quantidade de derrotas do jogador.

            (int) -> Jogador
        """
        
        self.__derrotas = derrotas

        return self
    
    def set_empate(self, empate):
        """
            Esta função recebe a quantidade de empates do jogador.

            (int) -> Jogador
        """
        self.__empate = empate

        return self
    
    def nova_vitoria(self):
        """
            Esta função atualiza a quantidade de vitórias do jogador.

            (None) -> Jogador
        """
        self.__vitorias.append(self.__vitorias[-1] + 1)

        return self
    
    def nova_derrota(self):
        """
            Esta função atualiza a quantidade de derrotas do jogador.

            (None) -> Jogador
        """

        print(self.__derrotas[-1])
        self.__derrotas.append(self.__derrotas[-1] + 1)

        return self

    def novo_empate(self):
        """
            Esta função atualiza a quantidade de empates do jogador.

            (None) -> Jogador
        """
        self.__empate.append(self.__empate[-1] + 1)

        return self

    def nova_pontuacao(self, pontuacao):
        """
            Esta função atualiza a pontuação do jogador.

            (int) -> Jogador
        """
        self.__pontuacao.append(pontuacao)

        return self

    def salvar(self):
        """
            Esta função salva os dados do jogador.

            (None) -> Jogador
        """

        messages = [
            'vitorias: {}\n'.format(self.__vitorias),
            'derrotas: {}\n'.format(self.__derrotas),
            'empates: {}\n'.format(self.__empate),
            'pontuacao: {}\n'.format(self.__pontuacao)
        ]

        jogador_file = open("jogador/{}.txt".format(self.get_nome()), "w")

        with jogador_file as file:
            for message in messages:
                file.write(message)

        jogador_file.close()

        return self

    def string_to_list(self, string):
        """
            Esta função converte uma string em uma lista.

            (str) -> list
        """

        finalListInt = []
        newString = string.split(': ')[1].replace('\n', '')

        listString = re.sub('[\[\]]', '', newString)

        for i in listString.split(','):
            finalListInt.append(int(i))

        return finalListInt

    def carregar(self):
        """
            Esta função carrega os dados do jogador.

            (None) -> Jogador
        """

        try:
            save_file = open("jogador/{}.txt".format(self.get_nome()), "r")

            for line in save_file:
                if (line.startswith('vitorias: ')):
                    self.set_vitorias(self.string_to_list(line))
                elif (line.startswith('derrotas: ')):
                    self.set_derrotas(self.string_to_list(line))
                elif (line.startswith('empates: ')):
                    self.set_empate(self.string_to_list(line))
                elif (line.startswith('pontuacao: ')):
                    self.set_pontuacao(self.string_to_list(line))

            save_file.close()

            return True
        except:
            print('Não foi possível localizar o jogador {}!'.format(self.get_nome()))
            sleep(1)
            return False

    def mostrar_estatistica(self):
        Vitórias = self.get_vitorias()
        Derrotas = self.get_derrotas()
        Pontuacao = self.get_pontuacao()

        fig, ax = pyplot.subplots()
        ax.plot(Vitórias,'y-',linewidth=2,label= 'Vitórias')
        ax.plot(Derrotas,'r-',linewidth=2,label= 'Derrotas')
        ax.plot(Pontuacao,'g-',linewidth=2,label= 'Pontuação')
        ax.legend(loc= 'upper left')
        

        pyplot.show()

        return self

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