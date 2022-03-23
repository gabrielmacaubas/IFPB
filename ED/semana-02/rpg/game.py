class SuporteNaoDaDano(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Personagem:
    MAGO = 1
    TANK = 2
    GUERREIRO = 3
    SUPORTE = 4

    def __init__(self, nome: str, 
                tipo: int = GUERREIRO):
        self.nome = nome
        self.vida = 100
        self.stamina = 100
        self.tipo = tipo
    
    def __str__(self) -> str:
        return f'Personagem("{self.nome}")'
    
    def atacar(self, outro_personagem):
        if self.tipo == Personagem.SUPORTE:
            raise SuporteNaoDaDano("Suporte não dá dano")

        self.perder_stamina(10)
        forca = self._get_dano_terceiros()
        outro_personagem.sofrer_ataque(forca)
    
    def _get_dano_terceiros(self):
        tabela_dano = {
            Personagem.MAGO: 2,
            Personagem.SUPORTE: 1,
            Personagem.GUERREIRO: 15,
            Personagem.TANK: 10
        }
        return tabela_dano[self.tipo]

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

    def estah_vivo(self):
        if self.vida > 0:
            return "Vivo"
        else:
            return "Morto"
