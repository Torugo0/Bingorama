# Import's usados
from random import sample

# Exceções Personalizadas
class VerificaError(Exception):
    pass 

def preenche_cartela():
    '''Função que gera a cartela de bingo com números aleatórios'''
    cartela = []

    for i in range(5):
        linha = sample(range(i * 15 + 1, (i + 1) * 15 + 1), 5)
        cartela.append(linha)
    
    return cartela


def exibe_cartela(cartela):
    '''Exibe matriz estilizada'''

    print()
    print("+---------------------+")
    for i in range(5):
        print("|", end=" ")
        for j in range(5):
            print(f"{cartela[j][i]:02}", end="  ")
        print("|")
    print("+---------------------+")
    print()

def menu():
    
    print('''Bem vindo ao Bingorama !!
Digite a quantidade de jogadores abaixo''')
    while True:
        try:
            print("OBS: Mínimo de jogadores: 1, Máximo de jogadores: 5 \n")
        
            jogadores = int(input("Quantidade de jogadores: "))
            if jogadores <= 0 or jogadores > 5:
                raise VerificaError
            for i in range(jogadores):
                nova_cartela = preenche_cartela()
                exibe_cartela(nova_cartela)
            break
        except ValueError:
            print("O valor informado não é um número \n")
        except VerificaError:
            print("Quantidade de jogadores não permitida\n")

menu()