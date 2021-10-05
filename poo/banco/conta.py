class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando um objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def verificar_saldo(self):
        print(f"Saldo: R${self.__saldo:.{2}f}")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # Gets and Setters

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def setter_(self, limite):
        self.__limite = limite
