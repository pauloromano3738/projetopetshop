import time
import streamlit as st
import controllers.petController as petController
import models.pet as pet
import pandas as pd

st.title("Cadastro de Profissionais")

with st.form(key="insere_pro"):
    nome = st.text_input(label="Insira o nome do pet:")
    idade = st.number_input(label="Insira a idade do pet:", format= "%d", step=1)
    botao_cadastra = st.form_submit_button("Cadastrar")

botao_mostra = st.button("Mostrar")

if botao_cadastra:
    pet.nome = nome
    pet.idade = idade

    petController.Insere(pet.Pet(0, nome, idade))
    sucesso = st.success("Pet inserido com sucesso!")
    time.sleep(1)
    sucesso.empty()

if botao_mostra:
    pets = []

    for pet in petController.MostraPets():
        pets.append([pet.id, pet.nome, pet.idade])

    df = pd.DataFrame(
        pets,
        columns=['ID', 'Nome:', 'Idade:']
    )

    st.dataframe(df, hide_index=True, use_container_width=True)