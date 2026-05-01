if __name__ == "__main__":
    rodando = True
    caminho1 = input('Informe o caminho do documento a ser lido: ')
    while rodando:
        caminho2 = '/Users/joaovictor/appBiblia/arquivo1.txt'
        with open(caminho1, "r", encoding="utf-8") as f:
            comparando = f.read()[1:]
        with open(caminho2, "r", encoding="utf-8") as f:
            comparado = f.read()
        print(comparando in comparado)
        caminho1 = input('Informe o caminho do documento a ser lido: ')
        if len(caminho1) == 0:
            rodando = False