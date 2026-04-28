class Versiculo:
    def __init__(self, numero, texto):
        self.numero = numero
        self.texto = texto


class Capitulo:
    def __init__(self, numero):
        self.numero = numero
        self.versiculos = []

    def adicionar_versiculo(self, versiculo):
        self.versiculos.append(versiculo)


class Livro:
    def __init__(self, nome):
        self.nome = nome
        self.capitulos = []
        self.anotacoes = ""

    def adicionar_capitulo(self, capitulo):
        self.capitulos.append(capitulo)

    def get_capitulo(self, numero):
        for c in self.capitulos:
            if c.numero == numero:
                return c

    def get_texto(self):
        texto = ""
        for cap in self.capitulos:
            texto += f"\nCapítulo {cap.numero}\n"
            for v in cap.versiculos:
                texto += f"{v.numero} {v.texto}\n"
        return texto