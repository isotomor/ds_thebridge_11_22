import streamlit as st
import pandas as pd
from PIL import Image # !pip install Pillow
import streamlit.components.v1 as components

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
    file = open('data/heatmap.html', 'r')
    hm = file.read()
    components.html(hm, height=300)

    cargadores_distrito = df.groupby("DISTRITO")['Nº CARGADORES'].sum().sort_values(ascending=False)

    st.write(cargadores_distrito)

    st.bar_chart(cargadores_distrito)

    l_distritos = list(df['DISTRITO'].unique())
    filtro = st.sidebar.selectbox("Selecciona un distrito", l_distritos)
    if filtro:
        df_filtered = df[df['DISTRITO'] == filtro]
        st.write(df_filtered)
        st.map(df_filtered)
    else:
        st.write(df.head(10))


elif menu == "Filtros":
    l_distritos = list(df['DISTRITO'].unique())
    filtro = st.sidebar.selectbox("Selecciona un distrito", l_distritos)
    if filtro:
        df_filtered = df[df['DISTRITO'] == filtro]
        st.write(df_filtered)
    else:
        st.write(df.head(10))

