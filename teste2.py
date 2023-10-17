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
    '''Exibe matriz estilizada lado a lado'''

    print()
    print("+---------------------+")
    for linha in zip(*cartela):
        print("|", end=" ")
        for numero in linha:
            print(f"{numero:02}", end="  ")
        print("|")
    print("+---------------------+")
    print()

    return cartela

def valida_numero(cartelas, sorteia):
    '''Função que valida o número na cartela'''
    for cartela in cartelas:
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    if cartela[k][i][j] == sorteia:
                        cartela[k][i][j] = "X"

def menu():
    print('''Bem-vindo ao Bingorama!!
Digite a quantidade de jogadores abaixo''')

    while True:
        try:
            print("OBS: Mínimo de jogadores: 1, Máximo de jogadores: 5 \n")
            jogadores = int(input("Quantidade de jogadores: "))

            if jogadores <= 0 or jogadores > 5:
                raise VerificaError

            cartelas = [preenche_cartela() for _ in range(jogadores)]

            while True:
                sorteia = sample(range(1, 76), 1)[0]
                print(f"Número sorteado: {sorteia}")
                exibe_cartela(cartelas)
                valida_numero(cartelas, sorteia)

                continuar = input("Deseja continuar? (S para sim, qualquer tecla para sair): ")
                if continuar.lower() != "s":
                    break

            break

        except ValueError:
            print("O valor informado não é um número\n")
        except VerificaError:
            print("Quantidade de jogadores não permitida\n")

menu()
