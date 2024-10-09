# essas linhas importa o streamlit
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Estamos iniciando o streamlit
# Ele nos ajuda´ra no projeto final
# Em sua instalação vem incluido o panda e outras libs.


# Entrada do usuario para a idade
idade = st.number_input("Digite sua idade:", min_value=14, max_value=120)
if idade >= 18:
    # Uso obrigatorio da Identação 
    st.write(f"Hello World- Você é Maior de idade {idade}")
else:
    st.write(f"Hello World - Você é menor de idade {idade}")