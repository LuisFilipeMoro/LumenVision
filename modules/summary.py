from collections import Counter
import re


def gerar_resumo(texto, quantidade_frases=3):

    frases = re.split(r'[.!?]', texto)

    frases = [
        frase.strip()
        for frase in frases
        if len(frase.strip()) > 30
    ]

    if len(frases) <= quantidade_frases:
        return texto

    stopwords = {
        "a", "o", "e", "de", "do", "da", "em",
        "um", "uma", "para", "com", "que",
        "os", "as", "na", "no", "por", "ao",
        "dos", "das", "se", "não", "mais",
        "como", "ou", "ser", "foi", "são"
    }

    palavras = re.findall(
        r'\b[a-zA-ZÀ-ÿ]+\b',
        texto.lower()
    )

    palavras_importantes = [
        p
        for p in palavras
        if len(p) > 3 and p not in stopwords
    ]

    frequencia = Counter(palavras_importantes)

    ranking = []

    for indice, frase in enumerate(frases):

        score = 0

        palavras_frase = re.findall(
            r'\b[a-zA-ZÀ-ÿ]+\b',
            frase.lower()
        )

        for palavra in palavras_frase:
            score += frequencia.get(palavra, 0)

        ranking.append((score, indice, frase))

    ranking.sort(reverse=True)

    melhores = ranking[:quantidade_frases]

    melhores.sort(key=lambda x: x[1])

    resumo = ". ".join(
        frase
        for _, _, frase in melhores
    )

    palavras = resumo.split()

    if len(resumo) > 60:
        resumo  = " ".join(palavras[:60]) + "..."

    return resumo