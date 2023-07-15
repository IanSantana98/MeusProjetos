import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO DE {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print(' ')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_apos_saque = self.saldo - valor

        if valor_apos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE DE {valor})')
            return self.saldo

        print('Não foi possivel efetuar o saque')
        print(' ')
        self.detalhes(f'(SAQUE DE {valor} NEGADO)')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(
        self, agencia: int, conta: int,
        saldo: float = 0, limite: float = 0
    ):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_apos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_apos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE DE {valor})')
            return self.saldo

        print('Não foi possivel efetuar o saque')
        print(' ')
        print(f'Seu limite é de {self.limite:.2f}')
        print(' ')
        self.detalhes(f'(SAQUE DE {valor} NEGADO)')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 200)
    cp1.sacar(100)
    cp1.depositar(100)
    cp1.sacar(50)
    print('--------------')
    print(' ')
    cc1 = ContaCorrente(112, 223, 50, 1000)
    cc1.sacar(100)
    cc1.depositar(100)
    cc1.sacar(50)
    cc1.sacar(1001)
    cc1.sacar(132)
