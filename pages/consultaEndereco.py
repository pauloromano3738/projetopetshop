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

st.title("Endereços cadastrados")

enderecos = []

for endereco in enderecoController.MostraEnderecos():
    enderecos.append([endereco.id, endereco.rua,  endereco.numero, endereco.bairro, endereco.complemento])

df = pd.DataFrame(
    enderecos,
    columns=['ID', 'Rua:', 'Número:', 'Bairro:', 'Complemento:']
)

st.dataframe(df, hide_index=True, use_container_width=True)