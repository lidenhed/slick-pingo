from tela import *

# /Users/joaovictor/Desktop/teste.txt


def main():
    c = Controle()
    t = Tela(c)

    while True:

        opcao = t.telaInicial()

        match opcao:
            case '1':
                nome = t.informaLivro()
                c.iniciaLivro(nome)
            case '2':
                nome = t.listaLivros([livro.nome for livro in c.livros])
                texto = c.importaTexto(t.recebeTexto())
                c.encontraLivro(nome).criaCapitulo(texto)
            case '3':
                nome = t.informaLivro()
                c.encontraLivro(nome).imprimeCapitulos()
            case '4':
                palavra = t.buscaPalavra()
                t.retornaListaDePalavras(c.busca(palavra))
            case '5':
                break
        print()



main()