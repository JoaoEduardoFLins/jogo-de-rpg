class SerVivo:
    def __init__(self, pontosDeVida, pontosDeAtaque):
        self.pontosDeVida = pontosDeVida
        self.pontosDeAtaque = pontosDeAtaque

    def Ataque(self, ser_vivo_atacado):
        ser_vivo_atacado.pontosDeVida = ser_vivo_atacado.pontosDeVida-self.pontosDeAtaque
        print("\nO atacante causou ",self.pontosDeAtaque, " de dano no ser vivo atacado")
        print(f"A vida do ser vivo atacado ficou em", ser_vivo_atacado.pontosDeVida)