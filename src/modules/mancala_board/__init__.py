import os


class MancalaBoard:
    """
        Esta super classe inclui todos os métodos e atributos que são úteis para a montagem e gerenciamento do jogo principal.
        Faz a montagem inicial de cada player;
        Faz a montagem inicial de cada tipo de quantidade de peça do jogo;

        Inicia vazio o board de cada linha que irá representar o tabuleiro.
    """

    nome_jogador_1 = 'Jogador 1'
    nome_jogador_2 = 'Jogador 2'
    __turno_jogador_1 = True

    jogo_status = 0

    __player_board = [
        [4, 4, 4, 4, 4, 4, 0],
        [4, 4, 4, 4, 4, 4, 0]
    ]

    __pecas_jogo = ['⠀', '⠂', '⠃', '⠇', '⠏', '⠟', '⠿', '⡿', '⣿']

    __board_linha_00 = ''
    __board_linha_01 = ''
    __board_linha_02 = ''
    __board_linha_03 = ''
    __board_linha_04 = ''
    __board_linha_05 = ''
    __board_linha_06 = ''
    __board_linha_07 = ''
    __board_linha_08 = ''
    __board_linha_09 = ''
    __board_linha_10 = ''

    def __str__(self):
        """
            Método de representação em String.
            
            (MancalaBoard) -> str
        """
        return None

    def inicializar_jogo(self):
        print('Insira o nome do jogador 1:')
        self.nome_jogador_1 = input()
        print('Insira o nome do jogador 2:')
        self.nome_jogador_2 = input()

        self.jogo_status = 1

        return self

    def comecar_jogo(self):


        return self

    def __calcular_pontuacao_cava__(self, tamanho, player, local):
        """
            Função privada que recebe o tamanho total de slots que cada casa possui para preencher o tabuleiro;
            Recebe player para gerenciar a casa de jogo e o local representa o index da cava, ou seja, qual cava vai selecionar.
            Retorna um array de numero com a pontuação local (cava)

            (int, int, int) -> [[str]]
        """
        cava_pontuacao = []

        for x in range(0, tamanho, 1):
            cava_pontuacao.append(['', ''])

        pontuacao = self.__player_board[player][local]

        for (x, cava_linha) in enumerate(cava_pontuacao):
            for y in range(0, len(cava_linha)):
                if (pontuacao >= 8):
                    cava_pontuacao[x][y] = self.__pecas_jogo[8]
                    pontuacao -= 8

                elif (pontuacao < 8):
                    cava_pontuacao[x][y] = self.__pecas_jogo[pontuacao]

                    pontuacao -= pontuacao

        return cava_pontuacao

    def __montar_cava_pontuacao__(self, player):
        """
            Função privada que recebe o player para a montagem com a pontuação da cava.
            Retorna a propria classe e salva na linha representante a montagem do tabuleiro com a pontuação.

            (int) -> MancalaBoard
        """
        cava_pontuacao = self.__calcular_pontuacao_cava__(9, player, -1)

        self.__board_linha_00 += ('⎾ ⎺ ⎺ ⏋ \t')
        self.__board_linha_01 += ('| {0} {1} | \t'.format(cava_pontuacao[0][0], cava_pontuacao[0][1]))
        self.__board_linha_02 += ('| {0} {1} | \t'.format(cava_pontuacao[1][0], cava_pontuacao[1][1]))
        self.__board_linha_03 += ('| {0} {1} | \t'.format(cava_pontuacao[2][0], cava_pontuacao[2][1]))
        self.__board_linha_04 += ('| {0} {1} | \t'.format(cava_pontuacao[3][0], cava_pontuacao[3][1]))
        self.__board_linha_05 += ('| {0} {1} | \t'.format(cava_pontuacao[4][0], cava_pontuacao[4][1]))
        self.__board_linha_06 += ('| {0} {1} | \t'.format(cava_pontuacao[5][0], cava_pontuacao[5][1]))
        self.__board_linha_07 += ('| {0} {1} | \t'.format(cava_pontuacao[6][0], cava_pontuacao[6][1]))
        self.__board_linha_08 += ('| {0} {1} | \t'.format(cava_pontuacao[7][0], cava_pontuacao[7][1]))
        self.__board_linha_09 += ('| {0} {1} | \t'.format(cava_pontuacao[8][0], cava_pontuacao[8][1]))
        self.__board_linha_10 += ('⎿ ⎽ ⎽ ⏌ \t')

        return self

    def __montar_cavas__(self, player, cava):
        """
            Função privada que recebe o player para a contagem da pontuação da cava.
            Retorna a propria classe e salva na linha representante a montagem do tabuleiro com a pontuação.

            (int, int) -> MancalaBoard
        """
        cava_pontuacao = self.__calcular_pontuacao_cava__(3, player, cava)
        
        if (player == 0):
            self.__board_linha_00 += ('⎾ ⎺ {0} ⏋ \t'.format(cava if self.__turno_jogador_1 else '⎺'))
            self.__board_linha_01 += ('| {0} {1} | \t'.format(cava_pontuacao[0][0], cava_pontuacao[0][1]))
            self.__board_linha_02 += ('| {0} {1} | \t'.format(cava_pontuacao[1][0], cava_pontuacao[1][1]))
            self.__board_linha_03 += ('| {0} {1} | \t'.format(cava_pontuacao[2][0], cava_pontuacao[2][1]))
            self.__board_linha_04 += ('⎿ ⎽ ⎽ ⏌ \t')
            self.__board_linha_05 += ('        \t')

        if (player == 1):
            self.__board_linha_06 += ('⎾ ⎺ {0} ⏋ \t'.format(cava if not self.__turno_jogador_1 else '⎺'))
            self.__board_linha_07 += ('| {0} {1} | \t'.format(cava_pontuacao[0][0], cava_pontuacao[0][1]))
            self.__board_linha_08 += ('| {0} {1} | \t'.format(cava_pontuacao[1][0], cava_pontuacao[1][1]))
            self.__board_linha_09 += ('| {0} {1} | \t'.format(cava_pontuacao[2][0], cava_pontuacao[2][1]))
            self.__board_linha_10 += ('⎿ ⎽ ⎽ ⏌ \t')

        return self

    def __verifica_cava_vazia__(self, cava, player_board):
        """
            Função privada que verifica se a cava está vazia.
            Retorna True se a cava estiver vazia, False se não estiver.

            (int, int) -> MancalaBoard
        """

        if (self.__player_board[player_board][cava] == 1):
            if (player_board == 0):
                pontuacao_cava_oposta = self.__player_board[1][cava]

                self.__player_board[0][6] += pontuacao_cava_oposta
                self.__player_board[1][cava] = 0

            if (player_board == 1):
                pontuacao_cava_oposta = self.__player_board[0][cava]

                self.__player_board[1][6] += pontuacao_cava_oposta
                self.__player_board[0][cava] = 0
        

        return self

    def __verifica_termino_jogo__(self):
        """
            Função privada que verifica se o jogo terminou.
            
            (void) -> MancalaBoard
        """

        soma1 = 0
        soma2 = 0

        for valor in self.__player_board[0][0:5]: soma1 += valor
        for valor in self.__player_board[1][0:5]: soma2 += valor

        if (soma1 == 0 or soma2 == 0):
            self.jogo_status = 10

        return self

    def __movimentar_peca__(self, cava):
        """
            Função que recebe o player para a movimentação da cava selecionada.
            Retorna a propria classe e faz o gerenciamento de movimentação de pedrinha em cada cava.

            (int, int) -> MancalaBoard
        """

        print("NUM CAVA: {0}".format(cava))
        if ((cava < 0) or (cava > 5)):
            print('Cava inválida!')
            os.system('pause')
            return self

        direcao = -1 if self.__turno_jogador_1 else 1
        is_player_board = 0 if self.__turno_jogador_1 else 1
        
        cava_qntd_pecas = self.__player_board[is_player_board][cava]
        self.__player_board[is_player_board][cava] = 0

        if (cava_qntd_pecas == 0):
            print('Esta cava está vazia!')
            os.system('pause')
            return self
        
        while cava_qntd_pecas > 0:
            cava += direcao
            
            if (cava < 0):
                cava = -1
                direcao = 1

                if (cava_qntd_pecas >= 1 and self.__turno_jogador_1):
                    self.__player_board[0][6] += 1
                    cava_qntd_pecas -= 1
                    continue

            elif (cava > 5):
                cava = 6
                direcao = -1

                if (cava_qntd_pecas >= 1 and not self.__turno_jogador_1):
                    self.__player_board[1][6] += 1
                    cava_qntd_pecas -= 1
                    continue

            self.__player_board[0 if direcao == -1 else 1][cava] += 1
            cava_qntd_pecas -= 1

        if (cava != -1 and cava != 6):
            self.__verifica_cava_vazia__(cava, is_player_board)
            self.__turno_jogador_1 = not self.__turno_jogador_1

        self.__verifica_termino_jogo__()

        return self

    def __limpar_tabuleiro__(self):
        """
            Função privada que limpa o tabuleiro.

            (void) -> MancalaBoard
        """
        
        self.__board_linha_00 = ''
        self.__board_linha_01 = ''
        self.__board_linha_02 = ''
        self.__board_linha_03 = ''
        self.__board_linha_04 = ''
        self.__board_linha_05 = ''
        self.__board_linha_06 = ''
        self.__board_linha_07 = ''
        self.__board_linha_08 = ''
        self.__board_linha_09 = ''
        self.__board_linha_10 = ''

        return self
    
    def mostrar_tabuleiro(self):
        """
            Função que retorna a propria classe e faz um print na tela com o tabuleiro montado.

            (None) -> MancalaBoard
        """

        os.system('cls')
        
        self.__limpar_tabuleiro__()
        self.__montar_cava_pontuacao__(0)

        for player_index in range(0, 2, 1):
            for cava_index in range(0, 6, 1):
                self.__montar_cavas__(player_index, cava_index)

        self.__montar_cava_pontuacao__(1)
        
        print(self.__board_linha_00)
        print(self.__board_linha_01)
        print(self.__board_linha_02)
        print(self.__board_linha_03)
        print(self.__board_linha_04)
        print(self.__board_linha_05)
        print(self.__board_linha_06)
        print(self.__board_linha_07)
        print(self.__board_linha_08)
        print(self.__board_linha_09)
        print(self.__board_linha_10)

        return self

    def jogar(self):
        """
            Função que gerencia a movimentação do jogador e retorna a propria classe.

            (None) -> MancalaBoard
        """

        print("Vez do jogador {0}".format(self.nome_jogador_1 if self.__turno_jogador_1 == False else self.nome_jogador_2))
        print("Selecione a cava para jogar:")
        try:
            cava = int(input())
        except:
            print("Insira uma número de cava válida!")
            os.system('pause')
            return self

        self.__movimentar_peca__(cava)

        return self

    def finaliza_jogo(self):
        """
            Função que finaliza o jogo e retorna a pontuação final.

            (None) -> [int, int]
        """

        soma1 = 0
        soma2 = 0

        for valor in self.__player_board[0][0:5]: soma1 += valor
        for valor in self.__player_board[1][0:5]: soma2 += valor

        self.__player_board[0][6] += soma1
        self.__player_board[1][6] += soma2

        return [self.__player_board[0][6], self.__player_board[1][6]]
    
    def get_manual():
        """
            Esta função estática (chamada sempre através de Tela.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__'] = MancalaBoard.__init__.__doc__
        manual['__str__'] = MancalaBoard.__str__.__doc__
        manual['show_board'] = MancalaBoard.show_board.__doc__
        manual['movimentar_peca'] = MancalaBoard.movimentar_peca.__doc__
        manual['__player_board'] = '# Lista de listas que representa o tabuleiro do jogo.'
        manual['__pecas_jogo'] = '# Representação gráfica das peças do jogo.'
        manual['__board_linha_00 ate 10'] = '# Representação gráfica da linha XX do tabuleiro.'
        return manual