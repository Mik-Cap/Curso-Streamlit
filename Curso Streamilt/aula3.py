import streamlit as st
import random

# 1. Criar um número secreto
if 'número_secreto' not in st.session_state:
    st.session_state.número_secreto = random.randint(1, 5)


# 2. Título na aplicação
st.title("=== Jogo: Descubra o Número Secreto ===")

# 3. Dar uma mensagem de boas-vindas
st.write("Bem-vindo ao jogo! Tente adivinhar o número secreto entre 1 e 5.")

# 4. Receber o chute do usuário
chute = st.number_input("Digite seu palpite:", min_value=1, max_value=5)

if st.button("Enviar"):
    # 6. Verificar o chute com o número secreto
    if chute < st.session_state.número_secreto:
        
        st.write("Muito baixo! Tente novamente.")
    elif chute > st.session_state.número_secreto:
        st.write(f"Muito alto! Tente novamente.{st.session_state.número_secreto}")
    else:
        # 7. Mostrar uma mensagem personalizada
        st.balloons()
        st.write(f"Parabéns! Você acertou o número secreto: {st.session_state.número_secreto}")
        # Reiniciar o jogo
        if st.button("Reiniciar o jogo"):
            st.session_state.número_secreto = random.randint(1, 5)
            st.write("O jogo foi reiniciado. Tente adivinhar novamente!")