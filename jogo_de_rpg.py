class SerVivo:
    def __init__(self, pontosDeVida, pontosDeAtaque):
        self.pontosDeVida = pontosDeVida
        self.pontosDeAtaque = pontosDeAtaque

    def Ataque(self, ser_vivo_atacado):
        ser_vivo_atacado.pontosDeVida = ser_vivo_atacado.pontosDeVida-self.pontosDeAtaque
        print("O atacante causou ",self.pontosDeAtaque, " de dano no ser vivo atacado")
        print(f"A vida do ser vivo atacado ficou em", ser_vivo_atacado.pontosDeVida)

class Personagem(SerVivo):
    def __init__(self, pontosDeVida, pontosDeAtaque, nome):
        super().__init__(pontosDeVida, pontosDeAtaque)
        self.nome = nome

    def MostrarDadosPersonagem(self):
        print("O nome do personagem é:",self.nome, "\nPontos de vida: ",self.pontosDeVida,"\nPontos de ataque: ",self.pontosDeAtaque)
        
class Monstro(SerVivo):
    def __init__(self, pontosDeVida, pontosDeAtaque, tipoMonstro):
        super().__init__(pontosDeVida, pontosDeAtaque)
        self.tipoMonstro = tipoMonstro

class Goblin(Monstro):
    def __init__(self, pontosDeVida, pontosDeAtaque, tipoMonstro, inteligencia):
        super().__init__(pontosDeVida, pontosDeAtaque,tipoMonstro)
        self.inteligencia = inteligencia

    def MostrarDadosGoblin(self):
        print("\nO tipo de monstro é:",self.tipoMonstro,"\nPontos de vida: ",self.pontosDeVida,"\nPontos de ataque: ",self.pontosDeAtaque,"\nO nível de inteligência é: ",self.inteligencia)

class Lobo(Monstro):
    def __init__(self, pontosDeVida, pontosDeAtaque, tipoMonstro, forca):
        super().__init__(pontosDeVida, pontosDeAtaque,tipoMonstro)
        self.forca = forca

    def MostrarDadosLobo(self):
        print("\nO tipo de monstro é:",self.tipoMonstro,"\nPontos de vida: ",self.pontosDeVida,"\nPontos de ataque: ",self.pontosDeAtaque,"\nO nível de força é: ",self.forca)

Personagem1 = Personagem(50, 10, "Personagem-1")
Personagem1.MostrarDadosPersonagem()

Goblin1 = Goblin(50,10,"Goblin-1",2)
Goblin1.MostrarDadosGoblin()
Goblin1.Ataque(Personagem1)

Lobo1 = Lobo(100,20,"Lobo-1",10)
Lobo1.MostrarDadosLobo()
Lobo1.Ataque(Personagem1)