import forca
import advinhacao


print("Escolha o seu jogo")

print("[1] Jogo da forca   [2] Jogo de advinhação")

jogo = int(input("Qual o jogo ? "))

if jogo == 1:
    print("Jogando Forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando Advinhação")
    advinhacao.jogar()