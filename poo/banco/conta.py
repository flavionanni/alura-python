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
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Transação não autorizada! Sem saldo")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_sacar 


    # Gets and Setters
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
