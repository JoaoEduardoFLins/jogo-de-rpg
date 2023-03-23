class SerVivo:
    def __init__(self, pontosDeVida, pontosDeAtaque):
        self.pontosDeVida = pontosDeVida
        self.pontosDeAtaque = pontosDeAtaque

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

    def AtaqueGoblin(self,Personagem):
        print("O dano do goblin no Personagem:",Personagem.nome," foi",self.pontosDeAtaque)
        Personagem.pontosDeVida=Personagem.pontosDeVida-self.pontosDeAtaque
        print("A vida do personagem caiu para:",Personagem.pontosDeVida)

class Lobo(Monstro):
    def __init__(self, pontosDeVida, pontosDeAtaque, tipoMonstro, forca):
        super().__init__(pontosDeVida, pontosDeAtaque,tipoMonstro)
        self.forca = forca

    def MostrarDadosLobo(self):
        print("\nO tipo de monstro é:",self.tipoMonstro,"\nPontos de vida: ",self.pontosDeVida,"\nPontos de ataque: ",self.pontosDeAtaque,"\nO nível de força é: ",self.forca)

    def AtaqueLobo(self,Personagem):
        print("O dano do lobo no Personagem:",Personagem.nome," foi",self.pontosDeAtaque)
        Personagem.pontosDeVida=Personagem.pontosDeVida-self.pontosDeAtaque
        print("A vida do personagem caiu para:",Personagem.pontosDeVida)
        
Personagem1 = Personagem(50, 10, "Personagem-1")
Personagem1.MostrarDadosPersonagem()

Goblin1 = Goblin(50,10,"Goblin-1",2)
Goblin1.MostrarDadosGoblin()
Goblin1.AtaqueGoblin(Personagem1)

Lobo1 = Lobo(100,20,"Lobo-1",10)
Lobo1.MostrarDadosLobo()
Lobo1.AtaqueLobo(Personagem1)