import streamlit as st
from PIL import Image
from modules.pdf_reader import extrair_texto_pdf
from modules.docx_reader import extrair_texto_docx
from modules.stats import (
    contar_palavras,
    calcular_tempo_leitura,
    contar_paragrafos
)
from modules.keywords import extrair_keywords
from modules.image_reader import extrair_texto_imagem
from modules.txt_reader import extrair_texto_txt
from modules.ai import (
    gerar_questoes_ia,
    gerar_analise_ia,
    gerar_dicas_estudo_ia
)


# Configuração da página
st.set_page_config(
    page_title="LumenVision",
    page_icon="🌟",
    layout="wide"
)


# Carregar CSS
with open("assets/styles.css", "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Carregar Logo
logo = Image.open("assets/logo.png")

# Exibir Logo
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    st.image(logo, width=400)

# Título
st.markdown(
    '<div class="main-title">LumenVision</div>',
    unsafe_allow_html=True
)

# Slogan
st.markdown(
    '<div class="slogan">Transformando conteúdo em conhecimento.</div>',
    unsafe_allow_html=True
)

# Descrição
st.markdown(
    '''
    <div class="description">
    O LumenVision transforma materiais de estudo não estruturados
    em informações organizadas e acessíveis.
    </div>
    ''',
    unsafe_allow_html=True
)

st.divider()

# Upload

texto_extraido = ""
keywords = []

arquivo = st.file_uploader(
    "📂 Arraste ou selecione um arquivo",
    type=["pdf", "docx", "txt", "jpg", "jpeg", "png"]
)

if arquivo:

    if (
        "arquivo_atual" not in st.session_state
        or st.session_state.arquivo_atual != arquivo.name
    ):

        st.session_state.arquivo_atual = arquivo.name

        if "analise" in st.session_state:
            del st.session_state.analise

        if "questoes" in st.session_state:
            del st.session_state.questoes

        if "dicas" in st.session_state:
            del st.session_state.dicas    

    texto_extraido = ""

    if arquivo.name.endswith(".pdf"):
        texto_extraido = extrair_texto_pdf(arquivo)

    elif arquivo.name.endswith(".docx"):
        texto_extraido = extrair_texto_docx(arquivo)

    elif arquivo.name.endswith(".txt"):
        texto_extraido = extrair_texto_txt(arquivo)

    elif arquivo.name.endswith(".jpg"):
        texto_extraido = extrair_texto_imagem(arquivo)

    elif arquivo.name.endswith(".jpeg"):
        texto_extraido = extrair_texto_imagem(arquivo)

    elif arquivo.name.endswith(".png"):
        texto_extraido = extrair_texto_imagem(arquivo)  

    quantidade_palavras = contar_palavras(texto_extraido)   
    tempo_leitura = calcular_tempo_leitura(texto_extraido) 
    quantidade_paragrafos = contar_paragrafos(texto_extraido)

    keywords = extrair_keywords(texto_extraido)

    if "analise" not in st.session_state:
        with st.spinner("🧠 A IA está analisando o documento..."):
            st.session_state.analise = gerar_analise_ia(
                texto_extraido
            )

    if "dicas" not in st.session_state:
        st.session_state.dicas = gerar_dicas_estudo_ia(
            texto_extraido
    )        

    analise = st.session_state.analise
    partes = analise.split("RESUMO:")

    tema = (
        partes[0]
        .replace("TEMA:", "")
        .replace("*", "")
        .strip()
)

    resto = partes[1].split("QUESTÕES:")

    resumo = (
        resto[0]
        .replace("*", "")
        .strip()
)

    questoes = resto[1].strip()
    if "questoes" not in st.session_state:
        st.session_state.questoes = questoes


    st.success("✓ Arquivo carregado com sucesso.")

    col1, col2, col3, col4, col5, = st.columns(5)

    with col1:
        st.metric("📄 Palavras", quantidade_palavras)

    with col2:
        st.metric("⏱️ Leitura", f"{tempo_leitura} min")

    with col3:
        st.metric("📑 Parágrafos", quantidade_paragrafos)

    with col4:
        st.metric("🔑 Keywords", len(keywords))

    with col5:
        st.metric("🎯 Tema", tema[:20] + "..." if len(tema) > 20 else tema)

if texto_extraido:

    st.subheader("🎯 Tema Principal")
    st.info(tema)
    st.divider()

    st.text_area(
        "",
        texto_extraido,
        height=300
    )

    st.divider()
    st.subheader("📝 Resumo Automático")
    st.info(resumo)


    st.divider()
    st.subheader("📚 Questões de Revisão")

    if "questoes" not in st.session_state:
        st.session_state.questoes = questoes

    questoes_container = st.empty()

    questoes_container.info(st.session_state.questoes)

    if st.button(
        "🔄 Gerar Novas Questões",
        key="btn_gerar_questoes"
    ):

        with st.spinner("Gerando novas questões..."):

            st.session_state.questoes = gerar_questoes_ia(
                texto_extraido
            )

    questoes_container.info(st.session_state.questoes)

    st.divider()

    st.subheader("💡 Dicas de Estudo")
    st.info(st.session_state.dicas)


else:
    st.warning(
        "Nenhum texto foi encontrado. Verifique se possui texto legível."
    )


    st.divider()
    st.subheader("📊 Painel de Insights")
    st.info(
        "A análise do conteúdo aparecerá aqui."
    )
    st.divider()

st.subheader("🔑 Palavras-Chave")

tags_html = ""

for palavra in keywords:
    tags_html += f"""
    <span class="keyword-tag">
        {palavra.title()}
    </span>
    """
st.markdown(tags_html, unsafe_allow_html=True)

