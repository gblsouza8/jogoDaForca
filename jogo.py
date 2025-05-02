import random
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








