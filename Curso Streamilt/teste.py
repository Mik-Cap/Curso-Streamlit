import streamlit as st
import requests
import pandas as pd


def format_value(value):
    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f} milhões"
    elif value >= 1_000:
        return f"{value / 1_000:.2f} mil"
    else:
        return f"{value:.2f}"

st.title("DASHBOARD DE VENDAS:shopping_trolley:")
url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())

if st.button("todos"):
    st.balloons()
    receita = df['Preço'].sum()
    st.metric('Receita', format_value(receita)) 
    linhas = df.shape[0]
    st.metric('Quantidade de vendas (linhas)',format_value (linhas))
    st.metric('Quantidade de variáveis (colunas)', df.shape[1])
    st.dataframe(df)
    st.snow()
else:
    st.write("clique no botão todos")
