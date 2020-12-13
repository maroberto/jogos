import random

def jogar():
    print("********************************")
    print("Bem vindo no jogo de advinhação!")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel =  int (input("Define o nível"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa: {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Parabéns, você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("você errou! O seu chute foi maior do que número secreto.")
            elif(menor):
                print("você errou! O seu chute foi menor do que número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) # 40 - 20 = 20
            pontos = pontos - pontos_perdidos


        rodada = rodada + 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()



