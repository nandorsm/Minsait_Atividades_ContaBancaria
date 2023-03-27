from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Teste do p1
# pessoa1 = Conta(10, 33.99)
# # pessoa1.__id_conta(3)
# # pessoa1.set_id_conta(11)
# # print(pessoa1.get_id_conta())
# print(f'ID da conta: {pessoa1.get_id_conta()}')
# print(f'Saldo da conta: R${pessoa1.get_saldo():.2f}')

# teste do p2 com try exception
# p2 = ContaCorrente(id_conta=1, saldo=50, limite=100)
# try:
#     valor = float(input("Digite o valor do saque: "))
#     print("Limite: ", p2.get_limite())
#     print("Saldo: ", p2.get_saldo())
#     p2.sacar("200.08")
#     print("Saldo: ", p2.get_saldo())
#     p2.sacar(valor)
#     print("Saldo: ", p2.get_saldo())
# except ValueError as e:
#     print("Digite o valor que deseja sacar em numéricos!!", e)


# Teste do p2
# p2 = ContaCorrente(id_conta=1, saldo=100, limite=200)
# valor = float(input("Digite o valor do saque/deposito: R$ "))
# print("Limite: R$ ", p2.get_limite())
# print("Saldo: R$ ", p2.get_saldo())
# p2.sacar(valor)
# #p2.depositar(valor)
# print('=' * 30)
# print("Novo limite atual: R$ ", p2.get_limite())
# print("Novo saldo atual: R$ ", p2.get_saldo())


# Teste do p3
# p3 = ContaPoupanca(id_conta=7, saldo=15000, taxa_de_rendimento=8)
# print(f'Id da conta: {p3.get_id_conta()}')
# print(f'Saldo atual: R$ {p3.get_saldo():.2f}')
# p3.depositar(2000)
# print(f'Novo saldo atual: R$ {p3.get_saldo():.2f}')
# p3.sacar(1000)
# print(f'Novo saldo atual: R$ {p3.get_saldo():.2f}')
# p3.verificar_rendimento_ao_ano()
# p3.verificar_rendimento_ao_mes()
# p3.verificar_rendimento_ao_dia()
# p3.verificar_rendimento_a_hora()
# p3.verificar_rendimento_ao_minuto()
# p3.verificar_rendimento_ao_segundo()



# taxa_anual = 8.6  = 0.086
# taxa_mensal = 3.5 = 0.035
# taxa_semanal = 1.1 = 0.011
# taxa_diaria = 0.3 = 0.003
# taxa_horaria = 0.1 = 0.001
# taxa_por_minuto = 0.03 = 0.0003
# taxa_por_segundo = 0.005 = 0.00005