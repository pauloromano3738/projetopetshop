import time
import streamlit as st
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

st.title("Agendamento")

with st.form(key="login"):
    data_agendamento = st.date_input("Escolha uma data:", format="DD/MM/YYYY")
    


