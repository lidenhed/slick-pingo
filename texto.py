class Versiculo:
    def __init__(self, texto, numero = 0):
        if len(texto) == 0:
            raise ValueError('Necessário texto para criar um versículo.')
        else:
            self.__texto = texto
        self.__numero = numero

    def __str__(self):
        return f"{self.__numero} {self.__texto}"
    
    def __repr__(self):
        return f"Versiculo({self.__texto}, {self.__numero})"

    def numeroPalavras(self):
        palavras = [palavra for palavra in self.__texto.split(" ") if len(palavra) > 0]
        return len(palavras)

class Capitulo:
    def __init__(self, texto, numero = 0):
        self.__versiculos = []
        self.__numero = numero
        versiculos = texto.split("\n")
        for versiculo in versiculos:
            self.__versiculos.append(Versiculo(versiculo, versiculos.index(versiculo) + 1))

    def adicionaVersiculo(self, texto, numero):
        versiculo = Versiculo(texto, numero)
        self.__versiculos.insert(numero - 1, versiculo)

    @property
    def numero(self):
        return self.__numero
    
    @property
    def versiculos(self):
        return self.__versiculos

    @numero.setter
    def numero(self, valor):
        self.__numero = valor
    
    def __str__(self):
        return f'Capítulo {self.numero}'


class Livro:
    def __init__(self, nome, texto = None):
        self.__nome = nome.capitalize()
        self.__capitulos = []
        self.__numeroCapitulos = 0
    
    def criaCapitulo(self, texto, numero = None):
        if len(texto) > 0:
            numero = self.__numeroCapitulos + 1 if not numero else numero
            self.__capitulos.append(Capitulo(texto, numero))
            self.__capitulos.sort(key = lambda capitulo: capitulo.numero)
            self.__numeroCapitulos += 1
        else:
            raise ValueError(('Para criar um Capítulo é necessário um texto'))
    
    @property
    def nome(self):
        return self.__nome

    @property
    def capitulos(self):
        return self.__capitulos
    
    def imprimeCapitulo(self, numero):
        for versiculo in self.__capitulos[numero-1].versiculos:
            print(versiculo)
    
    def imprimeCapitulos(self):
        for capitulo in self.__capitulos:
            print(capitulo)
            self.imprimeCapitulo(self.__capitulos.index(capitulo))

    
    def retornaCapitulos(self):
        texto = ''
        for capitulo in self.__capitulos:
            for versiculo in capitulo.versiculos:
                texto += str(versiculo) + '\n'
        return texto

