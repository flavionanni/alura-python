class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando um objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def verificar_saldo(self):
        print(f"Saldo: R${self.saldo:.{2}f}")

    def depositar(self, valor):
        self.saldo += valor
        self.extrato()

    def sacar(self, valor):
        self.saldo -= valor
        self.extrato()
