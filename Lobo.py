from Monstro import Monstro

class Lobo(Monstro):
    def __init__(self, pontosDeVida, pontosDeAtaque, tipoMonstro, forca):
        super().__init__(pontosDeVida, pontosDeAtaque,tipoMonstro)
        self.forca = forca

    def MostrarDadosLobo(self):
        print("\nO tipo de monstro é:",self.tipoMonstro,"\nPontos de vida: ",self.pontosDeVida,"\nPontos de ataque: ",self.pontosDeAtaque,"\nO nível de força é: ",self.forca)
        