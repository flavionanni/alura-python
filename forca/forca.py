import random

def jogar():

    print("********************************")
    print("***Bem vindo no jogo da Forca***")
    print("********************************")

    
    with open("forca/palavra.txt", "r") as arquivo:

        palavras = []

        for palavra in arquivo:
            palavra = palavra.strip() # tira qualquer espaço entre as palavras, inclusive o \n
            palavras.append(palavra) #adiciona cada palavra em um list
    
    numero = random.randrange(0, len(palavras)) # A variavel número recebe um valor aleatório para depois ser o index da list

    palavra_secreta = palavras[numero].upper() # Dado o número aleatório, ele busca uma palavra na posição do número.

    escopo_palavra = ["_" for letra in palavra_secreta]

    print(escopo_palavra)

    enforcou = False
    acertou = False
    tentativas = len(palavra_secreta)

    while(not enforcou and not acertou):
        chute_usuario = input("Digite uma letra:").strip().upper()

        index = 0
        if(chute_usuario in palavra_secreta):
            for letra in palavra_secreta:
                if(chute_usuario == letra):
                    escopo_palavra[index] = letra

                index = index + 1

        else:
            tentativas -= 1
            if tentativas != 0 : 
                print(f"Você ainda tem {tentativas} tentativas antes de ser enforcado.")


        print(escopo_palavra)

        enforcou = tentativas == 0
        acertou = "_" not in escopo_palavra

    if(acertou):
        print("Você ganhou !!")
    else:
        print(f"Você perdeu, a palavra secreta era {palavra_secreta}!")

    print("Fim do Jogo")


if(__name__ == "__main__"):
    jogar()
