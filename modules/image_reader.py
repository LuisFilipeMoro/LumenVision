from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extrair_texto_imagem(arquivo):

    imagem = Image.open(arquivo)

    texto = pytesseract.image_to_string(
    imagem,
    lang="por"
)

    return texto