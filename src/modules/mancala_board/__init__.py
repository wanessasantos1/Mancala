class Mancala:
    player_1_score = 0
    player_2_score = 0

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

    def __calcular_pontuacao_cava__(self, tamanho, player, local):
        cava_pontuacao = []

        for x in range(0, tamanho, 1):
            cava_pontuacao.append(['', ''])

        pontuacao = self.__player_board[player][local]

        for (x, cava_linha) in enumerate(cava_pontuacao):
            for y in range(0, len(cava_linha)):
                if (pontuacao > 8):
                    cava_pontuacao[x][y] = self.__pecas_jogo[8]
                    pontuacao -= 8

                elif (pontuacao < 8):
                    cava_pontuacao[x][y] = self.__pecas_jogo[pontuacao]

                    pontuacao -= pontuacao

        return cava_pontuacao

    def __montar_cava_pontuacao__(self, player):
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
        cava_pontuacao = self.__calcular_pontuacao_cava__(3, player, cava)
        
        if (player == 0):
            
            self.__board_linha_00 += ('⎾ ⎺ ⎺ ⏋ \t')
            self.__board_linha_01 += ('| {0} {1} | \t'.format(cava_pontuacao[0][0], cava_pontuacao[0][1]))
            self.__board_linha_02 += ('| {0} {1} | \t'.format(cava_pontuacao[1][0], cava_pontuacao[1][1]))
            self.__board_linha_03 += ('| {0} {1} | \t'.format(cava_pontuacao[2][0], cava_pontuacao[2][1]))
            self.__board_linha_04 += ('⎿ ⎽ ⎽ ⏌ \t')
            self.__board_linha_05 += ('        \t')

        if (player == 1):
            self.__board_linha_06 += ('⎾ ⎺ ⎺ ⏋ \t')
            self.__board_linha_07 += ('| {0} {1} | \t'.format(cava_pontuacao[0][0], cava_pontuacao[0][1]))
            self.__board_linha_08 += ('| {0} {1} | \t'.format(cava_pontuacao[1][0], cava_pontuacao[1][1]))
            self.__board_linha_09 += ('| {0} {1} | \t'.format(cava_pontuacao[2][0], cava_pontuacao[2][1]))
            self.__board_linha_10 += ('⎿ ⎽ ⎽ ⏌ \t')

        return self

    def movimentar_peca(self, player, cava):
        if ((cava < 0) | (cava > 5)):
            print('Cava inválida!')
            return self

        direction = player == 0 if -1 else 1

        cava_qntd_pecas = self.__player_board[player][cava]
    
    def show_board(self):

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