import os, datetime
from modules.errors.mancala_errors import MancalaLoadGameError, MancalaMovementInvalidError

from modules.jogador import Jogador

class MancalaBoard:
    """
        Esta super classe inclui todos os métodos e atributos que são úteis para a montagem e gerenciamento do jogo principal.
        Faz a montagem inicial de cada player;
        Faz a montagem inicial de cada tipo de quantidade de peça do jogo;

        Inicia vazio o board de cada linha que irá representar o tabuleiro.
    """

    jogador_1 = Jogador()
    jogador_2 = Jogador()
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
        nome_jogador_1 = input()
        print('Insira o nome do jogador 2:')
        nome_jogador_2 = input()

        self.jogador_1.set_nome(nome_jogador_1).carregar()
        self.jogador_2.set_nome(nome_jogador_2).carregar()

        self.__player_board = [
            [4, 4, 4, 4, 4, 4, 0],
            [4, 4, 4, 4, 4, 4, 0]
        ]
        self.__turno_jogador_1 = True

        self.limpar_tabuleiro()

        self.jogo_status = 1
        self.log('MANCALA-INICIO', 'INFO', 'Um novo jogo foi iniciado com sucesso!')

        return self

    def comecar_jogo(self):


        return self

    def calcular_pontuacao_cava(self, tamanho, player, local):
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

    def montar_cava_pontuacao(self, player):
        """
            Função privada que recebe o player para a montagem com a pontuação da cava.
            Retorna a propria classe e salva na linha representante a montagem do tabuleiro com a pontuação.

            (int) -> MancalaBoard
        """
        cava_pontuacao = self.calcular_pontuacao_cava(9, player, -1)

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

    def montar_cavas(self, player, cava):
        """
            Função privada que recebe o player para a contagem da pontuação da cava.
            Retorna a propria classe e salva na linha representante a montagem do tabuleiro com a pontuação.

            (int, int) -> MancalaBoard
        """
        cava_pontuacao = self.calcular_pontuacao_cava(3, player, cava)
        
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

    def verifica_cava_vazia(self, cava, player_board):
        """
            Função privada que verifica se a cava está vazia.
            Retorna True se a cava estiver vazia, False se não estiver.

            (int, int) -> MancalaBoard
        """

        pontuacao_cava_oposta = 0

        if (self.__player_board[player_board][cava] == 1):
            if (player_board == 0):
                pontuacao_cava_oposta = self.__player_board[1][cava]

                self.__player_board[0][6] += pontuacao_cava_oposta
                self.__player_board[1][cava] = 0

            if (player_board == 1):
                pontuacao_cava_oposta = self.__player_board[0][cava]

                self.__player_board[1][6] += pontuacao_cava_oposta
                self.__player_board[0][cava] = 0

            self.log('MANCALA-MOVIMENTO', 'INFO', 'Jogador {0} realizou um bom movimento e capturou um total de '+ str(pontuacao_cava_oposta) +' do inimigo!', player_board)

        return self

    def verifica_termino_jogo(self):
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

    def movimentar_peca(self, cava):
        """
            Função que recebe o player para a movimentação da cava selecionada.
            Retorna a propria classe e faz o gerenciamento de movimentação de pedrinha em cada cava.

            (int, int) -> MancalaBoard
        """

        direcao = -1 if self.__turno_jogador_1 else 1
        is_player_board = 0 if self.__turno_jogador_1 else 1

        if ((cava < 0) or (cava > 5)):
            print('Cava inválida!')
            self.log('MANCALA-MOVIMENTO', 'WARN', 'Jogador {0} informou uma cava ('+ str(cava) +') inválida!', is_player_board)
            os.system('pause')
            return self
        
        cava_qntd_pecas = self.__player_board[is_player_board][cava]
        self.__player_board[is_player_board][cava] = 0

        if (cava_qntd_pecas == 0):
            print('Esta cava está vazia!')
            self.log('MANCALA-MOVIMENTO', 'WARN', 'Jogador {0} informou uma cava ('+ str(cava) +') vazia!', is_player_board)
            os.system('pause')
            return self
        
        self.log('MANCALA-MOVIMENTO', 'INFO', 'Jogador {0} realizou um movimento da cava ('+ str(cava) +')!', is_player_board)
        
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
            self.verifica_cava_vazia(cava, is_player_board)
            self.__turno_jogador_1 = not self.__turno_jogador_1
        else:
            self.log('MANCALA-MOVIMENTO', 'INFO', 'Jogador {0} realizou um bom movimento e vai jogar novamente!', is_player_board)

        self.salvar_jogo()
        self.verifica_termino_jogo()

        return self

    def limpar_tabuleiro(self):
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
        
        self.limpar_tabuleiro()
        self.montar_cava_pontuacao(0)

        for player_index in range(0, 2, 1):
            for cava_index in range(0, 6, 1):
                self.montar_cavas(player_index, cava_index)

        self.montar_cava_pontuacao(1)
        
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

        print("Vez do jogador {0}".format(self.jogador_1.get_nome() if self.__turno_jogador_1 else self.jogador_2.get_nome()))
        print("Selecione a cava para jogar:")
        try:
            cava = int(input())
        except:
            print("Insira uma número de cava válida!")
            message = 'O jogador {0} tentou inserir um caractere inválido!', 0 if self.__turno_jogador_1 else 1
            self.log('MANCALA-JOGAR', 'EXCEPT', message)
            os.system('pause')
            raise MancalaMovementInvalidError(message)

        self.movimentar_peca(cava)

        return self

    def salvar_jogo(self):
        """
            Função que salva o jogo atual.

            (None) -> MancalaBoard
        """

        save_file = open("saves/save_1.txt", "w+")

        save_file.write('nome_jogador_1: ' + self.jogador_1.get_nome() + '\n')
        save_file.write('nome_jogador_2: ' + self.jogador_2.get_nome() + '\n')
        save_file.write('turno_jogador_1: ' + str(self.__turno_jogador_1) + '\n')
        save_file.write('player_board: ' + str(self.__player_board) + '\n')

        save_file.close()

        return self

    def carregar_jogo(self):
        """
            Função que carrega o jogo salvo.

            (None) -> Boolean
        """

        try:
            save_file = open("saves/save_1.txt", "r")

            for line in save_file:
                if (line.startswith('nome_jogador_1: ')):
                    self.jogador_1.set_nome(line.replace('nome_jogador_1: ', '').replace('\n', ''))
                elif (line.startswith('nome_jogador_2: ')):
                    self.jogador_2.set_nome(line.replace('nome_jogador_2: ', '').replace('\n', ''))
                elif (line.startswith('turno_jogador_1: ')):
                    self.__turno_jogador_1 = bool(line.replace('turno_jogador_1: ', '').replace('\n', ''))
                elif (line.startswith('player_board: ')):
                    self.__player_board = eval(line.replace('player_board: ', '').replace('\n', ''))

            save_file.close()
            self.jogo_status = 1

            return True
        except:
            print("Não foi possível carregar o jogo! Iniciando novo jogo!")
            self.log('MANCALA-CARREGAR', 'EXCEPT', 'Não foi possível carregar o jogo!')
            os.system('pause')
            raise MancalaLoadGameError('Não foi possível carregar o jogo!')

    def finaliza_jogo(self):
        """
            Função que finaliza o jogo e retorna a pontuação final.

            (None) -> [string, int]
        """

        soma1 = 0
        soma2 = 0

        for valor in self.__player_board[0][0:5]: soma1 += valor
        for valor in self.__player_board[1][0:5]: soma2 += valor

        self.__player_board[0][6] += soma1
        self.__player_board[1][6] += soma2

        self.log('MANCALA-FINAL', 'INFO', 'Jogo finalizado com sucesso')

        self.jogo_status = 0

        if (self.__player_board[0][6] > self.__player_board[1][6]): 
            self.log('MANCALA-FINAL', 'INFO', 'O ganhador foi o Jogador {0} com {1} pontos'.format(self.jogador_1.get_nome(), self.__player_board[0][6]))
            self.jogador_1.nova_vitoria().nova_pontuacao(self.__player_board[0][6]).salvar()
            self.jogador_2.nova_derrota().nova_pontuacao(self.__player_board[1][6]).salvar()
            return [self.jogador_1.get_nome(), self.__player_board[0][6]]
        else:
            self.log('MANCALA-FINAL', 'INFO', 'O ganhador foi o Jogador {0} com {1} pontos'.format(self.jogador_2.get_nome(), self.__player_board[1][6]))
            self.jogador_1.nova_derrota().nova_pontuacao(self.__player_board[0][6]).salvar()
            self.jogador_2.nova_vitoria().nova_pontuacao(self.__player_board[1][6]).salvar()
            return [self.jogador_2.get_nome(), self.__player_board[1][6]]

    def log(self, area, action, texto, jogador=-1):
        data_atual = datetime.datetime.now()
        data_hora_atual = data_atual.strftime("%d/%m/%Y %H:%M:%S")

        if (jogador != -1):
            texto = texto.format(self.jogador_1.get_nome() if jogador == 0 else self.jogador_2.get_nome())

        message = "{0} [{1}-{2}]: {3}".format(data_hora_atual, area, action, texto)

        log_file = open("log/log.txt", "a+")

        log_file.write(message + "\n")
        log_file.close()

        print(message)
        return self
    
    def get_manual():
        """
            Esta função estática (chamada sempre através de Tela.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__'] = MancalaBoard.__init__.__doc__
        manual['__str__'] = MancalaBoard.__str__.__doc__
        manual['inicializar_jogo'] = MancalaBoard.inicializar_jogo.__doc__
        manual['comecar_jogo'] = MancalaBoard.comecar_jogo.__doc__
        manual['calcular_pontuacao_cava'] = MancalaBoard.calcular_pontuacao_cava.__doc__
        manual['montar_cava_pontuacao'] = MancalaBoard.montar_cava_pontuacao.__doc__
        manual['montar_cavas'] = MancalaBoard.montar_cavas.__doc__
        manual['verifica_cava_vazia'] = MancalaBoard.verifica_cava_vazia.__doc__
        manual['verifica_termino_jogo'] = MancalaBoard.verifica_termino_jogo.__doc__
        manual['movimentar_peca'] = MancalaBoard.movimentar_peca.__doc__
        manual['limpar_tabuleiro'] = MancalaBoard.limpar_tabuleiro.__doc__
        manual['mostrar_tabuleiro'] = MancalaBoard.mostrar_tabuleiro.__doc__
        manual['jogar'] = MancalaBoard.jogar.__doc__
        manual['salvar_jogo'] = MancalaBoard.salvar_jogo.__doc__
        manual['carregar_jogo'] = MancalaBoard.carregar_jogo.__doc__
        manual['finaliza_jogo'] = MancalaBoard.finaliza_jogo.__doc__
        manual['__player_board'] = '# Lista de listas que representa o tabuleiro do jogo.'
        manual['__pecas_jogo'] = '# Representação gráfica das peças do jogo.'
        manual['__board_linha_00 ate 10'] = '# Representação gráfica da linha XX do tabuleiro.'
        manual['jogador_1'] = '# Representação do jogador 1.'
        manual['jogador_2'] = '# Representação do jogador 2.'
        manual['__turno_jogador_1'] = '# Indica se o turno é do jogador 1.'
        manual['jogo_status'] = '# Indica o status do jogo. 0 - Jogo não iniciado. 1 - Jogo iniciado. 2 - Jogo finalizado.'
        manual['__player_board'] = '# Lista de listas que representa o tabuleiro do jogo.'
        manual['__pecas_jogo'] = '# Representação gráfica das peças do jogo.'
        manual['__board_linha_00'] = '# Representação gráfica da linha XX do tabuleiro.'
        return manual