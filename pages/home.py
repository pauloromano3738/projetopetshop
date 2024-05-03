import streamlit as st
import pages.menu as menu

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="collapsed",
   menu_items=None
)

menu.mostraMenu()

st.title("BEM-VINDO *NOME*")
st.title("Agendamentos do dia:")
st.multiselect('Multiselect', [1,2,3])