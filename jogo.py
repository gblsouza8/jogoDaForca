import random
import sys


listaPalavras = ["banana", "abacate", "laranja", "uva", "melancia", "abacaxi", "morango"]
tamanhoLista = len(listaPalavras)

def gerarPalavra(tamanhoLista):
    numero_aleatorio = random.randint(0, tamanhoLista)
    palavra = listaPalavras[numero_aleatorio]
    return palavra

def criptografarPalavra(palavra):
    palavraCriptografada = ""
    tamanhoPalavra = len(palavra)
    for i in range(tamanhoPalavra):
        palavraCriptografada = palavraCriptografada + "_"
    return palavraCriptografada

def pedirLetra(palavra, palavraCriptografada, erros, limiteErros):
    letra = input("Insira uma letra: ")
    acerto = 0

    for i in range(len(palavra)):
        
        if palavra[i] == letra:
                acerto = 1
                lista_palavra = list(palavraCriptografada)
                lista_palavra[i] = letra
                palavraCriptografada = ''.join(lista_palavra)



    if acerto > 0:
        print("Você adivinhou uma letra!")
    else:
        print("Você errou... perdeu uma vida")
        erros = erros + 1
        print("Tentativas restantes:", limiteErros-erros)
    return palavraCriptografada, erros

def jogarNovamente():
    escolha = int(input("Deseja jogar novamente?\n1. Sim\n2. Não\n"))
    if escolha == 1:
        print("Reinicializando o jogo...")
        jogo()
    elif escolha == 2:
        print("Finalizando o jogo...")
        sys.exit()
    else:
        print("Escolha inválida... por favor, digite 1 ou 2")
        jogarNovamente()


def jogo():
    limiteErros = 3
    erros = 0
    palavra = gerarPalavra(tamanhoLista)
    palavraCriptografada = criptografarPalavra(palavra)
    print(palavraCriptografada)


    while erros < limiteErros:
        palavraCriptografada, erros = pedirLetra(palavra, palavraCriptografada, erros, limiteErros)
        print(palavraCriptografada)

        if '_' not in palavraCriptografada:
            print("Parabéns! você acertou todas as letras")
            break



    if erros >= limiteErros:
        print("Você não conseguiu adivinhar a palavra... a palavra era:",palavra)


    jogarNovamente()


jogo()





