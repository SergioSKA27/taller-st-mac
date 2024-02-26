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
t.title('🎚️Sliders')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)

st.divider()
c1,c2 = st.columns([0.8,0.2])

with c1:
    st.subheader('st.slider()')
    '**st.slider() es una función que permite mostrar un slider en la interfaz web.**'
    '**El método st.slider() recibe un argumento label que es el texto que se mostrará al lado del slider, un argumento min_value que es el valor mínimo del slider, un argumento max_value que es el valor máximo del slider y un argumento value que es el valor por defecto del slider.**'
    '**El método st.slider() retorna el valor seleccionado por el usuario o el valor por defecto.**'
    with st.echo():
        value = st.slider('Selecciona un valor', min_value=0, max_value=100, value=50)
        st.write('Valor seleccionado:', value)
    '**Opcionalmente, podemos crear un slider de rango con el argumento value que recibe una lista con los valores mínimo y máximo del slider.**'
    with st.echo():
        value = st.slider('Selecciona un rango de valores', min_value=0, max_value=100, value=[25, 75])
        st.write('Rango seleccionado:', value)
    st.divider()
    st.subheader('st.select_slider()')
    '**st.select_slider() es una función que permite mostrar un slider con opciones en la interfaz web.**'
    '**El método st.select_slider() recibe un argumento label que es el texto que se mostrará al lado del slider, un argumento options que es una lista con las opciones que se mostrarán en el slider, un argumento value que es el valor por defecto del slider.**'
    '**El método st.select_slider() retorna el valor seleccionado por el usuario o el valor por defecto.**'
    with st.echo():
        value = st.select_slider('Selecciona un valor', options=['Opción 1', 'Opción 2', 'Opción 3'], value='Opción 2')
        st.write('Valor seleccionado:', value)
    st.divider()
    st.markdown('''
    <a href="#d62cfdc3" style="text-align: center; display: block;">Volver al principio</a>
    ''', unsafe_allow_html=True)


with c2:
    with st.container(border=True):
        st.markdown('#### Índice')
        st.markdown('[st.slider()](#st-slider)')
        st.markdown('[st.select_slider()](#st-select-slider)')
