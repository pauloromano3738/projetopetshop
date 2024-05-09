import streamlit as st
import pages.menu as menu
import controllers.clienteController as clienteController
import models.cliente as cliente
import models.endereco as endereco
import pandas as pd

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="centered",
   initial_sidebar_state="collapsed",
   menu_items=None
)

menu.mostraMenu()

st.title("Clientes cadastrados")

with st.form(key="insere_cliente"):
    st.title("Cadastro de cliente")
    col1, col2 = st.columns([5, 5])
    with col1:
        nomeCliente = st.text_input(label="Insira o nome do cliente:")
        idadeCliente = st.number_input(label="Insira a idade do cliente:", format= "%d", step=1)
        rua = st.text_input(label="Rua:")
        bairro = st.text_input(label="Bairro:")
    with col2:
        cpfCliente = st.text_input(label="Insira o CPF do cliente:")
        telefoneCliente = st.number_input(label="Insira o telefone do cliente:", format= "%d", step=1)
        numero = st.number_input(label="Número:", format= "%d", step=1)
        complemento = st.text_input(label="Complemento:")
    botaoInserir = st.form_submit_button("INSERIR")

if botaoInserir:
    enderecoCriado = endereco.Endereco(None, rua, numero, bairro, complemento)
    clienteCriado = cliente.Cliente(None, nomeCliente, cpfCliente, idadeCliente, telefoneCliente, enderecoCriado)
    clienteController.Insere(clienteCriado, enderecoCriado)

clientesNome = []

# Itera sobre os clientes e adiciona suas informações (id e nome) à lista clientesNome
for cliente in clienteController.MostraClientes():
    clienteInfo = (cliente.id, cliente.nome)  # Usando uma tupla para cada cliente (id, nome)
    clientesNome.append(clienteInfo)

# Cria o selectbox com os nomes dos clientes como rótulos
clienteSelecionado_nome = st.selectbox("Escolha um cliente:", options=[cliente[1] for cliente in clientesNome], index=None)

botaoExcluir = st.button("EXCLUIR", type='primary')

if botaoExcluir:
    # Obtém o id correspondente ao cliente selecionado
    clienteSelecionado_id = [cliente[0] for cliente in clientesNome if cliente[1] == clienteSelecionado_nome][0]
    clienteController.Excluir(clienteSelecionado_id)

clientes = []

for cliente in clienteController.MostraClientes():
    clientes.append([cliente.id, cliente.nome,  cliente.cpf, cliente.idade, cliente.telefone, cliente.endereco_id])

df = pd.DataFrame(
    clientes,
    columns=['ID', 'Nome:', 'CPF:', 'Idade:', 'Telefone:', 'Endereco_id:']
)

st.dataframe(df, hide_index=True, use_container_width=True)