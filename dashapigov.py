import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard de Serviços Públicos", layout="wide")

# Estilo CSS personalizado
st.markdown(
    """
    <style>
        body { font-family: 'Arial', sans-serif; }
        .stDataFrame { border-radius: 10px; }
        .css-1d391kg { background-color: #f0f2f6; }
        .stSelectbox, .stTextInput, .stDataEditor { border-radius: 10px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título do dashboard
st.title("📊 Dashboard de Serviços Públicos")
st.markdown("---")

# Conectar ao banco de dados
conn = sqlite3.connect('servicos_publicos.db')
cursor = conn.cursor()

# Consultar os dados da tabela
cursor.execute('''SELECT 
    nome, 
    contato, 
    CASE 
        WHEN gratuito = 'true' THEN 'Sim' 
        WHEN gratuito = 'false' THEN 'Não' 
        ELSE gratuito 
    END AS gratuito, 
    nome_orgao, 
    palavras_chave, 
    etapas 
FROM servicos''')
rows = cursor.fetchall()

# Converter os dados para um DataFrame
df = pd.DataFrame(rows, columns=["nome", "contato", "gratuito", "nome_orgao", "palavras_chave", "etapas"])

# Filtros na barra lateral
st.sidebar.header("🔍 Filtros")
orgao = st.sidebar.selectbox("Selecione o Órgão", ["Todos"] + list(df["nome_orgao"].unique()))
palavra_chave = st.sidebar.text_input("Palavra-Chave")

# Aplicar filtros
df_filtrado = df if orgao == "Todos" else df[df["nome_orgao"] == orgao]
if palavra_chave:
    df_filtrado = df_filtrado[df_filtrado["palavras_chave"].str.contains(palavra_chave, case=False, na=False)]

# Layout de colunas
col1, col2 = st.columns([2, 1])

with col1:
    st.write("### 📋 Dados dos Serviços Filtrados")
    st.data_editor(df_filtrado, use_container_width=True, height=300)

with col2:
    # Gráfico de barras interativo
    st.write("### 📊 Serviços Gratuitos vs. Pagos")
    fig_bar = px.bar(df_filtrado, x="gratuito", title="Distribuição de Serviços", text_auto=True, color="gratuito")
    st.plotly_chart(fig_bar, use_container_width=True)

# Aplicar filtros ao gráfico de pizza
df_pizza = df_filtrado.copy()
contagem_orgaos = df_pizza["nome_orgao"].value_counts().reset_index()
contagem_orgaos.columns = ["nome_orgao", "contagem"]
contagem_orgaos["nome_orgao"] = contagem_orgaos["nome_orgao"].where(contagem_orgaos["contagem"] > 5, "Outros")


st.write("### 🏛️ Distribuição de Serviços por Órgão")
fig_pie = px.pie(
    contagem_orgaos, 
    names="nome_orgao", 
    values="contagem", 
    title="Proporção de Serviços por Órgão", 
    hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Set3,
)
st.plotly_chart(fig_pie, use_container_width=True)

# Exibir detalhes do serviço
st.write("### 🧐 Detalhes do Serviço Selecionado")
if not df_filtrado.empty:
    servico_selecionado = st.selectbox("Selecione um Serviço", df_filtrado["nome"])
    servico_info = df_filtrado[df_filtrado["nome"] == servico_selecionado].iloc[0]
    
    st.info(f"**Nome:** {servico_info['nome']}")
    st.write(f"**Órgão:** {servico_info['nome_orgao']}")
    st.write(f"**Contato:** {servico_info['contato']}")
    st.write(f"**Gratuito:** {servico_info['gratuito']}")
    st.write(f"**Palavras-Chave:** {servico_info['palavras_chave']}")
    st.write(f"**Etapas:** {servico_info['etapas']}")
else:
    st.warning("Nenhum serviço encontrado com os filtros selecionados.")

# Botão para baixar os dados filtrados
st.markdown("---")
st.download_button("📥 Baixar Dados Filtrados", df_filtrado.to_csv(index=False), "servicos_filtrados.csv", "text/csv")

# Fechar a conexão com o banco de dados
conn.close()
