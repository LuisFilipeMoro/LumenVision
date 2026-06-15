from ollama import chat

def gerar_resposta(prompt):

    resposta = chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta["message"]["content"]


def gerar_resumo_ia(texto):

    print("Enviando texto para IA...")

    texto = texto[:2500]

    prompt = f"""
    Você é um assistente acadêmico especializado em análise de documentos.

    Leia o texto abaixo e gere um resumo detalhado em português.

    Regras:
    - Escreva apenas o resumo.
    - Não escreva frases como "O resumo é" ou "O texto fala sobre".
    - Não cite autores, e-mails ou instituições.
    - Não copie trechos literalmente.
    - Produza um resumo entre 120 e 180 palavras.
    - Explique os principais conceitos, objetivos e conclusões do texto.
    - Utilize linguagem clara e formal.

    Texto:
    {texto}
    """

    return gerar_resposta(prompt)

def gerar_tema_ia(texto):

    texto = texto[:2000]

    prompt = f"""
    Você é um especialista em análise de documentos.

    Leia o texto abaixo e identifique o tema principal.

    Regras:
    - Responda apenas com o tema.
    - Use no máximo 8 palavras.
    - Não use ponto final.
    - Não escreva explicações.
    - O tema deve ser claro e profissional.

    Texto:
    {texto}
    """

    return gerar_resposta(prompt)


def gerar_questoes_ia(texto):

    texto = texto[:2500]

    prompt = f"""
    Você é um professor universitário.

    Com base no texto abaixo, crie 5 perguntas de revisão para estudo.

    Regras:
    - Faça perguntas claras.
    - Numere de 1 a 5.
    - Não forneça respostas.
    - Foque nos conceitos mais importantes.
    - Escreva em português.

    Texto:
    {texto}
    """

    return gerar_resposta(prompt)

def gerar_analise_ia(texto):

    texto = texto[:2500]

    prompt = f"""
    Você é um especialista acadêmico.

    Analise o texto abaixo e responda EXATAMENTE neste formato:

    TEMA:
    [tema do documento]

    RESUMO:
    - Produza um resumo entre 180 e 250 palavras.
    - Explique o contexto, os objetivos, os principais conceitos e as conclusões do texto.

    QUESTÕES:
    1. [pergunta]
    2. [pergunta]
    3. [pergunta]
    4. [pergunta]
    5. [pergunta]

    Regras:
    - Não cite autores.
    - Não explique o que está fazendo.
    - Retorne apenas o formato solicitado.

    Texto:
    {texto}
    """

    return gerar_resposta(prompt)

def gerar_dicas_estudo_ia(texto):

    texto = texto[:2500]

    prompt = f"""
    Você é um especialista em aprendizagem.

    Com base no texto abaixo, forneça dicas de estudo.

    Regras:
    - Gere entre 3 e 5 dicas.
    - Seja objetivo.
    - Escreva em português.
    - Foque em como estudar o conteúdo.
    - Utilize tópicos.

    Texto:
    {texto}
    """

    return gerar_resposta(prompt)