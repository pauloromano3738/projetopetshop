import datetime as data
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

containerCliente = st.empty()

with containerCliente.container():

    st.title("Cadastro de Cliente")

    with st.form(key="insere_cliente"):

        col1, col2 = st.columns([5, 5])
        with col1:
            nome = st.text_input(label="Insira o nome do cliente:")
            idade = st.number_input(label="Insira a idade do cliente:", format= "%d", step=1)
            rua = st.text_input(label="Rua:")
            bairro = st.text_input(label="Bairro:")
        with col2:
            cpf = st.text_input(label="Insira o CPF do cliente:")
            telefone = st.number_input(label="Insira o telefone do cliente:", format= "%d", step=1)
            numero = st.number_input(label="Número:", format= "%d", step=1)
            complemento = st.text_input(label="Complemento:")

        botao_cadastra_cliente = st.form_submit_button("Cadastrar")

    if botao_cadastra_cliente:
        clienteController.Insere(cliente.Cliente(None, nome, cpf, idade, telefone, endereco), 
                                 endereco.Endereco(None, rua, numero, bairro, complemento))
        sucesso = st.success("Cliente inserido com sucesso!")
        time.sleep(1)
        sucesso.empty()
        containerCliente.empty()









containerPet = st.empty()

with containerPet.container(): 

    st.title("Cadastro de Pet")
    with st.form(key="insere_pet"):

        col1, col2 = st.columns([5, 5])
        with col1:
            nome = st.text_input(label="Insira o nome do pet:")
            peso = st.number_input(label="Insira o peso do pet:", format= "%d", step=1)

        with col2:
            idade = st.number_input(label="Insira a idade do pet:", format= "%d", step=1)
            raca = st.text_input(label="Insira a raça do pet:")
        clienteId = st.number_input(label="Cliente_ID", format= "%d", step=1)
        botao_cadastra_pet = st.form_submit_button("Cadastrar")

    if botao_cadastra_pet:

        petController.Insere(pet.Pet(None, nome, idade, peso, raca, clienteId))
        sucesso = st.success("Pet inserido com sucesso!")
        time.sleep(1)
        sucesso.empty()
        containerPet.empty()









containerAgendamento = st.empty()

with containerAgendamento.container():
                
    st.title("Agendamento")

    with st.form(key="agendamento"):
        col1, col2 = st.columns([5, 5])
        with col1:
            dataAgendamento = st.date_input("Escolha uma data:", format="DD/MM/YYYY")
        with col2:
            horaAgendamento = st.time_input("Escolha o horário:", value='now')
        profissional = st.selectbox(label="Profissional responsável:", options=['admin'])
        botao_agenda = st.form_submit_button("Agendar")

    if botao_agenda:
        DataHoraCombinadas = data.datetime.combine(dataAgendamento, horaAgendamento)
        agendamentoController.Insere(agendamento.Agendamento(None, "Em andamento", DataHoraCombinadas, profissional.id))
        print(DataHoraCombinadas)
        containerAgendamento.empty()
        


