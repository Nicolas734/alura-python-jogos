
import random
def jogar():
    print("Bem vindo ao jogo de forca!\n")

    arquivo = open("palavras.txt", "r")
    palavras = [ linha.strip() for linha in arquivo ]

    palavra_secretra = palavras[random.randrange(0, len(palavras))].strip().lower()
    enforcou = False
    acertou = False
    erros = 0

    letras_acertadas = ["_"] * len(palavra_secretra)
    # letras_acertadas = ["_" for letra in palavra_secretra]


    while not enforcou and not acertou:
        chute = input("Tente advinhar a letra: ").strip().lower()

        if chute == palavra_secretra:
            acertou = True
            break
        elif chute in letras_acertadas:
            print("letra já utilizada")
        elif chute not in palavra_secretra:
            erros += 1
        else:
            for index, letra in enumerate(palavra_secretra):
                if chute == letra.lower():
                    print("Encontrei a letra {} na posicão {}".format(letra, index + 1))
                    letras_acertadas[index] = chute
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(" ".join(letras_acertadas))

    if acertou:
        print("você acertou!, a resposta era {}.".format(palavra_secretra.capitalize()))
        print("Fim de jogo")
    else:
        print("você perdeu :( , a resposta era {}.".format(palavra_secretra.capitalize()))

if __name__ == "__main__":
    jogar()