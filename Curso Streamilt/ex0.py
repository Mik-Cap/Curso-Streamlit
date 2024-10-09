# importanto a biblioteca streamlit
import streamlit as st # nomeando ela para st

# criando uma variavel e armazenando o input 
numero = st.number_input("Digite um Numero:",step=1) 

# se o numero for maior que 1 positivo, 0 numero e -1 negativo
if numero>1:
    st.write(f" Positivo: {numero}")
elif numero == 0:
    st.write(f" Nulo: {numero} ")
else:
    st.write(f" Negativo: {numero}")