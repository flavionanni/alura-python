import random

print("********************************")
print("Bem vindo no jodo de Adivinhação")
print("********************************")

print("*"* 10, "Nível de Dificuldade", "*" * 10)
print("(1) Fácil", "(2) Médio", "(3) Difícil", "*" * 42, sep="\n")

pontuacao = 1000


dificuldade = int(input("Digitel o nível: "))

if(dificuldade == 1):
    total_de_tentativas = 20

elif(dificuldade == 2):
    total_de_tentativas = 10

else:
    total_de_tentativas = 5

numero_secreto = random.randrange(1,101)


for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa {rodada:02d} de {total_de_tentativas:02d}")
    chute_usuario = int(input("Digite um número: "))

    print(f"O número escolhido foi {chute_usuario}!")

    if(chute_usuario < 1 or chute_usuario > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue  # pula para o próximo laço

    acertou = numero_secreto == chute_usuario
    maior = chute_usuario > numero_secreto
    menor = chute_usuario < numero_secreto

    if(acertou):
        print(f"Você acertou! e obteve um total de {pontuacao} pontos.")
        break

    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")

        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    
    diferenca_pontuacao = abs(numero_secreto - chute_usuario)
    pontuacao = pontuacao - diferenca_pontuacao


print(f"Fim do jogo, o número secréto era o {numero_secreto}!")
