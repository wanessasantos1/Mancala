import sys
sys.path.insert(0,"..")

from modules.mancala_board import Mancala

board = Mancala()

board.show_board()
board.movimentar_peca(0, 7)