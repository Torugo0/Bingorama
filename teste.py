''''''
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

    return cartela

def valida_numero(cartela, sorteia):
    '''Função que valida o número na cartela'''
    for i in range(len(cartela)):
        for j in range(len(cartela[i])):
            if cartela[i][j] == sorteia:
                cartela[i][j] = "X" 

def menu():
    print('''Bem-vindo ao Bingorama!!
Digite a quantidade de jogadores abaixo''')
    
    while True:
        try:
            print("OBS: Mínimo de jogadores: 1, Máximo de jogadores: 5 \n")
            jogadores = int(input("Quantidade de jogadores: "))
            
            if jogadores <= 0 or jogadores > 5:
                raise VerificaError
            
            cartelas = [preenche_cartela() for y in range(jogadores)]
            
            while True:
                sorteia = sample(range(1, 76), 1)[0]
                

                for cartela in cartelas:
                    exibe_cartela(cartela)
                    valida_numero(cartela, sorteia)
                print(f"Número sorteado: {sorteia}")
                    
                continuar = input("Deseja continuar? (S para sim, qualquer tecla para sair): ")
                if continuar.lower() != "s":
                    break
            
            break
        
        except ValueError:
            print("O valor informado não é um número\n")
        except VerificaError:
            print("Quantidade de jogadores não permitida\n")

menu()
