class Conta:
    def __init__(self, id_conta: int, saldo: float) -> None:
        self.__id_conta = id_conta
        self.__saldo = saldo

    #Getters and Setters
    def set_id_conta(self, id_conta: int) -> int:
        self.__id_conta = id_conta
    
    def get_id_conta(self) -> int:
        return self.__id_conta
    
    def set_saldo(self, saldo: float) -> float:
        self.__saldo = saldo
    
    def get_saldo(self) -> float:
        return self.__saldo
    

    def depositar():
        pass

    def sacar():
        pass