import sys, os
sys.path.insert(0,"..")

from modules.mancala_manager import Mancala

__author__ = 'Wanessa Pinto dos Santos'
__copyright__ = 'Copyright 2022'
__credits__ = __author__
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = __author__
__email__ = 'wanessa.santos@poli.ufrj.br'
__status__ = 'Production'

hasStop = False

mancala = Mancala()

while (hasStop == False): 

    try:
        mancala.render_menu_principal()
        print("Digite a opção desejada: ")

        opcao = input()
        if (opcao == "0"):
            hasStop = True
        elif (opcao == "1"):
            mancala.novo_jogo()
        elif (opcao == "2"):
            mancala.carregar_jogo()
        else:
            print("Opção inválida!")
            os.system('pause')
    except Exception as e:
        print(e)
        os.system('pause')