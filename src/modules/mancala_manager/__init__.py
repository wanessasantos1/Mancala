import os
from modules.mancala_board import MancalaBoard
from modules.interface_usuario import InterfaceUsuario
from modules.jogador import Jogador

class Mancala(InterfaceUsuario):
    qntdPecas = 36
    game = MancalaBoard()

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
        os.system('cls')

        if (self.game.jogo_status == 0):
            self.game.inicializar_jogo()
            self.game.salvar_jogo()

        while(self.game.jogo_status == 1):
            self.game.mostrar_tabuleiro()
            self.game.jogar()

        if(self.game.jogo_status == 5):
            self.game.salvar_jogo()

        if (self.game.jogo_status == 10):
            ganhador = self.game.finaliza_jogo()

            os.system('cls')
            print('O ganhador da partida foi {0} com {1} pontos'.format(ganhador[0], ganhador[1]))

        os.system('pause')

        return self
    
    def carregar_jogo(self):
        carregado_sucesso = self.game.carregar_jogo()

        if (carregado_sucesso): self.novo_jogo()
        pass