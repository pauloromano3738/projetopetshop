import streamlit as st
import pages.menu as menu
import controllers.petController as petController
import models.pet as pet
import pandas as pd

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="wide",
   initial_sidebar_state="collapsed",
   menu_items=None
)

menu.mostraMenu()

st.title("Pets cadastrados")

pets = petController.MostraPets()
pet_ids = [pet.id for pet in pets]

# Mostrar tabela de pets
pets_dados = []
for pet in pets:
    pets_dados.append([pet.id, pet.nome, pet.idade, pet.peso, pet.raca, pet.cliente_id])

df = pd.DataFrame(
    pets_dados,
    columns=['ID', 'Nome', 'Idade', 'Peso', 'Raça', 'Cliente_id']
)

# Selectbox para selecionar o ID do pet
selected_pet_id = st.selectbox("Selecione o ID do pet para excluir", pet_ids)

# Função para estilizar a linha selecionada
def highlight_selected(s):
    return ['background-color: #FF4B4B' if s.ID == selected_pet_id else '' for _ in s]

# Aplicar estilização na tabela
styled_df = df.style.apply(highlight_selected, axis=1)

st.dataframe(styled_df, hide_index=True, use_container_width=True)

# Botão para excluir o pet selecionado
if st.button("EXCLUIR", type="primary"):
    petController.ExcluiPet(selected_pet_id)
    st.success(f"Pet excluído com sucesso!")
    # Recarregar a página para atualizar os dados
    st.experimental_rerun()
