from docx import Document


def extrair_texto_docx(arquivo):
    documento = Document(arquivo)

    texto = ""

    for paragrafo in documento.paragraphs:
        texto += paragrafo.text + "\n"

    return texto