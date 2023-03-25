from SerVivo import SerVivo

class Monstro(SerVivo):
    def __init__(self, pontosDeVida, pontosDeAtaque, tipoMonstro):
        super().__init__(pontosDeVida, pontosDeAtaque)
        self.tipoMonstro = tipoMonstro