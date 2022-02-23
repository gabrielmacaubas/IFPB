
class Personagem:

    def __init__(self, nome: str):
        self.nome = nome
        self.vida = 100
        self.stamina = 100
        self.vivo = "Vivo"
    
    def __str__(self):
        return f'Personagem("{self.nome}")'
    
    def atacar(self, outro_personagem):
        self.perder_stamina(10)
        outro_personagem.sofrer_ataque(forca=15)
    
    def sofrer_ataque(self, forca):
        self.modificar_vida(-forca)

    def perder_stamina(self, quantidade):
        self.stamina -= quantidade
    
    def modificar_vida(self, quantidade: int):
        if self.vida + quantidade > 100:
            self.vida = 100
        elif self.vida + quantidade < 0:
            self.vida = 0
        else: self.vida += quantidade 
        self.estah_vivo()

    def estah_vivo(self):
        if self.vida > 0:
            self.vivo = "Vivo"
        else:
            self.vivo = "Morto"
