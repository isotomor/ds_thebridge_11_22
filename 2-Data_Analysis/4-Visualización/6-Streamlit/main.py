import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cargadores", page_icon=":electric_plug:", layout="wide")

path = "red_recarga_acceso_publico_2021.csv"
df = pd.read_csv(path, sep=";")