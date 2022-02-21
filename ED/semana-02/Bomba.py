class Visor:
    def __init__(self, preço_do_combustivel, nome_combustivel):
        self.nome_combustivel = nome_combustivel
        self.preço_combustivel = preço_do_combustivel
        self.quant_litros = 0.0
        self.valor_a_pagar = 0.0

    def reset(self):
        self.quant_litros = 0.0
        self.valor_a_pagar = 0.0

    def __str__(self): # método quq exige que uma string seja retornada
        return f'''
    Combustivel: {self.nome_combustivel}
    Preço: {self.preço_combustivel} 
    Quantidade de Litros: {self.quant_litros}     
    Total a pagar: {self.valor_a_pagar} 
    '''



class BombaDeCombustivel:
    ALCOOL = 1   # Propriedade de Classe
    GASOLINA = 2 # Propriedade de Classe
    def __init__(self, preço_da_gasolina:float, preço_do_alcool:float):
        self.preço_gasolina = preço_da_gasolina
        self.preço_alcool = preço_do_alcool
        self.ligada = True

        self.visor_alcool = Visor(self.preço_alcool, 'ALCOOL')
        self.visor_gasolina = Visor(self.preço_gasolina, 'GASOLINA')

    def abastercer(self):
        pass

    def zerarBomba(self, tipo_combustivel):
        if tipo_combustivel == BombaDeCombustivel.GASOLINA:
            self.visor_gasolina.reset()
        # elif tipo_combustivel



    def alterarPreçoGasolina(self, novoPreço:float):
        if novoPreço > 0:
            self.preço_gasolina = novoPreço

    def alterarPreçoAlcool(self, novoPreço:float):
        if novoPreço > 0:
            self.preço_alcool = novoPreço

    def mostrarVisor(self):
        pass

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def info(self):
        return 'Bomba de Combustivel'







