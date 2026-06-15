# LumenVision

**Transformando conteúdo em conhecimento.**

O **LumenVision** é um sistema inteligente desenvolvido para a disciplina de Sistemas Multimídia (UFSC) que processa materiais de estudo não estruturados (PDF, DOCX e imagens) e os transforma em informações organizadas, facilitando a leitura, compreensão e análise de conteúdo acadêmico e técnico.

---

## Funcionalidades

-  **Leitura Multiformato:** Extração de conteúdo de arquivos PDF e DOCX.
-  **OCR Avançado:** Extração de texto de imagens utilizando PyTesseract e OpenCV.
-  **Inteligência Artificial Local:** Geração de resumos automáticos, perguntas de revisão e dicas estratégicas através do **Ollama (Qwen 2.5)**.
-  **Privacidade Total:** Todo o processamento de IA e OCR é feito localmente (offline), sem envio de dados para servidores externos.
-  **Interface Interativa:** Visualização estruturada e fluida desenvolvida com **Streamlit**.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 
- **Interface:** Streamlit
- **Orquestração de IA:** Ollama (Modelo: Qwen 2.5)
- **Processamento de Imagem/OCR:** PyTesseract & OpenCV
- **Leitura de Documentos:** PDFPlumber & python-docx

---

## Como Executar o Projeto Localmente

1. **Certifique-se de ter o Ollama instalado e rodando o modelo:**
   ollama run qwen2.5

2. **Baixe (clone) este repositório:**
   git clone [https://github.com/LuisFilipeMoro/LumenVision.git](https://github.com/LuisFilipeMoro/LumenVision.git)
   cd LumenVision   

3. **Instale todas as bibliotecas necessárias:**
   pip install -r requirements.txt

4. **Inicie a aplicação no navegador:**
   streamlit run app.py
    
---

## Estrutura de Pastas

LumenVision/
│
├── assets/               # Arquivos de estilização e identidade visual
│   ├── logo.png
│   └── styles.css
│
├── modules/              # Módulos com as funcionalidades do sistema
│   ├── ai.py             # Integração principal com o Ollama / Qwen 2.5
│   ├── docx_reader.py    # Extrator de texto de arquivos Word (.docx)
│   ├── image_reader.py   # Módulo de OCR para leitura de imagens
│   ├── keywords.py       # Extrator de palavras-chave do conteúdo
│   ├── pdf_reader.py     # Extrator de texto de arquivos PDF
│   ├── stats.py          # Estatísticas e métricas dos dados processados
│   ├── summary.py        # Lógica de geração de resumos acadêmicos
│   └── txt_reader.py     # Leitor de arquivos de texto simples (.txt)
│
├── uploads/              # Pasta temporária para armazenamento dos arquivos enviados
│
├── app.py                # Arquivo principal da interface (Streamlit)
├── requirements.txt      # Bibliotecas e dependências do projeto
└── teste_ia.py           # Script de teste de integração com a IA

## Status: 
Em desenvolvimento (Projeto Prático - UFSC)

## Autor: 
Luís Filipe Moro Aguiar
