import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime

st.set_page_config(layout="wide")

st.markdown('''
<style>
#MainMenu, header {visibility: hidden;}
.st-emotion-cache-r421ms {
  border: 1px solid rgba(49, 51, 63, 0.2);
  border-radius: 0.5rem;
  padding: 1rem;
  position: fixed;
  width: 20%;
}
</style>
''', unsafe_allow_html=True)
t,indx = st.columns([0.8,0.2])
t.title('🗃️Trabajando con archivos')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)

st.divider()
c1,c2 = st.columns([0.8,0.2])

with c1:
    st.subheader('st.file_uploader()')
    '**st.file_uploader() es una función que permite mostrar un input para subir archivos en la interfaz web.**'
    '**El método st.file_uploader() recibe un argumento label que es el texto que se mostrará al lado del input para subir archivos y un argumento type que es el tipo de archivo que se puede subir.**'
    '**El método st.file_uploader() retorna un objeto UploadedFile  que contiene el archivo subido por el usuario.**'

    with st.echo():
        uploaded_file = st.file_uploader('Sube un archivo', type=['csv', 'txt'])
        # Si el archivo fue subido podemos leerlo con pandas y mostrarlo en la interfaz web
        if uploaded_file is not None:
            st.write('Archivo subido:', uploaded_file.name)
            df = pd.read_csv(uploaded_file)
            st.write(df)

    st.divider()
    st.subheader('st.download_button()')
    '**st.download_button() es una función que permite mostrar un botón para descargar archivos en la interfaz web.**'
    '**El método st.download_button() recibe un argumento label que es el texto que se mostrará en el botón, un argumento data que es el contenido del archivo que se descargará y un argumento file_name que es el nombre del archivo que se descargará.**'
    with st.echo():
        data = pd.DataFrame({
            'first column': [1, 2, 3, 4],
            'second column': [10, 20, 30, 40],
        })
        st.download_button('Descargar archivo', data.to_csv(), file_name='data.csv')

    st.divider()
    st.markdown('''
    <a href="#cd2f59d4" style="text-align: center; display: block;">Volver al principio</a>
    ''', unsafe_allow_html=True)


with c2:
    with st.container(border=True):
        st.markdown('#### Índice')
        st.markdown('[st.file_uploader()](#st-file-uploader)')
        st.markdown('[st.download_button()](#st-download-button)')
