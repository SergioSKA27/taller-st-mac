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
t.title('🎬Mostar archivos multimedia')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)
st.divider()
c1,c2 = st.columns([0.8,0.2])

with c1:
    st.subheader('st.image()')
    '**st.image() es una función que permite mostrar una imagen en la interfaz web.**'
    '**El método st.image() recibe un argumento image que es la imagen que se mostrará en la interfaz web, un argumento caption que es el texto que se mostrará debajo de la imagen y un argumento use_column_width que si es True ajusta el ancho de la imagen al ancho de la columna.**'
    '**Podemos mostrar imágenes de la web o imágenes locales pasando la ruta de la imagen o el enlace de la imagen, adicionalmente podemos mostrar imágenes de numpy arrays o bytes.**'
    with st.echo():
        st.image("https://source.unsplash.com/random/720x480?machine-learning,programming,python,mathematics", caption='Imagen aleatoria', use_column_width=False)

    st.divider()

    st.subheader('st.audio()')
    '**st.audio() es una función que permite mostrar un audio en la interfaz web.**'
    '**El método st.audio() recibe un argumento audio que es el audio que se mostrará en la interfaz web, un argumento format que es el formato del audio y un argumento start_time que es el tiempo en el que se iniciará el audio.**'
    '**Podemos mostrar audios de la web o audios locales pasando la ruta del audio o el enlace del audio, adicionalmente podemos mostrar audios de numpy arrays o bytes.**'
    with st.echo():
        st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg", format='audio/ogg', start_time=0)

    st.divider()
    st.subheader('st.video()')
    '**st.video() es una función que permite mostrar un video en la interfaz web.**'
    '**El método st.video() recibe un argumento video que es el video que se mostrará en la interfaz web, un argumento format que es el formato del video y un argumento start_time que es el tiempo en el que se iniciará el video.**'
    '**Podemos mostrar videos de la web o videos locales pasando la ruta del video o el enlace del video, adicionalmente podemos mostrar videos de numpy arrays o bytes.**'
    with st.echo():
        st.video("https://www.youtube.com/watch?v=B4LvDiIi128", format='video/mp4', start_time=0)

    st.markdown('''
    <a href="#10876363" style="text-align: center; display: block;">Volver al principio</a>
    ''', unsafe_allow_html=True)

with c2:
    with st.container(border=True):
        st.markdown('#### Índice')
        st.markdown('[st.image()](#st-image)')
        st.markdown('[st.audio()](#st-audio)')
        st.markdown('[st.video()](#st-video)')
