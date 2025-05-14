import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

x = 6

while x < 16:
    print(x)

    x += 1

print('Finished')