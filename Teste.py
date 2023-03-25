from SerVivo import SerVivo
from Monstro import Monstro
from Personagem import Personagem
from Monstro import Monstro
from Goblin import Goblin
from Lobo import Lobo

Personagem1 = Personagem(50, 10, "Personagem-1")
Personagem1.MostrarDadosPersonagem()

Goblin1 = Goblin(50,10,"Goblin-1",2)
Goblin1.MostrarDadosGoblin()
Goblin1.Ataque(Personagem1)

Lobo1 = Lobo(100,20,"Lobo-1",10)
Lobo1.MostrarDadosLobo()
Lobo1.Ataque(Personagem1)