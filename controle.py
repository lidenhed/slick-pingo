from texto import *
import sys

class Controle:
    def __init__(self):
        self.__livros = []
        self.__opcao = 0
    
    @property
    def livros(self):
        return self.__livros

    def iniciaLivro(self, nome, texto = None):
        livro = Livro(nome)
        self.__livros.append(livro)
        return livro

    def encontraLivro(self, nome):
        for livro in self.__livros:
            if livro.nome.lower() == nome.lower():
                return livro

    def importaTexto(self, caminho):
        conteudo = ''
        textoTratado = ''
        with open(caminho, 'r') as arquivo:
            conteudo = arquivo.readline()
            while conteudo:
                primeiraParte = ''
                i = 0
                while i < len(conteudo) and conteudo[i] != ' ':
                    primeiraParte += conteudo[i]
                    i += 1
                try:
                    int(primeiraParte)
                    textoTratado += conteudo[i+1:]
                except:
                    textoTratado += conteudo
                finally:
                    conteudo = arquivo.readline()
        return textoTratado


    # def heuristicaQtdLetras(self, palavraBuscada, palavraComparada):
    #     buscada = palavraBuscada.lower()
    #     comparada = palavraComparada.lower()
    #     registro = []
    #     valor = 0
    #     for letra in comparada:
    #         if not letra in registro:
    #             registro.append(letra)
    #             valor += buscada.count(letra)
    #     return valor / (len(buscada) * (1/9 * abs(len(buscada) - len(comparada))**2 +1))
    
    def heuristicaQtdLetras(self, palavraBuscada, palavraComparada):
        buscada = palavraBuscada.lower()
        comparada = palavraComparada.lower()
        registro = []
        valor = 0
        for letra in comparada:
            if letra not in registro:
                registro.append(letra)
                x = (buscada.count(letra) / comparada.count(letra))
                if x == 0:
                    x = comparada.count(letra) * 1.5
                valor += 1 + (1 - x)**2 / x
        return len(registro) / valor


    # def heuristicaPosicaoLetras(self, palavraBuscada, palavraComparada):
    #     buscada = palavraBuscada.lower()
    #     comparada = palavraComparada.lower()
    #     registro = {}
    #     i = 0
    #     valor = 0
    #     while i < len(buscada):
    #         if not registro.get(buscada[i]):
    #             registro.update({buscada[i]: []})
    #         j = 0
    #         while j < len(comparada):
    #             if buscada[i] == comparada[j]:
    #                 if not j in registro.get(buscada[i]):
    #                     registro.get(buscada[i]).append(j)
    #                     valor += 500 * (1 / (((i - j) ** 2) + 1))
    #                     j = len(comparada)
    #                 else:
    #                     j += 1
    #             else:
    #                 j += 1
    #         i += 1
    #     return valor
    # sorted()


    def heuristicaPosicaoLetras(self, palavraBuscada, palavraComparada):
        registro = {}
        valor = 0
        for i in range(len(palavraComparada)):
            if not registro.get(palavraComparada[i]):
                registro.update({palavraComparada[i]: []})
            for j in range(len(palavraBuscada)):
                if palavraBuscada[j] == palavraComparada[i]:
                    registro.get(palavraComparada[i]).append((i, j))
        for v in registro.values():
            a = sorted(v, key = lambda a: abs(a[0]-a[1]))
            removidos = []
            while len(a) > 0:
                b = a.pop(0)
                if b[0] not in removidos:
                    removidos.append(b[0])
                    valor += 500 * (1 / (((b[0] - b[1]) ** 2) + 1))
        return valor / (len(palavraComparada)*500)


    def buscaHeuristica(self, palavraBuscada, palavraComparada):
        p1 = self.heuristicaPosicaoLetras(palavraBuscada, palavraComparada)
        p2 = self.heuristicaQtdLetras(palavraBuscada, palavraComparada)
        return (p1 + p2) / 2

    def busca(self, palavraBuscada):
        match = []
        for livro in self.__livros:
            palavras = livro.retornaCapitulos().split()
            for palavra in palavras:
                if self.buscaHeuristica(palavraBuscada, palavra) >= 0.7:
                    match.append(palavra)
        return sorted(match)



