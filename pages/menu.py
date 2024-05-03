import streamlit as st

def mostraMenu():
    st.sidebar.title('MENU')
    botaoProfissional = st.sidebar.button("PROFISSIONAIS")
    botaoCliente = st.sidebar.button("CLIENTES")
    botaoPet = st.sidebar.button("PETS")
    st.sidebar.button("AGENDAMENTOS")

    if botaoProfissional:
        st.switch_page("pages/cadastroProfissional.py")

    if botaoCliente:
        st.switch_page("pages/cadastroCliente.py")
        

    if botaoPet:
        st.switch_page("pages/cadastroPet.py")