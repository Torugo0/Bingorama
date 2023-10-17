# Import's usados
from random import sample

# Exceções Personalizadas
class VerificaError(Exception):
    pass 

class ContinueError(Exception):
    pass

def preenche_cartela():
    '''Função que gera a cartela de bingo com números aleatórios'''
    cartela = []

    for i in range(5):
        linha = sample(range(i * 15 + 1, (i + 1) * 15 + 1), 5)
        cartela.append(linha)
    
    return cartela

def exibe_cartela(cartela, jogador):
    '''Função que exibe cartela estilizada'''

    print()
    print(f"Cartela do jogador {jogador}:")
    print("+----------------------+")
    for i in range(5):
        print("|", end="  ")
        for j in range(5):
            print(f"{cartela[j][i]:02}", end="  ")
        print("|")
    print("+----------------------+")
    print()
    return cartela

def valida_numero(cartela, sorteia):
    '''Função que valida o número na cartela'''
    for i in range(len(cartela)):
        for j in range(len(cartela[i])):
            if cartela[i][j] == sorteia:
                cartela[i][j] = "XX"

def verifica_ganhador():
    '''Função que verifica o ganhador'''



def game(jogadores):
    jogadores_etiquetas = [f"{i + 1}" for i in range(jogadores)]

    cartelas = [preenche_cartela() for y in range(jogadores)]
    
    while True:
        sorteia = sample(range(1, 76), 1)[0]
        
        for i in range(jogadores):
            exibe_cartela(cartelas[i], jogadores_etiquetas[i])
            valida_numero(cartelas[i], sorteia)
        print(f"Número sorteado: {sorteia}")

        while True:
            try:  
                continuar = input("Digite S para continuar: ")
                if continuar.lower() != "s":
                    raise ContinueError
                break
            except ContinueError:
                print("Digite apenas S para continuar \n")

def menu():
    print('''Bem-vindo ao Bingorama!!
Digite a quantidade de jogadores abaixo''')
    
    while True:
        try:
            print("OBS: Mínimo de jogadores: 1, Máximo de jogadores: 5 \n")
            jogadores = int(input("Quantidade de jogadores: "))
            
            if jogadores <= 0 or jogadores > 5:
                raise VerificaError
            game(jogadores)
            
        except ValueError:
            print("O valor informado não é um número\n")
        except VerificaError:
            print("Quantidade de jogadores não permitida\n")

menu()