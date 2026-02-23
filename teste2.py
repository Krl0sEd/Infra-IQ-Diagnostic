import streamlit as st

# 1. Criamos uma variável na memória para saber em qual tela estamos
if 'tela_atual' not in st.session_state:
    st.session_state.tela_atual = 'Home'

# 2. Criamos as funções que desenham cada tela
def tela_home():
    st.title("Página Inicial")
    st.write("Bem-vindo ao sistema!")
    if st.button("Ir para Dashboard"):
        st.session_state.tela_atual = 'Dashboard'
        st.rerun() # Força a tela a atualizar instantaneamente

def tela_dashboard():
    st.title("Dashboard de Infraestrutura")
    st.write("Aqui ficam os gráficos...")
    if st.button("Voltar"):
        st.session_state.tela_atual = 'Home'
        st.rerun()

# 3. O "Roteador" do SPA
if st.session_state.tela_atual == 'Home':
    tela_home()
elif st.session_state.tela_atual == 'Dashboard':
    tela_dashboard()