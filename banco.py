from random import choice, randint
from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

admin = 0
numero_sua_conta: int = 0
contas: List[Conta] = []


def main() -> None:
    setup()
    print('-------------------------------------------------------------------------------------------\n'
          '========================= EXERCÍCIO - SISTEMA BANCÁRIO ====================================\n'
          '-------------------------------------------------------------------------------------------')
    if admin == 1:
        criar_conta()
    menu()


def setup() -> None:
    loop = True
    global admin
    while loop:
        admin = int(input('-------> Você deseja iniciar a simulação como:\n'
                          '1) CLIENTE\n'
                          '2) ADMINISTRADOR\n'
                          '>>> DIGITE O CÓDIGO NUMÉRICO: '))
        if admin == 1 or admin == 2:
            break
        else:
            print('### OPÇÃO INVÁLIDA! ###\n')
    while loop:
        if admin == 2:
            c_teste = int(input('\n-------> Você deseja que o sistema gere contas teste?\n'
                                '1) SIM\n'
                                '2) NÃO\n'
                                '>>> DIGITE O CÓDIGO NUMÉRICO: '))
            if c_teste == 1:
                quantidade = int(input('>>> Informe a quantidade: '))
                gerar_contas(quantidade)
                print(f'-------> FORAM GERADAS {quantidade} CONTAS COM SUCESSO <-------\n')
                break
            else:
                print(f'-------> SISTEMA INICIALIZADO SEM CONTAS CADASTRADAS <-------\n')
                break
        else:
            print('-------> MODO CLIENTE: \n'
                  '\n>> GERANDO CONTAS TESTES PARA OS TESTES DE TRANSFERÊNCIA!\n')
            gerar_contas(3)
            sleep(1)
            print('-------> FORAM GERADAS 3 CONTAS COM SUCESSO <-------\n')
            break


def menu() -> None:
    if admin == 2:
        print('\n>>> Selecione uma opção através do código numérico:\n'
              '0) Ver conta\n'
              '1) Listar contas\n'
              '2) Criar conta\n'
              '3) Efetuar saque\n'
              '4) Efetuar deposito\n'
              '5) Efetuar transferência\n'
              '6) Aumentar limite\n'
              '7) Pagar fatura\n'
              '8) Sair do sistema\n')
    else:
        print('\n>>> Selecione uma opção através do código numérico:\n'
              '0) Ver conta\n'
              '1) Efetuar saque\n'
              '2) Efetuar deposito\n'
              '3) Efetuar transferência\n'
              '4) Aumentar limite\n'
              '5) Pagar fatura\n'
              '6) Sair do sistema\n')

    escolha: int = int(input('>>> DIGITE O CÓDIGO NUMÉRICO: '))

    if escolha == 0:
        ver_conta()
    elif escolha == 1:
        if admin == 2:
            listar_contas()
        else:
            efetuar_saque()
    elif escolha == 2:
        if admin == 2:
            criar_conta()
        else:
            efetuar_deposito()
    elif escolha == 3:
        if admin == 2:
            efetuar_saque()
        else:
            efetuar_transferencia()
    elif escolha == 4:
        if admin == 2:
            efetuar_deposito()
        else:
            aumentar_limite()
    elif escolha == 5:
        if admin == 2:
            efetuar_transferencia()
        else:
            pagar_fatura()
    elif escolha == 6 and admin == 2:
        if admin == 2:
            aumentar_limite()
        else:
            print('----------------- SISTEMA FECHANDO -----------------')
            sleep(1)
            print('----------------------- FIM ------------------------')
            exit(0)
    elif escolha == 7 and admin == 2:
        pagar_fatura()
    elif escolha == 8 and admin ==2:
        print('----------------- SISTEMA FECHANDO -----------------')
        sleep(1)
        print('----------------------- FIM ------------------------')
        exit(0)
    else:
        print('>>> ERRO: OPÇÃO INVÁLIDA, TENTE NOVAMENTE! <<<')
        sleep(1)
        menu()


def criar_conta() -> None:
    print('\n-------------------------- Criando conta --------------------------')
    nome: str = str(input('>>> Digite o nome: '))
    email: str = str(input('>>> Digite o e-mail: '))
    cpf: str = str(input('>>> Digite o CPF: '))
    data: str = str(input('>>> Digite o data de nascimento: '))
    try:
        global numero_sua_conta
        cliente: Cliente = Cliente(nome=nome, email=email, cpf=cpf, data_nascimento=data)
        conta: Conta = Conta(cliente)
        numero_sua_conta = conta.numero
        contas.append(conta)
        print('---- CONTA CADASTRADA COM SUCESSO\n')
        print(cliente)
        print(conta)
        sleep(1)
        menu()
    except:
        print('### OCORREU ALGUM ERRO ###')
        sleep(1)
        criar_conta()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('>>> Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_codigo(numero)

        if conta:
            if admin == 1:
                if numero == numero_sua_conta:
                    valor: float = float(input('>>> Informe o valor do saque: '))
                    conta.sacar(valor)
                    sleep(1)
                    menu()
                else:
                    print('### VOCÊ SÓ PODE SACAR DA SUA CONTA ###')
                    print(f'### O NÚMERO DA SUA CONTA É {numero_sua_conta} ###')
                    sleep(1)
                    menu()
            if admin == 2:
                valor: float = float(input('>>> Informe o valor do saque: '))
                conta.sacar(valor)
                sleep(1)
                menu()
        else:
            print(f'Não foi encontrada a conta com número: {numero}')
            sleep(1)
            menu()

    else:
        print('### Ainda não existem contas cadastradas ###')
        sleep(1)
        menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('>>> Informe o código da conta: '))
        conta: Conta = buscar_conta_por_codigo(numero)

        if conta:
            valor: float = float(input('>>> Informe o valor de depósito: '))
            conta.depositar(valor)
            sleep(1)
            menu()
        else:
            print(f'Não foi encontrada a conta com número: {numero}')
            sleep(1)
            menu()

    else:
        print('### Ainda não existem contas cadastradas ###')
        sleep(1)
        menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('>>> Informe o número da sua conta: '))
        conta_o: Conta = buscar_conta_por_codigo(numero_o)
        if conta_o:
            if admin == 1:
                if numero_o == numero_sua_conta:
                    num_conta_d: int = int(input('>>> Informe o número da conta destino: '))
                    conta_d: Conta = buscar_conta_por_codigo(num_conta_d)
                    if conta_d:
                        valor: float = float(input('>>> Informe o valor a ser transferido: '))
                        conta_o.transferir(destino=conta_d, valor=valor)
                        sleep(1)
                        menu()
                    else:
                        print('### CONTA DESTINO NÃO EXISTE ###')
                        sleep(1)
                        menu()
                else:
                    print('### VOCÊ SÓ PODE TRANSFERIR DA SUA CONTA ###')
                    print(f'### O NÚMERO DA SUA CONTA É {numero_sua_conta} ###')
                    sleep(1)
                    menu()
            if admin == 2:
                num_conta_d: int = int(input('>>> Informe o número da conta destino: '))
                conta_d: Conta = buscar_conta_por_codigo(num_conta_d)
                if conta_d:
                    valor: float = float(input('>>> Informe o valor a ser transferido: '))
                    conta_o.transferir(destino=conta_d, valor=valor)
                    sleep(1)
                    menu()
                else:
                    print('### CONTA DESTINO NÃO EXISTE ###')
                    sleep(1)
                    menu()
        else:
            print('### A CONTA INFORMADA NAO EXISTE ###')
            sleep(1)
            menu()
    else:
        print('### Ainda não existem contas cadastradas ###')
        sleep(1)
        menu()


def aumentar_limite() -> None:
    if len(contas) > 0:
        numero: int = int(input('>>> Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_codigo(numero)

        if conta:
            if admin == 1:
                if numero == numero_sua_conta:
                    valor: float = float(input('>>> Informe o valor desejado: '))
                    conta.altera_limite(valor)
                    sleep(1)
                    menu()
                else:
                    print('### VOCÊ SÓ PODE AUMENTAR O LIMITE DA SUA CONTA ###')
                    print(f'### O NÚMERO DA SUA CONTA É {numero_sua_conta} ###')
                    sleep(1)
                    menu()
            if admin == 2:
                valor: float = float(input('>>> Informe o valor desejado: '))
                conta.altera_limite(valor)
                sleep(1)
                menu()
        else:
            print(f'Não foi encontrada a conta com número: {numero}')
            sleep(1)
            menu()
    else:
        print('### Ainda não existem contas cadastradas ###')
        sleep(1)
        menu()


def pagar_fatura() -> None:
    if len(contas) > 0:
        numero: int = int(input('>>> Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_codigo(numero)

        if conta:
            if admin == 1:
                if numero == numero_sua_conta:
                    conta.pagar_fatura()
                    sleep(1)
                    menu()
                else:
                    print('### VOCÊ SÓ PODE PAGAR A FATURA DA SUA CONTA ###')
                    print(f'### O NÚMERO DA SUA CONTA É {numero_sua_conta} ###')
                    sleep(1)
                    menu()
            if admin == 2:
                conta.pagar_fatura()
                sleep(1)
                menu()
        else:
            print(f'Não foi encontrada a conta com número: {numero}')
            sleep(1)
            menu()
    else:
        print('### Ainda não existem contas cadastradas ###')
        sleep(1)
        menu()


def ver_conta() -> None:
    if len(contas) > 0:
        numero: int = int(input('>>> Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_codigo(numero)

        if conta:
            if admin == 1:
                if numero == numero_sua_conta:
                    print('')
                    print(conta)
                    sleep(1)
                    menu()
                else:
                    print('### VOCÊ SÓ PODE VER A SUA CONTA ###')
                    print(f'### O NÚMERO DA SUA CONTA É {numero_sua_conta} ###')
                    sleep(1)
                    menu()
            if admin == 2:
                print('')
                print(conta)
                sleep(1)
                menu()
        else:
            print(f'Não foi encontrada a conta com número: {numero}')
            sleep(1)
            menu()

    else:
        print('### Ainda não existem contas cadastradas ###')
        sleep(1)
        menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('--------------- LISTAGEM DE CONTAS ---------------')
        for conta in contas:
            print(conta)
            print('---------------------------------')
            sleep(1)
        menu()
    else:
        print('### Ainda não existem contas cadastradas ###')
        sleep(1)
        menu()


def buscar_conta_por_codigo(codigo: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == codigo:
                c = conta
    return c


def gerar_dados():
    nome = choice(['Marcelo', 'Maria', 'Rodolfo', 'Amanda', 'Gabriela',
                   'Manoel', 'Sabrina', 'Daniel', 'Bruna', 'Julio'])
    email = choice(['@gmail.com', '@yahoo.com', '@outlook.com'])
    email_completo = f'{nome.lower()}{email}'
    cpf = f'{randint(100, 999)}' + f'.{randint(000, 999)}' + f'.{randint(000, 999)}' + f'-{randint(00, 99)}'
    data = f'{randint(10, 30)}/{randint(10, 12)}/{randint(1960, 1990)}'
    return nome, email_completo, cpf, data


def gerar_contas(quant: int):
    for x in range(quant):
        nome, email, cpf, data = gerar_dados()
        gc_cliente = Cliente(nome, email, cpf, data)
        print(gc_cliente)
        sleep(1)
        gc_conta = Conta(gc_cliente)
        print(gc_conta)
        contas.append(gc_conta)
        sleep(1)


if __name__ == '__main__':
    main()
