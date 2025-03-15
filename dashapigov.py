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
        .stMarkdown h3 { color: #2e86c1; }
        .stButton button { background-color: #2e86c1; color: white; border-radius: 10px; }
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
        WHEN Gratuito = 'true' THEN 'Sim' 
        WHEN Gratuito = 'false' THEN 'Não' 
        ELSE Gratuito 
    END AS Gratuito, 
    nome_orgao, 
    palavras_chave, 
    etapas 
FROM servicos''')
rows = cursor.fetchall()

# Converter os dados para um DataFrame
df = pd.DataFrame(rows, columns=["Nome do Serviço", "Contato", "Gratuito", "Nome do Orgão", "Palavras Chaves", "Etapas"])

# Contar o número de serviços por órgão
contagem_orgaos = df["Nome do Orgão"].value_counts().reset_index()
contagem_orgaos.columns = ["Nome do Orgão", "Contagem"]

# Filtrar órgãos com mais de 100 serviços
orgaos_mais_de_100 = contagem_orgaos[contagem_orgaos["Contagem"] > 100]["Nome do Orgão"].tolist()

# Filtros na barra lateral
st.sidebar.header("🔍 Filtros")
orgao = st.sidebar.selectbox("Selecione o Órgão", ["Orgãos com 100 Serviços"] + orgaos_mais_de_100 + list(df["Nome do Orgão"].unique()))
palavra_chave = st.sidebar.text_input("Palavras Chaves")

# Aplicar filtros
if orgao == "Orgãos com 100 Serviços":
    df_filtrado = df[df["Nome do Orgão"].isin(orgaos_mais_de_100)]
elif orgao:
    df_filtrado = df[df["Nome do Orgão"] == orgao]
else:
    df_filtrado = df

if palavra_chave:
    df_filtrado = df_filtrado[df_filtrado["Palavras Chaves"].str.contains(palavra_chave, case=False, na=False)]

# Layout de colunas
col1, col2 = st.columns([2, 1])

with col1:
    st.write("### 📋 Dados dos Serviços Filtrados")
    st.dataframe(df_filtrado, use_container_width=True, height=300)

with col2:
    # Gráfico de barras empilhadas
    st.write("### 📊 Serviços por Órgão e Tipo")
    df_grouped = df_filtrado.groupby(["Nome do Orgão", "Gratuito"]).size().reset_index(name="contagem")
    fig_bar_stacked = px.bar(
        df_grouped, 
        x="Nome do Orgão", 
        y="contagem", 
        color="Gratuito", 
        title="Distribuição de Serviços por Órgão",
        text_auto=True,
        barmode="stack"
    )
    st.plotly_chart(fig_bar_stacked, use_container_width=True)

# Exibir detalhes do serviço
st.write("### 🧐 Detalhes do Serviço Selecionado")

if not df_filtrado.empty:
    # Selecionar um serviço
    servico_selecionado = st.selectbox("Selecione um Serviço", df_filtrado["Nome do Serviço"])
    servico_info = df_filtrado[df_filtrado["Nome do Serviço"] == servico_selecionado].iloc[0]

    # Usar colunas para organizar as informações
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**📌 Nome do Serviço**")
        st.info(servico_info['Nome do Serviço'])

        st.markdown("**🏛️ Órgão Responsável**")
        st.success(servico_info['Nome do Orgão'])

        st.markdown("**📞 Contato**")
        st.warning(servico_info['Contato'])

    with col2:
        st.markdown("**💸 Gratuito**")
        if servico_info['Gratuito'] == "Sim":
            st.success("✅ Sim")
        else:
            st.error("❌ Não")

        st.markdown("**🔑 Palavras-Chave**")
        st.info(servico_info['Palavras Chaves'])

        st.markdown("**📝 Etapas**")
        st.info(servico_info['Etapas'])

else:
    st.warning("⚠️ Nenhum serviço encontrado com os filtros selecionados.")

# Botão para baixar os dados filtrados
st.markdown("---")
st.download_button(
    label="📥 Baixar Dados Filtrados",
    data=df_filtrado.to_csv(index=False),
    file_name="servicos_filtrados.csv",
    mime="text/csv"
)

# Fechar a conexão com o banco de dados
conn.close()