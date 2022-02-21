import os
from modules.mancala_board import MancalaBoard
from modules.interface_usuario import InterfaceUsuario
from modules.jogador import Jogador

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

    def novo_jogo(self):
        game = MancalaBoard()

        os.system('cls')
        game.inicializar_jogo()

        while(game.jogo_iniciado == 1):
            game.mostrar_tabuleiro()
            game.jogar()

        if (game.jogo_status == 10):
            game.finaliza_jogo()

        os.system('pause')
