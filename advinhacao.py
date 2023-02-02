import random

def jogar():

    print("Bem vindo ao jogo de adivinhação!\n")

    numero_secreto = random.randint(0, 100)
    pontos = 1000


    print("Qual o nivel de dificuldade?")
    print("[1] Facil   [2] Médio   [3] Dificil")

    nivel = int(input("Defina o nivel de dificuldade: "))


    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5


    for rodada in range(1, total_tentativas + 1):
        print("Tentativa",rodada, "de" , total_tentativas, sep=" ")
        chute = int(input("Digite um numero entre 1 e 100: "))
        print("Você digitou {}".format(chute))

        if(chute < 1 or chute > 100):
            print("Você deve escolher um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            print( "a resposta é", numero_secreto)
            break
        else:
            if(maior):
                print("Você errou!, O seu chute foi maior que o numero secreto")
            elif(menor):
                print("Você errou!, O seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute) 
            pontos -= pontos_perdidos

    print("Fim de jogo.")

if __name__ == "__main__":
    jogar()