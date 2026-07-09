import streamlit as st

st.set_page_config(
    page_title="Classificador de Estabilidade de Taludes",
    page_icon="⛰️",
    layout="centered"
)

st.title("⛰️ Classificador de Estabilidade de Taludes")

st.write(
    "Modelo de Machine Learning utilizando Gradient Boosting."
)

st.header("Parâmetros do Talude")

gamma = st.number_input("γ (kN/m³)", value=18.0)

c = st.number_input("c (kPa)", value=20.0)

phi = st.number_input("φ (°)", value=30.0)

beta = st.number_input("β (°)", value=35.0)

H = st.number_input("H (m)", value=20.0)

ru = st.number_input("ru", value=0.20)

if st.button("Classificar"):

    st.success("Os dados foram recebidos com sucesso!")

    st.write("Valores informados:")

    st.write(f"γ = {gamma}")

    st.write(f"c = {c}")

    st.write(f"φ = {phi}")

    st.write(f"β = {beta}")

    st.write(f"H = {H}")

    st.write(f"ru = {ru}")
