from models.cliente import Cliente
from models.conta import Conta

c1: Cliente = Cliente('NomeTeste', 'teste@gmail.com', '134.567.890-94', '10/10/1960')
c2: Cliente = Cliente('Testando', 'testando@yahoo.com', '435.353.600-44', '06/07/1977')

print('\n--------------- TESTANDO CLASSE CLIENTE -------------------\n')
print(c1)
print(c2)

conta1: Conta = Conta(c1)
conta2: Conta = Conta(c2)

print('--------------- TESTANDO CLASSE CONTA -------------------\n')
print(conta1)
print(conta2)