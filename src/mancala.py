import sys
sys.path.insert(0,"..")

from modules.interface_usuario import InterfaceUsuario
from modules.mancala_board import MancalaBoard
from modules.jogador import Jogador

__author__ = 'Wanessa Pinto dos Santos'
__copyright__ = 'Copyright 2022'
__credits__ = __author__
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = __author__
__email__ = 'wanessa.santos@poli.ufrj.br'
__status__ = 'Production'

class Mancala(InterfaceUsuario):
    qntdPecas = 36

    def __init__(self, qntdPecas=36):
        """
            O construtor cria um novo jogo a partir das configurações passadas:
            
            - Quantidade de peças (padrão 36)
            
            Representação: Uma representação com caracteres especiais no tabuleiro com a quantidade de peças dentro da cava
        """

        pass

    def __str__(self):
        """
            Este método, usado para representação em string, é a base da ETAPA 4.4. Aqui será
            retornada a String que contém as descrições de todos os métodos e atributos das 
            classes.
        """
        saida = ""
        manuais = []

        manuais.append(["MANUAL DA CLASSE BOARD", MancalaBoard.get_manual()],)
        manuais.append(["MANUAL DA CLASSE JOGADOR", Jogador.get_manual()])

        for manual in manuais:
            saida += manual[0] + "\n"
            for chave in manual[1]:
                saida += f'{chave} : {manual[1].get(chave)}\n'
            saida +='\n'
        
        return saida

print(Mancala())