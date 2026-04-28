import json
from m import *
from tela import *


class Controller:
    def __init__(self, view):
        self.view = view
        self.livros = self.carregar_livros()
        self.carregar_anotacoes()
        self.view.on_busca = self.buscar
        self.view.trocar_tela(TelaInicial, self)

    def abrir_livro(self, livro):
        self.livro_atual = livro
        self.view.trocar_tela(TelaLivro, self, livro)

    def buscar(self, termo):
        if not termo:
            return

        if hasattr(self.view, "tela_atual") and isinstance(self.view.tela_atual, TelaLivro):
            self.view.tela_atual.destacar(termo)
            return

        resultados = []
        for livro in self.livros:
            if termo.lower() in livro.get_texto().lower():
                resultados.append(livro.nome)

        texto = "\n".join(resultados) or "Nada encontrado"
        self.view.trocar_tela(TelaBusca, texto)

    def salvar_anotacoes(self, livro, texto):
        livro.anotacoes = texto
        self.salvar_persistencia()

    def salvar_persistencia(self):
        data = {l.nome: l.anotacoes for l in self.livros}
        with open("data/anotacoes.json", "w") as f:
            json.dump(data, f)

    def carregar_anotacoes(self):
        try:
            with open("data/anotacoes.json", "r") as f:
                data = json.load(f)
                for l in self.livros:
                    if l.nome in data:
                        l.anotacoes = data[l.nome]
        except:
            pass

    def carregar_livros(self):
        livros = []

        for i in range(66):
            livro = Livro(f"Livro {i+1}")

            for c in range(1, 4):
                cap = Capitulo(c)
                for v in range(1, 6):
                    cap.adicionar_versiculo(Versiculo(v, f"Texto {v}"))
                livro.adicionar_capitulo(cap)

            livros.append(livro)

        return livros

    def voltar_inicio(self):
        self.view.trocar_tela(TelaInicial, self)