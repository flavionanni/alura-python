print("********************************")
print("Bem vindo no jodo de Adivinhação")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print(f"Tentativa {rodada:02d} de {total_de_tentativas:02d}")
    chute_usuario = int(input("Digite um número: "))

    print(f"O número escolhido foi {chute_usuario}!")

    acertou = numero_secreto == chute_usuario
    maior = chute_usuario > numero_secreto
    menor = chute_usuario < numero_secreto

    if(acertou):
        print("Você acertou!")

    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")

        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")
