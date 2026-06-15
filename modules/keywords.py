from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def extrair_keywords(texto, quantidade=5):

    stop_words = set(stopwords.words("portuguese"))

    palavras = word_tokenize(texto.lower())

    palavras_filtradas = []

    for palavra in palavras:

        if palavra.isalpha():

            if palavra not in stop_words:

                if len(palavra) > 3:

                    palavras_filtradas.append(palavra)

    bigramas = []

    for i in range(len(palavras_filtradas) - 1):

        bigrama = (
            palavras_filtradas[i]
            + " "
            + palavras_filtradas[i + 1]
        )

        bigramas.append(bigrama)

    contador = Counter(bigramas)

    return [
        frase
        for frase, _
        in contador.most_common(quantidade)
    ]
def identificar_tema(texto, keywords):

    if len(keywords) >= 3:

        return (
            keywords[0].title()
            + " e "
            + keywords[1].title()
        )

    elif len(keywords) == 2:

        return (
            keywords[0].title()
            + " e "
            + keywords[1].title()
        )

    elif len(keywords) == 1:

        return keywords[0].title()

    return "Não identificado"