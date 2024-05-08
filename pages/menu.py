import streamlit as st

def mostraMenu():
    st.sidebar.title('MENU')
    
    botaoProfissional = st.sidebar.button("CONSULTAR PROFISSIONAIS")
    botaoCliente = st.sidebar.button("CONSULTAR CLIENTES")
    botaoEndereco = st.sidebar.button("CONSULTAR ENDEREÇOS")
    botaoPet = st.sidebar.button("CONSULTAR PETS")
    botaoConsultarAgendamento = st.sidebar.button("CONSULTAR AGENDAMENTOS")
    botaoAgendamento = st.sidebar.button("REALIZAR AGENDAMENTO")

    if botaoProfissional:
        st.switch_page("pages/cadastroProfissional.py")

    if botaoCliente:
        st.switch_page("pages/consultaCliente.py")

    if botaoEndereco:
        st.switch_page("pages/consultaEndereco.py")
        
    if botaoPet:
        st.switch_page("pages/consultaPet.py")

    if botaoConsultarAgendamento:
        st.switch_page("pages/consultaAgendamento.py")

    if botaoAgendamento:
        st.switch_page("pages/agendamento.py")
