
def jogar():

    print("********************************")
    print("***Bem vindo no jogo da Forca***")
    print("********************************")

    palavra_secreta = "flavio".upper()

    escopo_palavra = [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ']

    print(escopo_palavra)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute_usuario = input("Digite uma letra:").strip().upper()

        index = 0
        if(chute_usuario in palavra_secreta):
            for letra in palavra_secreta:
                if(chute_usuario == letra):
                    escopo_palavra[index] = letra

                index = index + 1

        else:
            erros += 1

        print(escopo_palavra)

        enforcou = erros == 6
        acertou = " _ " not in escopo_palavra

    if(acertou):
        print("Você ganhou !!")
    else:
        print(f"Você perdeu, a palavra secreta era {palavra_secreta}!")

    print("Fim do Jogo")


if(__name__ == "__main__"):
    jogar()
