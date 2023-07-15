class carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class motor:
    def __init__(self, nome):
        self.nome = nome


class fabricante:
    def __init__(self, nome):
        self.nome = nome


fusion = carro('Fusion')
ford = fabricante('Ford')
motor_2_0 = motor('2.0')
fusion.fabricante = ford
fusion.motor = motor_2_0
print(fusion.nome, fusion.fabricante.nome, fusion.motor.nome)

gtr = carro('GTR R35')
nissan = fabricante('Nissan')
motor_v6 = motor('Motor V6')
gtr.fabricante = nissan
gtr.motor = motor_v6
print(gtr.nome, gtr.fabricante.nome, gtr.motor.nome)
