class Calculadora:

    def __init__(self):
        self.registrador = [float(), float()]
        self.operacao = str()
        self.valor = float()

    def reset(self):
        self.registrador = [float(), float()]

    def __str__(self):
        return f"""+{'-' * 14}+
|{self.registrador[1]:>14.2f}|
+{'-' * 14}+"""

    def calcular(self):
        if self.operacao == "+":
            self.somar()

        elif self.operacao == "-":
            self.subtrair()

        elif self.operacao == "/":
            self.dividir()

        elif self.operacao == "*":
            self.multiplicar()

        elif self.operacao == "r":
            self.reset()

        elif self.operacao == "d":
            self.desfazer()

        else:
            print("\nOPERAÇÃO INVÁLIDA")

    def somar(self):
        self.registrador[0] = self.registrador[1]
        self.registrador[1] += self.valor

    def subtrair(self):
        self.registrador[0] = self.registrador[1]
        self.registrador[1] -= self.valor

    def dividir(self):
        self.registrador[0] = self.registrador[1]
        self.registrador[1] /= self.valor

    def multiplicar(self):
        self.registrador[0] = self.registrador[1]
        self.registrador[1] *= self.valor

    def desfazer(self):
        self.registrador[1] = self.registrador[0]
