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

df = pd.DataFrame(columns=['name','age','color'])
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
}

result = st.data_editor(df, column_config = config, num_rows='dynamic')

if st.button('Get results'):
    st.write(result)

st.dataframe(df, column_config= config ,hide_index=True, use_container_width=True)