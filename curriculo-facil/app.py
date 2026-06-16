import streamlit as st

from gerador_pdf import gerar_pdf

st.title("Currículo Fácil")

st.write("Preencha suas informações abaixo.")

nome = st.text_input("Nome")

email = st.text_input("E-mail")

telefone = st.text_input("Telefone")

objetivo = st.text_area("Objetivo Profissional")

formacao = st.text_area("Formação")

cursos = st.text_area("Cursos")

projetos = st.text_area("Projetos")

if st.button("Gerar Currículo"):

    gerar_pdf(
        nome,
        email,
        telefone,
        objetivo,
        formacao,
        cursos,
        projetos
    )

    st.success("Currículo PDF criado com sucesso!")