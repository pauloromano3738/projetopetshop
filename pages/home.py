import streamlit as st

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="collapsed",
   menu_items=None
)

st.sidebar.title('MENU')
st.sidebar.button("PROFISSIONAIS")
botaoCadastrarPet = st.sidebar.button("PETS")
st.sidebar.button("AGENDAMENTOS")

if botaoCadastrarPet:
    st.switch_page("pages/cadastroPet.py")

st.title("BEM-VINDO *NOME*")
st.title("Agendamentos do dia:")