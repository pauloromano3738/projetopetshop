import streamlit as st
import pages.menu as menu
import controllers.agendamentoController as agendamentoController
import models.agendamento as agendamento
import pandas as pd

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="collapsed",
   menu_items=None
)

menu.mostraMenu()

st.title("Agendamentos cadastrados")

agendamentos = []

for agendamento in agendamentoController.MostraAgendamentos():
    agendamentos.append([agendamento.id, agendamento.status,  agendamento.data, agendamento.profissional_id, agendamento.cliente_id, agendamento.pet_id])

df = pd.DataFrame(
    agendamentos,
    columns=['ID', 'Status:', 'Data:', 'Profissional_id:', 'Cliente_id:', 'Pet_id:']
)

st.dataframe(df, column_config= {'Data:': st.column_config.DatetimeColumn('Data:', format="DD/MM/YYYY HH:mm a")}, hide_index=True, use_container_width=True)