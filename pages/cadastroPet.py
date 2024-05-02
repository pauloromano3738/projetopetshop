import time
import streamlit as st
import controllers.petController as petController
import models.pet as pet
import pandas as pd

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="collapsed",
   menu_items=None
)

st.title("Cadastro de Pets")

with st.form(key="insere_pet"):
    nome = st.text_input(label="Insira o nome do pet:")
    idade = st.number_input(label="Insira a idade do pet:", format= "%d", step=1)
    peso = st.number_input(label="Insira o peso do pet:", format= "%d", step=1)
    raca = st.text_input(label="Insira a raça do pet:")
    clienteId = st.number_input(label="Cliente_ID", format= "%d", step=1)
    botao_cadastra = st.form_submit_button("Cadastrar")

botao_mostra = st.button("Mostrar")

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

if botao_mostra:
    pets = []

    for pet in petController.MostraPets():
        pets.append([pet.id, pet.nome,  pet.idade, pet.peso, pet.raca, pet.cliente_id])

    df = pd.DataFrame(
        pets,
        columns=['ID', 'Nome:', 'Idade:', 'Peso:', 'Raça:', 'Cliente_id:']
    )

    st.dataframe(df, hide_index=True, use_container_width=True)