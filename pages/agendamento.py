import datetime
import time
import streamlit as st
import pages.menu as menu
import controllers.clienteController as clienteController
import models.cliente as cliente
import models.endereco as endereco
import controllers.petController as petController
import models.pet as pet
import controllers.agendamentoController as agendamentoController
import models.agendamento as agendamento
import pandas as pd

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
        idadeCliente = st.number_input(label="Insira a idade do cliente:", format= "%d", step=1)
        rua = st.text_input(label="Rua:")
        bairro = st.text_input(label="Bairro:")
    with col2:
        cpfCliente = st.text_input(label="Insira o CPF do cliente:")
        telefoneCliente = st.number_input(label="Insira o telefone do cliente:", format= "%d", step=1)
        numero = st.number_input(label="Número:", format= "%d", step=1)
        complemento = st.text_input(label="Complemento:")


    st.title("Cadastro de pet")
    col3, col4 = st.columns([5, 5])
    
    with col3:
        nomePet = st.text_input(label="Insira o nome do pet:")
        pesoPet = st.number_input(label="Insira o peso do pet:", format= "%d", step=1)
    with col4:
        idadePet = st.number_input(label="Insira a idade do pet:", format= "%d", step=1)
        racaPet = st.text_input(label="Insira a raça do pet:")

    st.title("Agendamento")

    col5, col6 = st.columns([5, 5])
    with col5:
        hoje = datetime.date.today()
        dataAgendamento = st.date_input("Escolha uma data:", format="DD/MM/YYYY", min_value=hoje)
        profissionalID = st.text_input("Dígite o id do profissional responsável:",)
    with col6:
        horaAgendamento = st.time_input("Escolha o horário:", datetime.time(8))

    botao_agendar = st.form_submit_button("Agendar")

    if botao_agendar:
        enderecoCriado = endereco.Endereco(None, rua, numero, bairro, complemento)
        clienteCriado = cliente.Cliente(None, nomeCliente, cpfCliente, idadeCliente, telefoneCliente, enderecoCriado)
        petCriado = pet.Pet(None, nomePet, idadePet, pesoPet, racaPet, clienteCriado)
        DataHoraCombinadas = datetime.datetime.combine(dataAgendamento, horaAgendamento)
        agendamentoCriado = agendamento.Agendamento(None, "Em Andamento", DataHoraCombinadas, profissionalID, None, None)
        agendamentoController.Insere(clienteCriado, enderecoCriado, petCriado, agendamentoCriado)
        sucesso = st.success("Agendamento realizado com sucesso!")
        time.sleep(1)
        sucesso.empty()