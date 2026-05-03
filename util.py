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
    
def substitui_caracteres(sentenca, substituir, substituto):
        i = sentenca.index(substituir)
        d = len(substituir)
        nova_sentenca = sentenca[:i] + substituto + sentenca[i+d:]
        return nova_sentenca

def correcao_erros_comuns(texto):
    while ' -' in texto:
        texto = substitui_caracteres(texto, ' -', '-')
    while '- ' in texto:
        texto = substitui_caracteres(texto, '- ', '-')
    while ' .' in texto:
        texto = substitui_caracteres(texto, ' .', '.')
    while ' ;' in texto:
        texto = substitui_caracteres(texto, ' ;', ';')
    while '.”' in texto:
        texto = substitui_caracteres(texto, '.”', '”.')
    while ' ,' in texto:
        texto = substitui_caracteres(texto, ' ,', ',')
    while ' :' in texto:
        texto = substitui_caracteres(texto, ' :', ':')
    while '.)' in texto:
        texto = substitui_caracteres(texto, '.)', ').')
    return texto

def primeira_depuracao(texto):
    texto = texto.split('\n')
    novo_texto = ''
    fim_da_pagina = False
    for line in texto:
        palavras = line.split(' ')
        partes = [palavra for palavra in palavras if len(palavra) > 0]
        if len(partes) > 0:
            primeira_palavra = partes[0]
            i = 0
            while i < len(primeira_palavra) and primeira_palavra[i].isdigit():
                i += 1
            if 0 < i and i < len(primeira_palavra) and primeira_palavra[i] not in '.,;?!':
                fim_da_pagina = False
                numero = primeira_palavra[0:i]
                primeira_palavra = primeira_palavra[i:]
                partes[0] = primeira_palavra
                if int(numero) == 1:
                    partes = ['\n\n' + numero + '\t'] + partes
                else:
                    partes = ['\n' + numero + '\t'] + partes
            else:
                partes = [''] + partes
                if primeira_palavra.islower():
                    fim_da_pagina = False
            if not fim_da_pagina:
                if partes[-1].isdigit():
                    partes = partes[:-1]
                    fim_da_pagina = True
                frase = ' '.join(partes)
                novo_texto += frase
    novo_texto = correcao_erros_comuns(novo_texto)
    return novo_texto


def segunda_depuracao(texto):
    linhas = texto.split('\n')
    tuplas = []
    frases = []
    frase_anterior = ''
    for linha in linhas:
        posicao = linhas.index(linha)
        palavras = linha.split()
        if len(palavras) > 0 and palavras[0].isdigit() and palavras[1].islower()\
                and len(frases) > 0 and frase_anterior == frases[-1]:
            frases.pop()
            tuplas.pop()
            frase_anterior = ''
        i = len(linha)-1
        while i >= 0 and linha[i] not in '.?!”":;':
            i -= 1
        frase = linha[i+1: ]
        if len(frase) > 0 and frase[-1] not in [',',')','”','’']:
            frases.append(frase)
            tuplas.append((frase.strip(), posicao))
            frase_anterior = frase
        else:
            frase_anterior = ''
    frases = '\n'.join(frases)
    return frases, tuplas

def terceira_depuracao(texto, tuplas):
    linhas = texto.split('\n')
    for tupla in tuplas:
        trecho, posicao = tupla
        frase = linhas[posicao]
        indicefinal = 0
        while frase.count(trecho) > 0:
            indice = frase.find(trecho)
            indicefinal += indice + len(trecho)
            frase = frase[indice+len(trecho): ]
        indicefinal -= len(trecho)
        nova_frase = linhas[posicao][:indicefinal]
        linhas[posicao] = nova_frase.strip()
    return '\n'.join(linhas)


def ultimo_sinal(texto):
    linhas = texto.split('\n')
    sinais = []
    for linha in linhas:
        linha = linha.split(' ')
        linha = [palavra for palavra in linha if len(palavra) > 0]
        if len(linha) > 0:
            ultima_palavra = linha[-1]
            if len(ultima_palavra) > 0:
                sinais.append(ultima_palavra[-1])
    texto = ''.join(sinais)
    return str(set(texto))
    

if __name__ == "__main__":
    caminho = input('Informe o caminho do documento a ser lido: ')
    texto = ler_arquivo(caminho)
    primeira_etapa = primeira_depuracao(texto)
    with open("1.txt", "w", encoding="utf-8") as f:
        f.write(primeira_etapa)
    a, b = segunda_depuracao(primeira_etapa)
    with open("2.txt", "w", encoding="utf-8") as f:
        f.write(a)
    terceira_etapa = terceira_depuracao(primeira_etapa, b)
    with open("3.txt", "w", encoding="utf-8") as f:
        f.write(terceira_etapa)

    # /Users/joaovictor/Desktop/123.pdf
    # /Users/joaovictor/Desktop/321.pdf
    # /Users/joaovictor/Desktop/1.pdf
    # /Users/joaovictor/Desktop/Portugues-NVI-All-Bible.pdf



    