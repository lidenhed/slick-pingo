from controle import *

class Tela:
    def __init__(self, vm):
        self.__vm = vm

    def telaInicial(self):
        print('''Escolha a opção:
        1 - Adicionar um livro
        2 - Adicionar um capítulo a um livro
        3 - Abrir um livro
        4 - Buscar palavra
        5 - Sair
        ''')
        opcao = input('Selecionar: ')
        return opcao
        # self.__vm.controleOpcoes(opcao)

    
    def informaLivro(self):
        nome = input('Informe o nome do livro: ')
        return nome
    
    def recebeTexto(self):
        caminho = input("Informe o caminho completo do arquivo: ")
        return caminho

    def listaLivros(self, listaDeLivros):
        for livro in listaDeLivros:
            print(listaDeLivros.index(livro) + 1, '-', livro)
        opcao = input('Escolha o livro: ')
        return opcao

    
    def buscaPalavra(self):
        palavra = input('Qual palavra deseja buscar? \n')
        return palavra

    def retornaListaDePalavras(self, listaDePalavras):
        print(listaDePalavras)



