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


def verifica_ganhador(cartela):
    '''Função que verifica o ganhador'''

    for linha in cartela:
        if all(numbers == "XX" for numbers in linha):
            return True # Verifica se todos os elementos da linha da cartela contém um XX

    for coluna in range(len(cartela[0])):
        if all(cartela[linha][coluna] == "XX" for linha in range(len(cartela))):
            return True

    if all(cartela[i][i] == "XX" for i in range(min(len(cartela), len(cartela[0])))):
        return True 

    if all(cartela[i][len(cartela[0]) - i - 1] == "XX" for i in range(min(len(cartela), len(cartela[0])))):
        return True

    return False

def game(jogadores):
    jogadores_etiquetas = [f"Jogador {i + 1}" for i in range(jogadores)]

    cartelas = [preenche_cartela() for y in range(jogadores)]

    vencedor = None

    while vencedor is None:
        sorteia = sample(range(1, 76), 1)[0]

        for i in range(jogadores):
            exibe_cartela(cartelas[i], jogadores_etiquetas[i])
            valida_numero(cartelas[i], sorteia)

        print(f"Número sorteado: {sorteia}")

        for i in range(jogadores):
            if verifica_ganhador(cartelas[i]):
                vencedor = jogadores_etiquetas[i]
                break

        continuar = input("Digite S para continuar: ")
        print()
        if continuar.lower() != "s":
            break
    
    print(f"Parabéns ao {vencedor} por vencer o jogo!")
    


def menume():    
    while True:
        try:
            jogadores = int(input("Quantidade de jogadores: "))
            print()
            
            if jogadores <= 0 or jogadores > 5:
                raise VerificaError
            
            return jogadores
        except ValueError:
            print("O valor informado não é um número\n")
        except VerificaError:
            print("Quantidade de jogadores não permitida")
            print("OBS: Mínimo de jogadores: 1, Máximo de jogadores: 5 \n")
    

def menu():
    print('''Bem-vindo ao Bingorama!!
Digite a quantidade de jogadores abaixo
OBS: Mínimo de jogadores: 1, Máximo de jogadores: 5 \n''')
    
    jogadores = menume()
    game(jogadores)


menu()