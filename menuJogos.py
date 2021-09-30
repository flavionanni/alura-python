from adivinhacao import adivinhacao

print("********************************")
print("*********Menu de Jogos!*********")
print("********************************")

print("(1) Adivinhacao")
escolha_do_jogo = int(input("Qual jogo deseja jogar ? "))

if(escolha_do_jogo == 1):
    adivinhacao.jogar()
