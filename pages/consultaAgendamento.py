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

agendamentos = agendamentoController.MostraAgendamentos()
agendamento_ids = [agendamento.id for agendamento in agendamentos]

# Mostrar tabela de agendamentos
agendamentos_dados = []
for agendamento in agendamentos:
    agendamentos_dados.append([agendamento.id, agendamento.status, agendamento.data, agendamento.profissional_id, agendamento.cliente_id, agendamento.pet_id])

df = pd.DataFrame(
    agendamentos_dados,
    columns=['ID', 'Status', 'Data', 'Profissional_id', 'Cliente_id', 'Pet_id']
)

df['Data'] = pd.to_datetime(df['Data']).dt.strftime("%d/%m/%Y %I:%M %p")

# Selectbox para selecionar o ID do agendamento
selected_agendamento_id = st.selectbox("Selecione o ID do agendamento para excluir", agendamento_ids)

# Função para estilizar a linha selecionada
def highlight_selected(s):
    return ['background-color: #FF4B4B' if s.ID == selected_agendamento_id else '' for _ in s]

# Aplicar estilização na tabela
styled_df = df.style.apply(highlight_selected, axis=1)

st.dataframe(styled_df, hide_index=True, use_container_width=True)

botaoExcluir = st.button(label="EXCLUIR", type="primary")

# Botão para excluir o agendamento selecionado
if botaoExcluir:
    agendamentoController.ExcluiAgendamento(selected_agendamento_id)
    st.success(f"Agendamento excluído com sucesso!")
    # Recarregar a página para atualizar os dados
    st.experimental_rerun()
