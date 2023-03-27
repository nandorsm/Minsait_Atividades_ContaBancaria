from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca


pessoa_conta_corrente = ContaCorrente(id_conta=1, saldo=2400, limite=3000)
pessoa_conta_poupanca = ContaPoupanca(id_conta=2, saldo=25000, taxa_de_rendimento=8)

try:
    selecionar_minha_conta = int(input("Digite 1 para acessar a sua Conta Corrente\nDigite 2 para acessar a sua conta Poupança\n -->"))
    while selecionar_minha_conta != 1 and selecionar_minha_conta != 2:
        selecionar_minha_conta = int(input("Digite 1 para acessar a sua Conta Corrente\nDigite 2 para acessar a sua conta Poupança\n -->"))
except ValueError as e:
    print("Erro, Valor inválido!", e)

if selecionar_minha_conta == 1:
    print("--- Sua conta corrente ---")
    print(f'ID: {pessoa_conta_corrente.get_id_conta()}')
    print(f'Saldo: {pessoa_conta_corrente.get_saldo()}')
    print(f'Limite: {pessoa_conta_corrente.get_limite()}')
    
    print("O que vc deseja fazer?")
    print("-Digite 1 para sacar")
    print("-Digite 2 para depositar")
    print("-Digite 3 para sair")
    opcao = int(input("-->"))
    while opcao != 3:
        while opcao != 1 and opcao != 2:
            print("O que vc deseja fazer?")
            print("-Digite 1 para sacar")
            print("-Digite 2 para depositar")
            print("-Digite 3 para sair")
            opcao = int(input("-->"))
        if opcao == 1:
            valor = float(input("Digite o valor que deseja Sacar: "))
            print("--- Sua conta corrente ---")
            pessoa_conta_corrente.sacar(valor)
            print(f'ID: {pessoa_conta_corrente.get_id_conta()}')
            print(f'Saldo: {pessoa_conta_corrente.get_saldo()}')
            print(f'Limite: {pessoa_conta_corrente.get_limite()}')
            print("O que vc deseja fazer?")
            print("-Digite 1 para sacar")
            print("-Digite 2 para depositar")
            print("-Digite 3 para sair")
            opcao = int(input("-->"))
        elif opcao == 2:
            valor = float(input("Digite o valor que deseja Depositar: "))
            print("--- Sua conta corrente ---")
            pessoa_conta_corrente.depositar(valor)
            print(f'ID: {pessoa_conta_corrente.get_id_conta()}')
            print(f'Saldo: {pessoa_conta_corrente.get_saldo()}')
            print(f'Limite: {pessoa_conta_corrente.get_limite()}')
            print("O que vc deseja fazer?")
            print("-Digite 1 para sacar")
            print("-Digite 2 para depositar")
            print("-Digite 3 para sair")
            opcao = int(input("-->"))
        elif opcao == 3:
            print("Obrigado por utilizar nossos serviços, até logo!")
        else:
            print("Opção inválida, tente novamente com as opções 1, 2 ou 3")




    
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