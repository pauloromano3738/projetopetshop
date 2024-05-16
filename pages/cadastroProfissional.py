import time
import streamlit as st
import pages.menu as menu
import controllers.profissionalController as profissionalController
import models.profissional as profissional
import pandas as pd

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="wide",
   initial_sidebar_state="collapsed",
   menu_items=None
)

menu.mostraMenu()

st.title("Cadastro de Profissionais")

with st.form(key="insere_profissional"):
    col1, col2 = st.columns([5, 5])

    with col1:
        nome = st.text_input(label="Insira o nome do profissional:")
        ocupacao = st.selectbox(label="Insira a ocupação do profissional:", options=["atendente", "tosador", "médico veterinário"])
        senha = st.text_input(label="Insira a senha para o profissional:", type="password", max_chars=8)
    with col2:
        cpf = st.text_input(label="Insira o CPF do profissional:", max_chars=11)
        login = st.text_input(label="Insira o login para o profissional:")

    botao_cadastra = st.form_submit_button("Cadastrar")

botao_mostra = st.button("Mostrar")

if botao_cadastra:
    profissionalController.Insere(profissional.Profissional(None, nome, cpf, ocupacao, login, senha))
    sucesso = st.success("Profissional inserido com sucesso!")
    time.sleep(1)
    sucesso.empty()

if botao_mostra:
    profissionais = []

    for profissional in profissionalController.MostraProfissionais():
        profissionais.append([profissional.id, profissional.nome, profissional.cpf, profissional.ocupacao])

    df = pd.DataFrame(
        profissionais,
        columns=['ID', 'Nome:', 'CPF:', 'Ocupação']
    )

    st.dataframe(df, hide_index=True, use_container_width=True)