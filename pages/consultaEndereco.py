import time
import streamlit as st
import pages.menu as menu
import controllers.enderecoController as enderecoController
import models.endereco as endereco
import pandas as pd

st.set_page_config(
   page_title="Projeto Petshop",
   page_icon="🐶",
   layout="wide",
   initial_sidebar_state="collapsed",
   menu_items=None
)

menu.mostraMenu()

st.title("Endereços cadastrados")

enderecos = enderecoController.MostraEnderecos()
endereco_ids = [endereco.id for endereco in enderecos]

# Mostrar tabela de endereços
enderecos_dados = []
for endereco in enderecos:
    enderecos_dados.append([endereco.id, endereco.rua, endereco.numero, endereco.bairro, endereco.complemento])

df = pd.DataFrame(
    enderecos_dados,
    columns=['ID', 'Rua', 'Número', 'Bairro', 'Complemento']
)

# Selectbox para selecionar o ID do endereço
selected_endereco_id = st.selectbox("Selecione o ID do endereço para excluir", endereco_ids)

# Função para estilizar a linha selecionada
def highlight_selected(s):
    return ['background-color: #FF4B4B' if s.ID == selected_endereco_id else '' for _ in s]

# Aplicar estilização na tabela
styled_df = df.style.apply(highlight_selected, axis=1)

st.dataframe(styled_df, hide_index=True, use_container_width=True)

# Botão para excluir o endereço selecionado
if st.button("EXCLUIR", type="primary"):
    enderecoController.ExcluiEndereco(selected_endereco_id)
    st.success(f"Endereço excluído com sucesso!")
    # Recarregar a página para atualizar os dados
    st.experimental_rerun()
