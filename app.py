import streamlit as st
import pickle

st.set_page_config(
    page_title="Classificador de Estabilidade de Taludes",
    page_icon="⛰️"
)

st.title("Classificador de Estabilidade de Taludes")

try:
    with open("taludes.pkcls", "rb") as f:
        modelo = pickle.load(f)

    st.success("✅ Modelo carregado com sucesso!")

except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")
