import time
import streamlit as st
import pages.menu as menu
import controllers.enderecoController as enderecoController
import models.endereco as endereco
import pandas as pd

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="collapsed",
   menu_items=None
)

menu.mostraMenu()


with st.form(key="insere_endereco"):
    rua = st.text_input(label="Rua:")
    numero = st.number_input(label="Número:", format= "%d", step=1)
    bairro = st.text_input(label="Bairro:")
    complemento = st.text_input(label="Complemento:")
    botao_cadastra = st.form_submit_button("Cadastrar")

if botao_cadastra:
    enderecoController.Insere(endereco.Endereco(None, rua, numero, bairro, complemento))
    sucesso = st.success("Cliente inserido com sucesso!")
    time.sleep(1)
    sucesso.empty()


enderecos = []

for endereco in enderecoController.MostraEnderecos():
    enderecos.append([endereco.id, endereco.rua,  endereco.numero, endereco.bairro, endereco.complemento])

df = pd.DataFrame(
    enderecos,
    columns=['ID', 'Rua:', 'Número:', 'Bairro:', 'Complemento:']
)

st.dataframe(df, hide_index=True, use_container_width=True, height=800)