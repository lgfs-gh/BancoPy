from models.cliente import Cliente
from utils.helper import formata_moeda


class Conta:
    codigo = 100

    def __init__(self: object, cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0
        self.__limite: float = 100
        self.__limite_max: float = 100
        self.__fatura: float = 0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self: object) -> str:
        return f'Número da conta: {self.numero}\n' \
               f'Cliente: {self.cliente.nome}\n' \
               f'Saldo Atual: {self.saldo}\n' \
               f'Limite: {self.limite}\n' \
               f'Saldo Total: {formata_moeda(self.saldo_total)}\n' \
               f'Fatura: {(formata_moeda(-1 * self.fatura))}\n'

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def limite_max(self: object) -> float:
        return self.__limite_max

    @limite_max.setter
    def limite_max(self: object, valor: float) -> None:
        self.__limite_max = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor) -> None:
        self.__saldo_total = valor

    @property
    def fatura(self: object) -> float:
        return self.__fatura

    @fatura.setter
    def fatura(self: object, valor) -> None:
        self.__fatura = valor

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print('-------- DEPOSITO EFETUADO COM SUCESSO --------')
        else:
            print('### ERRO: TENTE NOVAMENTE ###')

    def sacar(self: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                print('-------- SAQUE EFETUADO COM SUCESSO --------')
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.fatura = self.fatura - (self.limite_max - self.limite)
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
                print('-------- SAQUE EFETUADO COM SUCESSO --------')
        else:
            print('### ERRO: TENTE NOVAMENTE ###')

    def transferir(self: object, destino: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
                print('-------- TRANSFERENCIA EFETUADA COM SUCESSO --------')
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.fatura = self.fatura - (self.limite_max - self.limite)
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
                print('-------- TRANSFERENCIA EFETUADA COM SUCESSO --------')
        else:
            print('### ERRO: TENTE NOVAMENTE ###')

    def altera_limite(self: object, valor) -> None:
        if valor > 0 and valor > self.limite_max:
            self.limite_max = valor
            print('-------- LIMITE ALTERADO COM SUCESSO --------')
        else:
            print('### VALOR DEVE SER DIFERENTE DE ZERO E ACIMA DO LIMITE ATUAL ###')

    def pagar_fatura(self):
        if self.saldo >= (-1 * self.fatura):
            self.saldo = self.saldo + self.fatura
            self.fatura = 0
            self.limite = self.limite_max
            self.saldo_total = self._calcula_saldo_total
            print('-------- FATURA PAGA COM SUCESSO / LIMITE RESTAURADO --------')
        else:
            print('### ERRO: SALDO INSUFICIENTE ###')
