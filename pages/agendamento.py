import time
import streamlit as st
import pages.menu as menu
import controllers.clienteController as clienteController
import models.cliente as cliente
import controllers.enderecoController as enderecoController
import models.endereco as endereco
import controllers.petController as petController
import models.pet as pet
import pandas as pd

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="auto",
   menu_items=None
)

menu.mostraMenu()

st.title("Cadastro de Clientes")

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

    botao_cadastra = st.form_submit_button("Cadastrar")

    

if botao_cadastra:
    cliente.nome = nome
    cliente.cpf = cpf
    cliente.idade = idade
    cliente.telefone = telefone

    enderecoController.Insere(endereco.Endereco(None, rua, numero, bairro, complemento))

    

    clienteController.Insere(cliente.Cliente(None, nome, cpf, idade, telefone))
    sucesso = st.success("Cliente inserido com sucesso!")
    time.sleep(1)
    sucesso.empty()

st.title("Cadastro de Pets")

with st.form(key="insere_pet"):
    nome = st.text_input(label="Insira o nome do pet:")
    idade = st.number_input(label="Insira a idade do pet:", format= "%d", step=1)
    peso = st.number_input(label="Insira o peso do pet:", format= "%d", step=1)
    raca = st.text_input(label="Insira a raça do pet:")
    clienteId = st.number_input(label="Cliente_ID", format= "%d", step=1)
    botao_cadastra = st.form_submit_button("Cadastrar")

if botao_cadastra:
    pet.nome = nome
    pet.idade = idade
    pet.peso = peso
    pet.raca = raca
    pet.cliente_id = clienteId

    petController.Insere(pet.Pet(None, nome, idade, peso, raca, clienteId))
    sucesso = st.success("Pet inserido com sucesso!")
    time.sleep(1)
    sucesso.empty()

st.title("Agendamento")

with st.form(key="agendamento"):
    dataAgendamento = st.date_input("Escolha uma data:", format="DD/MM/YYYY")
    petEscolhido = st.selectbox(label="Escolha um pet", options=["cachorro", "gato"])
    botao_agenda = st.form_submit_button("Agendar")
    


