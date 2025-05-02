import random
listaPalavras = ["banana", "abacate", "laranja", "uva", "melancia", "abacaxi", "morango"]
tamanhoLista = len(listaPalavras)
erros = 0

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

def pedirLetra(palavra, palavraCriptografada, erros):
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
        print("Tentativas restantes:", 5-erros)
    return palavraCriptografada, erros

palavra = gerarPalavra(tamanhoLista)
palavraCriptografada = criptografarPalavra(palavra)
print(palavra)
print(palavraCriptografada)


while erros < 5:
    palavraCriptografada, erros = pedirLetra(palavra, palavraCriptografada, erros)
    print(palavraCriptografada)

    if '_' not in palavraCriptografada:
        print("Parabéns! você acertou todas as letras")
        break



if erros >= 5:
    print("Você não conseguiu adivinhar a palavra... a palavra era: ", palavra)








