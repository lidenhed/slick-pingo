from PyPDF2 import PdfReader


def ler_arquivo(caminho):
    if caminho.endswith(".txt"):
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()

    elif caminho.endswith(".pdf"):
        reader = PdfReader(caminho)
        texto = ""

        for page in reader.pages:
            texto += page.extract_text() or ""

        return texto

    else:
        raise ValueError("Formato não suportado")

def correcao_erros_comuns(texto):
    if ' -' in texto:
        i = texto.index(' -')
        texto = texto[:i] + '-' + texto[i+2:]
    return texto

def primeira_deputacao(texto):
    texto = texto.split('\n')
    novo_texto = ''
    fim_da_pagina = False
    inicio = False
    for line in texto:
        line = correcao_erros_comuns(line)
        palavras = line.split(' ')
        partes = [palavra for palavra in palavras if len(palavra) > 0]
        if len(partes) > 0:
            if partes[-1].isdigit():
                fim_da_pagina = True
            primeira_palavra = partes[0]
            i = 0
            while i < len(primeira_palavra) and primeira_palavra[i].isdigit():
                i += 1
            if 0 < i and i < len(primeira_palavra):
                if primeira_palavra[i] not in '.,;?!':
                    numero = primeira_palavra[0:i]
                    primeira_palavra = primeira_palavra[i:]
                    partes[0] = numero + ' ' + primeira_palavra
                if int(numero) == 1:
                    inicio = True
                else:
                    inicio = False

            if fim_da_pagina:
                novo_texto += ' ' + ' '.join(partes[:-1])
                fim_da_pagina = False
            elif inicio:
                novo_texto += '\n\n' + ' '.join(partes)


            novo_texto += frase

    return novo_texto

    def segunda_deputacao(texto):
        pass

    


if __name__ == "__main__":
    caminho = input('Informe o caminho do documento a ser lido: ')
    texto = ler_arquivo(caminho)
    primeira_etapa = primeira_deputacao(texto)



            
    with open("arquivo1.txt", "w", encoding="utf-8") as f:
        f.write(primeira_etapa)

    # /Users/joaovictor/Desktop/123.pdf
    # /Users/joaovictor/Desktop/321.pdf



    def substitui_caracteres(sentenca, substituir, substituto):
        i = sentenca.index(substituir)
        d = len(substituir)
        nova_sentenca = sentenca[:i] + substituto + sentenca[i+d:]
        return nova_sentenca