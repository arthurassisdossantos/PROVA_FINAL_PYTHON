import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Painel IQVU - Belo Horizonte", layout="wide")

df = pd.read_csv("dados_transporte_bh.csv", sep=";")
df.columns = df.columns.str.strip()
df["LINHA"] = df["LINHA"].astype(str).str.strip()
df = df[~df["PC"].isin([0, 3])]
viagens = df.groupby("LINHA").size().reset_index(name="viagens")
top_10_viagens = viagens.sort_values(by="viagens", ascending=False).head(10)
print(top_10_viagens)

df = pd.read_csv("dados_transporte_bh.csv", sep=";")
df.columns = df.columns.str.strip()
df["LINHA"] = df["LINHA"].astype(str).str.strip()
df = df[~df["PC"].isin([0, 3])]
viagens = df.groupby("LINHA").size().reset_index(name="viagens")
top_10 = viagens.sort_values(by="viagens", ascending=False).head(10)

st.title("Transporte Coletivo de Belo Horizonte — Top 10 Linhas")

st.sidebar.header("Opções de Visualização")
opcao = st.sidebar.radio("Escolha o que deseja exibir:", ["Tabela", "Gráfico"])

if opcao == "Tabela":
    st.header("Tabela das 10 linhas com mais viagens")
    st.dataframe(top_10, use_container_width=True, hide_index=True)

elif opcao == "Gráfico":
    st.header("Gráfico das 10 linhas com mais viagens")
    fig = px.bar(
        top_10,
        x="LINHA",
        y="viagens",
        labels={"LINHA": "Linha de Ônibus", "viagens": "Número de Viagens"},
        text_auto=True,
    )
    fig.update_xaxes(type="category")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption(
    "Fonte dos dados: dados abertos da Prefeitura de Belo Horizonte, https://pbh.gov.br."
)



