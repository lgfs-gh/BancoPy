from random import choice, randint
from typing import List
from time import sleep
from stringcolor import *

from models.cliente import Cliente
from models.conta import Conta

admin = 0
numero_sua_conta: int = 0
contas: List[Conta] = []


def main() -> None:
    """Inicia o sistema"""
    setup()
    print('-------------------------------------------------------------------------------------------\n'
          '========================= ' + cs('EXERCÍCIO - SISTEMA BANCÁRIO', 'yellow') + ' '
          '====================================\n '
          '-------------------------------------------------------------------------------------------')
    if admin == 1:
        criar_conta()
    menu()


# ------------------------------------------- SETUP / CONTROLE ---------------------------------------------------------
def setup() -> None:
    """Define as configurações iniciais do sistema"""
    loop = True
    global admin
    while loop:
        admin = int(input(cs('-------> Você deseja iniciar a simulação como:', 'yellow').bold() + '\n' +
                          '1) CLIENTE\n'
                          '2) ADMINISTRADOR\n'
                          '>>> DIGITE O CÓDIGO NUMÉRICO: '))
        if admin == 1 or admin == 2:
            break
        else:
            print('### OPÇÃO INVÁLIDA! ###\n')
    while loop:
        if admin == 2:
            c_teste = int(input(cs('\n-------> Você deseja que o sistema gere contas teste?', 'yellow').bold() + '\n' +
                                '1) SIM\n'
                                '2) NÃO\n'
                                '>>> DIGITE O CÓDIGO NUMÉRICO: '))
            if c_teste == 1:
                quantidade = int(input('>>> Informe a quantidade: '))
                gerar_contas(quantidade)
                print(cs(f'-------> FORAM GERADAS {quantidade} CONTAS COM SUCESSO <-------\n', 'green').bold())
                break
            else:
                print(cs(f'-------> SISTEMA INICIALIZADO SEM CONTAS CADASTRADAS <-------\n', 'green').bold())
                break
        else:
            print(cs('-------> MODO CLIENTE: \n', 'yellow').bold() +
                  '\n>> GERANDO CONTAS TESTES PARA OS TESTES DE TRANSFERÊNCIA!\n')
            gerar_contas(3)
            sleep(1)
            print(cs('-------> FORAM GERADAS 3 CONTAS COM SUCESSO <-------\n', 'green').bold())
            break


# ------------------------------------------------------ MENU ----------------------------------------------------------
def menu() -> None:
    """Menu de opções
    CLIENTES: podem ter acesso as opções que dizem respeito a própria conta
    ADMINISTRADORES: podem criar e acessar contas e realizar qualquer operação"""
    if admin == 2:
        print(cs('\n>>> Selecione uma opção através do código numérico:\n', 'yellow').bold() +
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
        print(cs('\n>>> Selecione uma opção através do código numérico:\n', 'yellow').bold() +
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
            print(cs('----------------- SISTEMA FECHANDO -----------------', 'yellow').bold())
            sleep(1)
            print(cs('----------------------- FIM ------------------------', 'yellow').bold())
            exit(0)
    elif escolha == 7 and admin == 2:
        pagar_fatura()
    elif escolha == 8 and admin == 2:
        print(cs('----------------- SISTEMA FECHANDO -----------------', 'yellow').bold())
        sleep(1)
        print(cs('----------------------- FIM ------------------------', 'yellow').bold())
        exit(0)
    else:
        print(cs('>>> ERRO: OPÇÃO INVÁLIDA, TENTE NOVAMENTE! <<<', 'red').bold())
        sleep(1)
        menu()


# --------------------------------------------- FUNÇÕES DO MENU --------------------------------------------------------
def criar_conta() -> None:
    """Cria um objeto do tipo Cliente e um objeto do tipo Conta"""
    print(cs('\n-------------------------- Criando conta --------------------------', 'yellow').bold())
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
        print(cs('---- CONTA CADASTRADA COM SUCESSO\n', 'green').bold())
        print(cliente)
        print(conta)
        sleep(1)
        menu()
    except:
        print(cs('### OCORREU ALGUM ERRO ###', 'red').bold())
        sleep(1)
        criar_conta()


def efetuar_saque() -> None:
    """Chama a função sacar()
    CLIENTES: só podem sacar da própria conta
    ADMINISTRADORES: podem sacar de qualquer conta"""
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
                    print(cs('### VOCÊ SÓ PODE SACAR DA SUA CONTA ###', 'red').bold())
                    print(cs(f'### O NÚMERO DA SUA CONTA É {numero_sua_conta} ###', 'red').bold())
                    sleep(1)
                    menu()
            if admin == 2:
                valor: float = float(input('>>> Informe o valor do saque: '))
                conta.sacar(valor)
                sleep(1)
                menu()
        else:
            print(cs(f'Não foi encontrada a conta com número: {numero}', 'red').bold())
            sleep(1)
            menu()

    else:
        print(cs('### Ainda não existem contas cadastradas ###', 'red').bold())
        sleep(1)
        menu()


def efetuar_deposito() -> None:
    """Chama a função depositar() e tem permissões iguais para CLIENTES e ADMINISTRADORES"""
    if len(contas) > 0:
        numero: int = int(input('>>> Informe o código da conta: '))
        conta: Conta = buscar_conta_por_codigo(numero)

        if conta:
            valor: float = float(input('>>> Informe o valor de depósito: '))
            conta.depositar(valor)
            sleep(1)
            menu()
        else:
            print(cs(f'Não foi encontrada a conta com número: {numero}', 'red').bold())
            sleep(1)
            menu()

    else:
        print(cs('### Ainda não existem contas cadastradas ###', 'red').bold())
        sleep(1)
        menu()


def efetuar_transferencia() -> None:
    """Chama a função transferir()
    CLIENTES: só podem transferir da própria conta para uma conta destino
    ADMINISTRADOS: podem transferir de qualquer conta para qualquer conta"""
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
                        print(cs('### CONTA DESTINO NÃO EXISTE ###', 'red').bold())
                        sleep(1)
                        menu()
                else:
                    print(cs('### VOCÊ SÓ PODE TRANSFERIR DA SUA CONTA ###', 'red').bold())
                    print(cs(f'### O NÚMERO DA SUA CONTA É {numero_sua_conta} ###', 'red').bold())
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
                    print(cs('### CONTA DESTINO NÃO EXISTE ###', 'red').bold())
                    sleep(1)
                    menu()
        else:
            print(cs('### A CONTA INFORMADA NAO EXISTE ###', 'red').bold())
            sleep(1)
            menu()
    else:
        print(cs('### Ainda não existem contas cadastradas ###', 'red').bold())
        sleep(1)
        menu()


def aumentar_limite() -> None:
    """Chama a função altera_limite() e passa os parâmetros definidos pelo usuário
    CLIENTES: Só podem aumentar o limite da própria conta e se a fatura estiver zerada
    ADMINISTRADOS: Podem aumentar o limite de qualquer conta a qualquer momento"""
    if len(contas) > 0:
        numero: int = int(input('>>> Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_codigo(numero)

        if conta:
            if admin == 1:
                if (-1 * conta.fatura) == 0:
                    if numero == numero_sua_conta:
                        valor: float = float(input('>>> Informe o valor desejado: '))
                        conta.altera_limite(valor)
                        sleep(1)
                        menu()
                    else:
                        print(cs('### VOCÊ SÓ PODE AUMENTAR O LIMITE DA SUA CONTA ###', 'red').bold())
                        print(cs(f'### O NÚMERO DA SUA CONTA É {numero_sua_conta} ###', 'red').bold())
                        sleep(1)
                        menu()
            else:
                print(cs('### LIMITE NÃO PÔDE SER ALTERADO, PAGUE A FATURA ###', 'red').bold())
            if admin == 2:
                valor: float = float(input('>>> Informe o valor desejado: '))
                conta.altera_limite(valor)
                sleep(1)
                menu()
        else:
            print(cs(f'Não foi encontrada a conta com número: {numero}', 'red').bold())
            sleep(1)
            menu()
    else:
        print(cs('### Ainda não existem contas cadastradas ###', 'red').bold())
        sleep(1)
        menu()


def pagar_fatura() -> None:
    """Chama a função pagar_fatura() do objeto conta
    MODO CLIENTE: o usuário só poderá pagar a própria fatura
    DMINISTRADORES: podem pagar qualquer fatura"""
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
                    print(cs('### VOCÊ SÓ PODE PAGAR A FATURA DA SUA CONTA ###', 'red').bold())
                    print(cs(f'### O NÚMERO DA SUA CONTA É {numero_sua_conta} ###', 'red').bold())
                    sleep(1)
                    menu()
            if admin == 2:
                conta.pagar_fatura()
                sleep(1)
                menu()
        else:
            print(cs(f'Não foi encontrada a conta com número: {numero}', 'red').bold())
            sleep(1)
            menu()
    else:
        print(cs('### Ainda não existem contas cadastradas ###', 'red').bold())
        sleep(1)
        menu()


def ver_conta() -> None:
    """Mostra a conta de acordo com o número inserido
    Somente ADMINISTRADORES podem ver todas as contas"""
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
                    print(cs('### VOCÊ SÓ PODE VER A SUA CONTA ###', 'red').bold())
                    print(cs(f'### O NÚMERO DA SUA CONTA É {numero_sua_conta} ###', 'red').bold())
                    sleep(1)
                    menu()
            if admin == 2:
                print('')
                print(conta)
                sleep(1)
                menu()
        else:
            print(cs(f'Não foi encontrada a conta com número: {numero}', 'red').bold())
            sleep(1)
            menu()

    else:
        print(cs('### Ainda não existem contas cadastradas ###', 'red').bold())
        sleep(1)
        menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print(cs('--------------- LISTAGEM DE CONTAS ---------------', 'yellow').bold())
        for conta in contas:
            print(conta)
            print('---------------------------------')
            sleep(1)
        menu()
    else:
        print(cs('### Ainda não existem contas cadastradas ###', 'red').bold())
        sleep(1)
        menu()


def buscar_conta_por_codigo(codigo: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == codigo:
                c = conta
    return c


# ------------------------------------------ GERADORES DE DADOS/CONTAS -------------------------------------------------
def gerar_dados():
    """Gera valores para as varieveis que serão passadas como atributos em gerar_contas()"""
    nome = choice(['Marcelo', 'Maria', 'Rodolfo', 'Amanda', 'Gabriela',
                   'Manoel', 'Sabrina', 'Daniel', 'Bruna', 'Julio'])
    email = choice(['@gmail.com', '@yahoo.com', '@outlook.com'])
    email_completo = f'{nome.lower()}{email}'
    cpf = f'{randint(100, 999)}' + f'.{randint(000, 999)}' + f'.{randint(000, 999)}' + f'-{randint(00, 99)}'
    data = f'{randint(10, 30)}/{randint(10, 12)}/{randint(1960, 1990)}'
    return nome, email_completo, cpf, data


def gerar_contas(quant: int):
    """Gera a quantidade de objetos do tipo Cliente
     e objetos do tipo Conta que o usuário informar"""
    for x in range(quant):
        nome, email, cpf, data = gerar_dados()
        gc_cliente = Cliente(nome, email, cpf, data)
        print(gc_cliente)
        sleep(1)
        gc_conta = Conta(gc_cliente)
        print(gc_conta)
        contas.append(gc_conta)
        sleep(1)


# ---------------------------------------------- EXECUTA A APLICAÇÃO ---------------------------------------------------
if __name__ == '__main__':
    main()
