import os

class Ferramentas:
    """
        Esta super classe inclui todos os métodos que podem vir a ser úteis para a
        mecânica do jogo, independente das classes criadas para o jogo específico.
    """
    
    def limpaTela():
        """
            Esta função limpa toda a tela do console do Windows. 
            Com isso, é possível dar 'refresh' na tela a ser desenhada.
        """
        os.system('cls')