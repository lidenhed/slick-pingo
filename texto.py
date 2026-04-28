class Versiculo:
    def __init__(self, texto, numero = 0):
        if len(texto) == 0:
            raise ValueError('Necessário texto para criar um versículo.')
        else:
            self.__texto = texto.strip()
        self.__numero = numero

    def __str__(self):
        return f"{self.__numero} {self.__texto}"

    def __repr__(self):
        return f"Versiculo({self.__texto}, {self.__numero})"


class Capitulo:
    def __init__(self, texto, numero = 0):
        self.__texto = texto
        self.__versiculos = []
        self.__numero = numero
        self.adiciona_versiculos(texto)
        
    @property
    def numero(self):
        return self.__numero
    
    @property
    def versiculos(self):
        return self.__versiculos

    @numero.setter
    def numero(self, valor):
        self.__numero = valor

    def adiciona_versiculos(self, texto):
        versiculos = texto.split("\n")
        for versiculo in versiculos:
            self.__versiculos.append(Versiculo(versiculo, versiculos.index(versiculo) + 1))
    
    def __str__(self):
        return f'Capítulo {self.numero}'

    def __repr__(self):
        return f"Capitulo({self.__texto}, {self.__numero})"


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
    
    def criaCapitulos(self, texto):
        if len(texto) > 0:
            capitulos = texto.split('\n\n')
            for capitulo in capitulos:
                self.criaCapitulo(capitulo, capitulos.index(capitulo) + 1)
        else:
            raise ValueError(('Para criar Capítulos é necessário um texto'))
    
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
            texto += str(capitulo).upper() + '\n'
            for versiculo in capitulo.versiculos:
                texto += str(versiculo) + '\n'
            texto += '\n'
        return texto

