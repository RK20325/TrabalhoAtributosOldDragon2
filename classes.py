class ClassePersonagem:
    def __init__(self, nome, dado_vida, habilidades):
        self.nome = nome
        self.dado_vida = dado_vida
        self.habilidades = habilidades

class Guerreiro(ClassePersonagem):
    def __init__(self):
        super().__init__(nome="Guerreiro", dado_vida="1d8", habilidades=["Ataque poderoso", "Armadura pesada"])

class Mago(ClassePersonagem):
    def __init__(self):
        super().__init__(nome="Mago", dado_vida="1d4", habilidades=["Magia arcana", "Conhecimento"])

class Ladino(ClassePersonagem):
    def __init__(self):
        super().__init__(nome="Ladino", dado_vida="1d6", habilidades=["Furtividade", "Ataque furtivo"])
