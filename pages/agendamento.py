import datetime
import time
import streamlit as st
import pages.menu as menu
import models.cliente as cliente
import models.endereco as endereco
import models.pet as pet
import controllers.profissionalController as profissionalController
import models.profissional as profissional
import controllers.agendamentoController as agendamentoController
import models.agendamento as agendamento

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="auto",
   menu_items=None
)

menu.mostraMenu()

with st.form(key="insere_agendamento"):
    st.title("Cadastro de cliente")
    col1, col2 = st.columns([5, 5])
    with col1:
        nomeCliente = st.text_input(label="Insira o nome do cliente:")
        idadeCliente = st.number_input(label="Insira a idade do cliente:", format= "%d", step=1, value=None)
        rua = st.text_input(label="Rua:")
        bairro = st.text_input(label="Bairro:")
    with col2:
        cpfCliente = st.text_input(label="Insira o CPF do cliente:", max_chars=11)
        telefoneCliente = st.text_input(label="Insira o telefone do cliente:", max_chars=11)
        numero = st.number_input(label="Número:", format= "%d", step=1, value=None)
        complemento = st.text_input(label="Complemento:")


    st.title("Cadastro de pet")

    col3, col4 = st.columns([5, 5])
    with col3:
        nomePet = st.text_input(label="Insira o nome do pet:")
        pesoPet = st.number_input(label="Insira o peso do pet:", format= "%f", placeholder="em kilos", value=None)
    with col4:
        idadePet = st.number_input(label="Insira a idade do pet:", format= "%d", step=1, placeholder="em anos", value=None)
        racaPet = st.text_input(label="Insira a raça do pet:")

    st.title("Agendamento")

    col5, col6 = st.columns([5, 5])
    with col5:
        hoje = datetime.date.today()
        dataAgendamento = st.date_input("Escolha uma data:", format="DD/MM/YYYY", min_value=hoje)
        profissionaisNome = []

        # Itera sobre os clientes e adiciona suas informações (id e nome) à lista clientesNome
        for profissional in profissionalController.MostraProfissionais():
            profissionalInfo = (profissional.id, profissional.nome)  # Usando uma tupla para cada cliente (id, nome)
            profissionaisNome.append(profissionalInfo)

        # Cria o selectbox com os nomes dos clientes como rótulos
        profissionalSelecionado_nome = st.selectbox("Escolha um profissional:", options=[profissional[1] for profissional in profissionaisNome], index=0)
        profissionalSelecionado_id = [profissional[0] for profissional in profissionaisNome if profissional[1] == profissionalSelecionado_nome][0]

    with col6:
        horaAgendamento = st.time_input("Escolha o horário:", datetime.time(8))

    botao_agendar = st.form_submit_button("Agendar")

    if botao_agendar:
        enderecoCriado = endereco.Endereco(None, rua, numero, bairro, complemento)
        clienteCriado = cliente.Cliente(None, nomeCliente, cpfCliente, idadeCliente, telefoneCliente, enderecoCriado)
        petCriado = pet.Pet(None, nomePet, idadePet, pesoPet, racaPet, clienteCriado)
        DataHoraCombinadas = datetime.datetime.combine(dataAgendamento, horaAgendamento)
        agendamentoCriado = agendamento.Agendamento(None, "Em Andamento", DataHoraCombinadas, profissionalSelecionado_id, None, None)
        agendamentoController.Insere(clienteCriado, enderecoCriado, petCriado, agendamentoCriado)
        sucesso = st.success("Agendamento realizado com sucesso!")
        time.sleep(1)
        sucesso.empty()