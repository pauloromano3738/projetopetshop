import streamlit as st

def mostraMenu():
    st.sidebar.title('MENU')
    botaoProfissional = st.sidebar.button("PROFISSIONAIS")
    botaoEndereco = st.sidebar.button("ENDEREÇOS")
    botaoCliente = st.sidebar.button("CLIENTES")
    botaoPet = st.sidebar.button("PETS")
    botaoAgendamento = st.sidebar.button("AGENDAMENTOS")

    if botaoProfissional:
        st.switch_page("pages/cadastroProfissional.py")

    if botaoEndereco:
        st.switch_page("pages/consultaEndereco.py")

    if botaoCliente:
        st.switch_page("pages/consultaCliente.py")
        
    if botaoPet:
        st.switch_page("pages/consultaPet.py")

    if botaoAgendamento:
        st.switch_page("pages/agendamento.py")