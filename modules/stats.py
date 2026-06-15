def contar_palavras(texto):
    return len(texto.split())


def calcular_tempo_leitura(texto):
    palavras = contar_palavras(texto)

    minutos = max(1, round(palavras / 200))

    return minutos


def contar_caracteres(texto):
    return len(texto)


def contar_paragrafos(texto):

    paragrafos = [
        p for p in texto.split("\n")
        if p.strip()
    ]

    return len(paragrafos)