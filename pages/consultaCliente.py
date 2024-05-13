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

clientes = []

for cliente in clienteController.MostraClientes():
    clientes.append([cliente.id, cliente.nome,  cliente.cpf, cliente.idade, cliente.telefone, cliente.endereco_id])

df = pd.DataFrame(
    clientes,
    columns=['ID', 'Nome:', 'CPF:', 'Idade:', 'Telefone:', 'Endereco_id:']
)

st.dataframe(df, hide_index=True, use_container_width=True)