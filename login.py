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

    #a váriavel valido recebe um booleano retornado da função verificar_login de loginController 
    valido = loginController.verificar_login(profissional.Profissional(None, None, None, None, login, senha)) #a função verificar_login recebe como parâmetro a instância de um objeto profissional e passa os parâmetros login e senha

    if valido: #se o valor da váriavel for True execute:
        st.success("Login realizado com sucesso!") #a função success mostra uma mensagem de sucesso na tela
        st.switch_page("pages/home.py") #a função switch_page redireciona o sistema para uma página que é passada no parâmetro, que no caso é a pasta pages e o arquivo home.py
    else: #se não
        st.error("Login incorreto. Tente novamente.") #a função error recebe uma string como parâmetro e mostra como mensagem de error na tela

