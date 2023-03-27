
from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, limite: float, id_conta: int, saldo: float) -> None:
        super().__init__(id_conta, saldo)
        self.__limite = limite
    
    # Getters and Setters
    def set_limite(self, limite: float) -> float:
        self.__limite = limite

    def get_limite(self) -> float:
        return self.__limite


    def sacar(self, valor) -> float:
        try:
            if valor < 0:
                valor = 0
            elif valor <= self.get_saldo():
                self.set_saldo(self.get_saldo() - valor)
                
            elif valor <= self.get_saldo() + self.get_limite():
                valor = valor - self.get_saldo()
                self.set_saldo(0)
                self.set_limite(self.get_limite() - valor)
            else:
                print("Saldo insuficiente!")
        except TypeError as e:
            print("Digite o valor que deseja sacar em numéricos!", e)
        
    def depositar(self, valor) -> float:
        try:
            if valor > 0:
                self.set_saldo(self.get_saldo() + valor)
            else:
                print("Deposite um valor válido")
        except TypeError as e:
            print("Digite o valor que deseja depositar em numéricos!", e)


    def status(self):
        print(f'ID: {self.get_id_conta()}')
        print(f'Saldo: {self.get_saldo()}')
        print(f'Limite: {self.get_limite()}')

    def opcoes(self):
        print("O que vc deseja fazer?")
        print("-Digite 1 para sacar")
        print("-Digite 2 para depositar")
        print("-Digite 3 para sair")