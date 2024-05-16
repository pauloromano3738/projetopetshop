import streamlit as st

def mostraMenu():
    st.sidebar.image(image='pages/logo.png', output_format="PNG")

    st.sidebar.header("MENU", divider="red")

    with st.container():

        botaoProfissional = st.sidebar.button("CONSULTAR PROFISSIONAIS", use_container_width=True)
        botaoCliente = st.sidebar.button("CONSULTAR CLIENTES", use_container_width=True)
        botaoEndereco = st.sidebar.button("CONSULTAR ENDEREÇOS", use_container_width=True)
        botaoPet = st.sidebar.button("CONSULTAR PETS", use_container_width=True)
        botaoConsultarAgendamento = st.sidebar.button("CONSULTAR AGENDAMENTOS", use_container_width=True)
        botaoAgendamento = st.sidebar.button("REALIZAR AGENDAMENTO", use_container_width=True)

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
            st.switch_page("pages/agendamentoPagina.py")
