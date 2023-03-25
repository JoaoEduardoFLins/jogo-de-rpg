from Monstro import Monstro

class Goblin(Monstro):
    def __init__(self, pontosDeVida, pontosDeAtaque, tipoMonstro, inteligencia):
        super().__init__(pontosDeVida, pontosDeAtaque,tipoMonstro)
        self.inteligencia = inteligencia

    def MostrarDadosGoblin(self):
        print("\nO tipo de monstro é:",self.tipoMonstro,"\nPontos de vida: ",self.pontosDeVida,"\nPontos de ataque: ",self.pontosDeAtaque,"\nO nível de inteligência é: ",self.inteligencia)
        