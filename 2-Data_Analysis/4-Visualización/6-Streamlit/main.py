import streamlit as st
import pandas as pd
from PIL import Image # !pip install Pillow

st.set_page_config(page_title="Cargadores", page_icon=":electric_plug:", layout="wide")

path = "data/red_recarga_acceso_publico_2021.csv"
df = pd.read_csv(path, sep=";")
df.rename(columns={"latidtud":"lat", "longitud":"lon"}, inplace=True)

img = Image.open('data/puntos-recarga-madrid.jpg')

st.title("Cargadores Madrid")

menu = st.sidebar.selectbox("Selecciona la página", ['Home','Datos','Filtros'])

if menu == "Home":
    st.image(img, use_column_width='auto')
    with st.expander('Quieres saber más?'):
        st.write("Es una solución factible para reducir emisiones en la ciudad")
elif menu == "Datos":
    st.write(df.head(5))
    st.map(df)