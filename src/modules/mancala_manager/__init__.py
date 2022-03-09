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
        """
            Inicia um novo jogo
        """

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

    def jogo_ajuda(self):
        os.system('cls')
        print('''
            O Mancala é um jogo de tabuleiro de raciocínio lógico-matemático que tem como objetivo colher o maior número de sementes. O tabuleiro do mancala conta com 14 espaços ou orifícios dispostos seis em cada lado e um em cada extremo do tabuleiro. Só é permitido apenas dois jogadores. O jogo começa por turnos, o primeiro jogador pega as quatro sementes de uma das seis cavidades e “semeia” de uma em uma a começar pela casinha seguinte à sua direita. O movimento se faz em sentido anti-horário, sendo conhecido como movimento de semeadura. Se, ao mover as peças, termina em seu armazém, joga de novamente. Do contrário, termina seu turno, dando vez ao outro jogador. O jogo termina quando um jogador não tem mais sementes para semear. Neste caso, o outro jogador tem direito de capturar as sementes. O jogador que tiver capturado mais sementes é o ganhador.
            
            Regras: 
            -Se você passa pelo armazém do seu adversário, durante a semeadura, não tem que colocar peças nela. Você só pode colocar sementes no seu próprio armazém. 
            -Se a última peça da semeadura ocupa uma cavidade vazia do seu lado do tabuleiro, você pode capturar todas as sementes da cavidade oposta e a sua própria. Todas essas sementes capturadas são colocadas diretamente em seu armazém.
        ''')

        os.system('pause')

        return self

    def manual_projeto(self):
        os.system('cls')
        print(self.__str__())

        os.system('pause')

        return self

    def estatistica(self):
        '''
            Estatísticas de um jogador
        '''

        os.system('cls')

        print('Insira o nome do jogador para ver a estatística: ')

        jogadorNome = input()

        jogador = Jogador()

        jogador.set_nome(jogadorNome)
        exist = jogador.carregar()

        if (exist):
            jogador.mostrar_estatistica()

        os.system('pause')

        return self