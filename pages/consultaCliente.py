import streamlit as st
import pages.menu as menu
import controllers.clienteController as clienteController
import models.cliente as cliente
import pandas as pd

st.set_page_config(
    page_title="Projeto Petshop",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

menu.mostraMenu()

st.title("Clientes cadastrados")

clientes = clienteController.MostraClientes()
cliente_ids = [cliente.id for cliente in clientes]

# Mostrar tabela de clientes
clientes_dados = []
for cliente in clientes:
    clientes_dados.append([cliente.id, cliente.nome, cliente.cpf, cliente.idade, cliente.telefone, cliente.endereco_id])

df = pd.DataFrame(
    clientes_dados,
    columns=['ID', 'Nome', 'CPF', 'Idade', 'Telefone', 'Endereco_id']
)

# Selectbox para selecionar o ID do cliente
selected_cliente_id = st.selectbox("Selecione o ID do cliente para excluir", cliente_ids)

# Função para estilizar a linha selecionada
def highlight_selected(s):
    return ['background-color: #FF4B4B' if s.ID == selected_cliente_id else '' for _ in s]

# Aplicar estilização na tabela
styled_df = df.style.apply(highlight_selected, axis=1)

st.dataframe(styled_df, hide_index=True, use_container_width=True)

# Botão para excluir o cliente selecionado
if st.button("EXCLUIR", type="primary"):
    clienteController.ExcluiCliente(selected_cliente_id)
    st.success(f"Cliente excluído com sucesso!")
    # Recarregar a página para atualizar os dados
    st.experimental_rerun()
