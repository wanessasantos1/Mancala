import sys
sys.path.insert(0,"..")

from modules.interface_usuario import InterfaceUsuario

__author__ = ['Wanessa Pinto dos Santos']
__copyright__ = 'Copyright 2022'
__credits__ = ['Wanessa Pinto Santos']
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = 'Wanessa Pinto dos Santos'
__email__ = 'wanessa.santos@poli.ufrj.br'
__status__ = 'Production'

def testANSI():
    interface = InterfaceUsuario()
    #interface.printCaracteres()
    interface.print("Hello",'CYAN',True)
    interface.print("Mate",'RED',True)

    print(f"{interface.strANSI('Hello','cyan')} {interface.strANSI('World','yellow')}")

testANSI()