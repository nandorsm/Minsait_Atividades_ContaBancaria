from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca


pessoa_conta_corrente = ContaCorrente(id_conta=1, saldo=2400, limite=3000)
pessoa_conta_poupanca = ContaPoupanca(id_conta=2, saldo=25000, taxa_de_rendimento=8)

txt_conta_corrente = "--- Sua conta corrente ---"
txt_conta_poupanca = "--- Sua conta poupança ---"
selecionar_minha_conta = ''
opcao = ''


while type(selecionar_minha_conta) != int or selecionar_minha_conta != 1 and selecionar_minha_conta != 2:
    try:
        selecionar_minha_conta = int(input("Digite 1 para acessar a sua Conta Corrente\nDigite 2 para acessar a sua conta Poupança\n -->"))
        while selecionar_minha_conta != 1 and selecionar_minha_conta != 2:
            selecionar_minha_conta = int(input("Digite 1 para acessar a sua Conta Corrente\nDigite 2 para acessar a sua conta Poupança\n -->"))
    except ValueError:
        print("ERRO! Digite um caractere numérico!")

if selecionar_minha_conta == 1:
    print(txt_conta_corrente)
    pessoa_conta_corrente.status()
    pessoa_conta_corrente.opcoes()
    while type(opcao) != int or opcao != 1 and opcao != 2 and opcao != 3:
        try:
            opcao = int(input("-->"))
            pessoa_conta_corrente.opcoes()
        except ValueError:
            print("ERRO! Digite um caractere numérico!")
            pessoa_conta_corrente.opcoes()
    while opcao != 3:
        while opcao != 1 and opcao != 2:
            pessoa_conta_corrente.opcoes()
            opcao = int(input("-->"))
        if opcao == 1:
            valor = float(input("Digite o valor que deseja Sacar: "))
            print(txt_conta_corrente)
            pessoa_conta_corrente.sacar(valor)
            pessoa_conta_corrente.status()
            pessoa_conta_corrente.opcoes()
            opcao = int(input("-->"))
        elif opcao == 2:
            valor = float(input("Digite o valor que deseja Depositar: "))
            print(txt_conta_corrente)
            pessoa_conta_corrente.depositar(valor)
            pessoa_conta_corrente.status()
            pessoa_conta_corrente.opcoes()
            opcao = int(input("-->"))
        elif opcao == 3:
            print("Obrigado por utilizar nossos serviços, até logo!")
        else:
            print("Opção inválida, tente novamente com as opções 1, 2 ou 3")

if selecionar_minha_conta == 2:
    print(txt_conta_poupanca)
    pessoa_conta_poupanca.status()
    pessoa_conta_poupanca.opcoes()
    opcao = int(input("-->"))
    while opcao != 4:
        while opcao != 1 and opcao != 2 and opcao != 3:
            pessoa_conta_poupanca.opcoes()
            opcao = int(input("-->"))
        if opcao == 1:
            valor = float(input("Digite o valor que deseja Sacar: "))
            print(txt_conta_poupanca)
            pessoa_conta_poupanca.sacar(valor)
            pessoa_conta_poupanca.status()
            pessoa_conta_poupanca.opcoes()
            opcao = int(input("-->"))
        elif opcao == 2:
            valor = float(input("Digite o valor que deseja Depositar: "))
            print(txt_conta_poupanca)
            pessoa_conta_poupanca.depositar(valor)
            pessoa_conta_poupanca.status()
            pessoa_conta_poupanca.opcoes()
            opcao = int(input("-->"))
        elif opcao == 3 and opcao != 1 and opcao != 2:
            print(txt_conta_poupanca)
            pessoa_conta_poupanca.status()
            pessoa_conta_poupanca.verificar_rendimento_ao_ano()
            pessoa_conta_poupanca.verificar_rendimento_ao_mes()
            pessoa_conta_poupanca.verificar_rendimento_ao_dia()
            pessoa_conta_poupanca.verificar_rendimento_a_hora()
            pessoa_conta_poupanca.verificar_rendimento_ao_minuto()
            pessoa_conta_poupanca.verificar_rendimento_ao_segundo()
            pessoa_conta_poupanca.opcoes()
            opcao = int(input("-->"))
        elif opcao == 4:
            print("Obrigado por utilizar nossos serviços, até logo!")
        else:
            print("Opção inválida, tente novamente com as opções 1, 2 ou 3")
