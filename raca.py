class Raca:
    def __init__(self, movimento, infravisao, alinhamento, habilidades):
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = habilidades

class Humano(Raca):
    def __init__(self):
        super().__init__(movimento=9, infravisao=False, alinhamento="Qualquer", habilidades=["Versatilidade"])

class Anao(Raca):
    def __init__(self):
        super().__init__(movimento=6, infravisao=True, alinhamento="Leal", habilidades=["Resistência", "Conhecimento sobre pedras"])

class Elfo(Raca):
    def __init__(self):
        super().__init__(movimento=12, infravisao=True, alinhamento="Neutro", habilidades=["Visão aguçada", "Resistência a encantos"])
