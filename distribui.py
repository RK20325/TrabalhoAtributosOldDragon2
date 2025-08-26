import random

class Distribuidor:
    def distribuir(self):
        raise NotImplementedError

class Classico(Distribuidor):
    def distribuir(self):
        atributos = []
        for _ in range(6):
            rolagens = [random.randint(1, 6) for _ in range(3)]
            atributos.append(sum(rolagens))
        return atributos

class Heroico(Distribuidor):
    def distribuir(self):
        valores = [15, 14, 13, 12, 10, 8]
        escolha = input("Deseja embaralhar os valores heroicos antes de atribuir? (s/n): ").lower()
        if escolha == "s":
            random.shuffle(valores)
        return valores

class Aventureiro(Distribuidor):
    def distribuir(self):
        atributos = []
        for _ in range(6):
            rolagens = sorted([random.randint(1, 6) for _ in range(4)], reverse=True)
            atributos.append(sum(rolagens[:3]))
        return atributos
