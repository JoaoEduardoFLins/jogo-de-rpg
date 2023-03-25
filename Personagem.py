from SerVivo import SerVivo

class Personagem(SerVivo):
    def __init__(self, pontosDeVida, pontosDeAtaque, nome):
        super().__init__(pontosDeVida, pontosDeAtaque)
        self.nome = nome

    def MostrarDadosPersonagem(self):
        print("\nO nome do personagem é:",self.nome, "\nPontos de vida: ",self.pontosDeVida,"\nPontos de ataque: ",self.pontosDeAtaque)