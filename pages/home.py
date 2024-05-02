import streamlit as st

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="collapsed",
   menu_items=None
)

st.sidebar.title('MENU')
botaoProfissional = st.sidebar.button("PROFISSIONAIS")
botaoPet = st.sidebar.button("PETS")
st.sidebar.button("AGENDAMENTOS")

if botaoProfissional:
    st.switch_page("pages/cadastroProfissional.py")

if botaoPet:
    st.switch_page("pages/cadastroPet.py")

st.title("BEM-VINDO *NOME*")
st.title("Agendamentos do dia:")