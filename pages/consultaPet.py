import streamlit as st
import pages.menu as menu
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

menu.mostraMenu()

pets = []

for pet in petController.MostraPets():
    pets.append([pet.id, pet.nome,  pet.idade, pet.peso, pet.raca, pet.cliente_id])

df = pd.DataFrame(
    pets,
    columns=['ID', 'Nome:', 'Idade:', 'Peso:', 'Raça:', 'Cliente_id:']
)

st.dataframe(df, hide_index=True, use_container_width=True, height=800)

