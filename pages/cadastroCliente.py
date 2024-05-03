import time
import streamlit as st
import pages.menu as menu
import controllers.clienteController as clienteController
import models.cliente as cliente
import pandas as pd

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="collapsed",
   menu_items=None
)

menu.mostraMenu()

st.title("Cadastro de Clientes")

with st.form(key="insere_cliente"):
    nome = st.text_input(label="Insira o nome do cliente:")
    cpf = st.text_input(label="Insira o CPF do cliente:")
    idade = st.number_input(label="Insira a idade do cliente:", format= "%d", step=1)
    telefone = st.number_input(label="Insira o telefone do cliente:", format= "%d", step=1)
    enderecoId = st.number_input(label="Endereco_ID", format= "%d", step=1)
    botao_cadastra = st.form_submit_button("Cadastrar")

botao_mostra = st.button("Mostrar")

if botao_cadastra:
    cliente.nome = nome
    cliente.cpf = cpf
    cliente.idade = idade
    cliente.telefone = telefone
    cliente.endereco_id = enderecoId

    clienteController.Insere(cliente.Cliente(None, nome, cpf, idade, telefone, enderecoId))
    sucesso = st.success("Cliente inserido com sucesso!")
    time.sleep(1)
    sucesso.empty()

if botao_mostra:
    clientes = []

    for cliente in clienteController.MostraClientes():
        clientes.append([cliente.id, cliente.nome,  cliente.cpf, cliente.idade, cliente.telefone, cliente.endereco_id])

    df = pd.DataFrame(
        clientes,
        columns=['ID', 'Nome:', 'CPF:', 'Idade:', 'Telefone:', 'Endereco_id:']
    )

    st.dataframe(df, hide_index=True, use_container_width=True)