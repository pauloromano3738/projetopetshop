import streamlit as st #importa a biblioteca do streamlit como st
import controllers.loginController as loginController #importa loginController da pasta controllers como loginController
import models.profissional as profissional #importa profissional da pasta models como profissional

#executa a função set_page_config da biblioteca streamlit, que serve para configurar algumas parâmetros da página.
st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="auto",
   menu_items=None
)

#container
st.title("Login") #executa a função title da biblioteca streamlit, que adiciona um texto formato em título na página.

with st.form(key="login"): #usando a notação with 
    login = st.text_input(label="Insira o seu login:")
    senha = st.text_input(label="Insira a sua senha:", type="password", max_chars=8)
    botao_login = st.form_submit_button("Entrar")

if botao_login: #se botao_login for clicado execute:

    #a váriavel valido recebe um booleano 
    valido = loginController.verificar_login(profissional.Profissional(None, None, None, None, login, senha))

    if valido:
        st.success("Login realizado com sucesso!")
        st.switch_page("pages/home.py")
    else:
        st.error("Login incorreto. Tente novamente.")

