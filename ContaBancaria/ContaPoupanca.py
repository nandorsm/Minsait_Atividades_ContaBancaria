from Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, taxa_de_rendimento: float, id_conta: int, saldo: float) -> None:
        super().__init__(id_conta, saldo)
        self.__taxa_de_rendimento = taxa_de_rendimento

    
    def set_taxa_de_rendimento(self, taxa_de_rendimento: float) -> float:
        self.__taxa_de_rendimento = taxa_de_rendimento

    def get_taxa_de_rendimento(self) -> float:
        return self.__taxa_de_rendimento
    
    def sacar(self, valor) -> float:
        try:
            if valor < 0:
                valor = 0
            elif valor <= self.get_saldo():
                self.set_saldo(self.get_saldo() - valor)
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
    
    def verificar_rendimento_ao_ano(self):
        rendimento = (self.get_taxa_de_rendimento() / 100) * self.get_saldo()
        return print(f'Seu rendimento ao Ano será de: {rendimento:.2f}')
    
    def verificar_rendimento_ao_mes(self):
        taxa_de_rendimento_ao_mes = self.get_taxa_de_rendimento() / 12.6
        rendimento = (taxa_de_rendimento_ao_mes / 100) * self.get_saldo()
        return print(f'Seu rendimento ao Mês será de: {rendimento:.2f}')
    
    def verificar_rendimento_a_semana(self):
        taxa_de_rendimento_a_semana = self.get_taxa_de_rendimento() / 38.3
        rendimento = (taxa_de_rendimento_a_semana / 100) * self.get_saldo()
        return print(f'Seu rendimento a Semana será de: {rendimento:.2f}')
    
    def verificar_rendimento_ao_dia(self):
        taxa_de_rendimento_ao_dia = self.get_taxa_de_rendimento() / 380.4
        rendimento = (taxa_de_rendimento_ao_dia / 100) * self.get_saldo()
        return print(f'Seu rendimento ao Dia será de: {rendimento:.2f}')
    
    def verificar_rendimento_a_hora(self):
        taxa_de_rendimento_a_hora = self.get_taxa_de_rendimento() / 7200.5
        rendimento = (taxa_de_rendimento_a_hora / 100) * self.get_saldo()
        return print(f'Seu rendimento a Hora será de: {rendimento:.3f}')
    
    def verificar_rendimento_ao_minuto(self):
        taxa_de_rendimento_ao_minuto = self.get_taxa_de_rendimento() / 432000
        rendimento = (taxa_de_rendimento_ao_minuto / 100) * self.get_saldo()
        return print(f'Seu rendimento ao Minuto será de: {rendimento:.8f}')
    
    def verificar_rendimento_ao_segundo(self):
        taxa_de_rendimento_ao_segundo = self.get_taxa_de_rendimento() / 2592000
        rendimento = (taxa_de_rendimento_ao_segundo / 100) * self.get_saldo()
        return print(f'Seu rendimento ao Segundo será de: {rendimento:.8f}')
    

    def status(self):
        print(f'ID: {self.get_id_conta()}')
        print(f'Saldo: {self.get_saldo()}')
        print(f'Taxa de rendimento: {self.get_taxa_de_rendimento()}')

    def opcoes(self):
        print("O que vc deseja fazer?")
        print("-Digite 1 para sacar")
        print("-Digite 2 para depositar")
        print("-Digite 3 para verificar os rendimentos por período")
        print("-Digite 4 para sair")
