import random

def gera_cartela():
    return random.sample(range(1, 76), 5)

def sortea_numero():
    return random.randint(1, 75)

def start_jogo():
    cartela = gera_cartela()
    print(f"Sua cartela de bingo: {cartela}")
    numerosSorteados = []
    qtdeSorteios = 0
    while len(cartela) > 0:
        numero = sortea_numero()
        numerosSorteados.append(numero)
        qtdeSorteios += 1
        if numero in cartela:
            cartela.remove(numero)

      
    print(f"A quantidade de números sorteados {qtdeSorteios}.")
    print(f"OS numeros sorteados foram:  {numerosSorteados}.")
    print(f"Parabéns você finalizaou o Bingo da Dot!!!")


start_jogo()
