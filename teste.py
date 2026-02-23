import streamlit as st
import pandas as pd

st.set_page_config(page_title="teste", page_icon="💻")

st.title("title")  # Título da página
st.header("1. header") # Cabeçalho 1 (h1)
st.subheader("2. subheader") # Cabeçalho 2 (h2)
st.text("text") # Texto simples (cru)
st.write("write") # Escreve texto, números, dataframes, etc. de forma inteligente
st.text_input("text_imput") # Campo de texto para entrada do usuário
st.text_area("text_area") # Área de texto para entrada do usuário
st.markdown("markdown") # Permite usar sintaxe Markdown para formatar o texto
st.code("code") # Exibe código formatado
st.latex(r"latex") # Exibe fórmulas matemáticas usando LaTeX
st.caption("caption") # Texto de legenda
st.metric("metric", 1000) # Exibe uma métrica com um valor
st.success("Teste")
st.info("Teste")
st.warning("Teste")
st.error("Teste")
st.json({"Teste": "Teste"})
st.dataframe({"Teste": ["Teste"]})
st.table({"Teste": ["Teste"]})
st.metric("Teste", "Teste")
st.progress(0.5)
st.spinner("Teste")
st.balloons()
st.snow()
st.toast("Teste")
st.columns(2)
st.area_chart({"Teste": [1, 2, 3]})
st.altair_chart({"Teste": [1, 2, 3]}) 
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.audio_input("audio_input")
st.__annotations__

st.header("Diferença visual abaixo:")
