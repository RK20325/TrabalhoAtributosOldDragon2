class Personagem:
    def __init__(self, nome, atributos, raca, classe):
        self.nome = nome
        self.atributos = atributos
        self.raca = raca
        self.classe = classe

    def exibir(self):
        print(f"\nPersonagem: {self.nome}")
        print(f"Atributos: {self.atributos}")
        print(f"Raça: {self.raca.__class__.__name__}")
        print(f"  Movimento: {self.raca.movimento}")
        print(f"  Infravisão: {self.raca.infravisao}")
        print(f"  Alinhamento: {self.raca.alinhamento}")
        print(f"  Habilidades: {', '.join(self.raca.habilidades)}")
        print(f"Classe: {self.classe.nome}")
        print(f"  Dado de Vida: {self.classe.dado_vida}")
        print(f"  Habilidades: {', '.join(self.classe.habilidades)}")
