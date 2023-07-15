import contas
import pessoa


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoa.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta in cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoa.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r}, )'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = pessoa.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoa.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    c3 = pessoa.Cliente('Ian', 24)
    cc3 = contas.ContaCorrente(333, 1000, 500, 3000)
    c3.conta = cc3
    banco = Banco()
    banco.clientes.extend([c1, c2, c3])
    banco.contas.extend([cc1, cp1, cc3])
    banco.agencias.extend([111, 222, 333])

    if banco.autenticar(c3, cc3):
        cc3.depositar(100)
        c3.conta.depositar(1000)
        c3.conta.sacar(5000)
        print(c3.conta)
