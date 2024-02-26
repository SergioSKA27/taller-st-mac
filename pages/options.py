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
t.title('✅Mostar opciones al usuario')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)

st.divider()
c1,c2 = st.columns([0.8,0.2])




with c1:
    st.subheader('st.checkbox()')
    '**st.checkbox() es una función que permite mostrar un checkbox en la interfaz web.**'
    '**El método st.checkbox() recibe un argumento label que es el texto que se mostrará al lado del checkbox y un argumento key que es un identificador único para el checkbox.**'
    '**El método st.checkbox() retorna True si el checkbox está seleccionado, de lo contrario retorna False.**'
    with st.echo():
        if st.checkbox('Seleccioname'):
            st.write('Checkbox seleccionado')
        else:
            st.write('Checkbox no seleccionado')
    st.divider()
    st.subheader('st.radio()')
    '**st.radio() es una función que permite mostrar un grupo de radio buttons en la interfaz web.**'
    '**El método st.radio() recibe un argumento label que es el texto que se mostrará al lado del grupo de radio buttons y un argumento options que es una lista con las opciones que se mostrarán en el grupo de radio buttons.**'
    '**El método st.radio() retorna la opción seleccionada por el usuario o el valor por defecto que es la primera opción.**'
    with st.echo():
        option = st.radio('Selecciona una opción', ['Opción 1', 'Opción 2', 'Opción 3'])
        st.write('Opción seleccionada:', option)
    st.divider()
    st.subheader('st.selectbox()')
    '**st.selectbox() es una función que permite mostrar un dropdown en la interfaz web.**'
    '**El método st.selectbox() recibe un argumento label que es el texto que se mostrará al lado del dropdown y un argumento options que es una lista con las opciones que se mostrarán en el dropdown.**'
    '**El método st.selectbox() retorna la opción seleccionada por el usuario o el valor por defecto que es la primera opción.**'
    with st.echo():
        option = st.selectbox('Selecciona una opción', ['Opción 1', 'Opción 2', 'Opción 3'])
        st.write('Opción seleccionada:', option)
    st.divider()
    st.subheader('st.toggle()')
    '**st.toggle() es una función que permite mostrar un toggle en la interfaz web.**'
    '**El método st.toggle() recibe un argumento label que es el texto que se mostrará al lado del toggle y un argumento value que es el valor por defecto del toggle.**'
    '**El método st.toggle() retorna True si el toggle está activado, de lo contrario retorna False.**'
    with st.echo():
        value = st.toggle('Activa o desactiva')
        if value:
            st.write('Toggle activado')
        else:
            st.write('Toggle desactivado')
    st.divider()
    st.subheader('st.multiselect()')
    '**st.multiselect() es una función que permite mostrar un dropdown con la opción de seleccionar múltiples opciones en la interfaz web.**'
    '**El método st.multiselect() recibe un argumento label que es el texto que se mostrará al lado del dropdown y un argumento options que es una lista con las opciones que se mostrarán en el dropdown.**'
    '**El método st.multiselect() retorna una lista con las opciones seleccionadas por el usuario o una lista vacía si no se selecciona ninguna opción.**'
    with st.echo():
        options = st.multiselect('Selecciona una o más opciones', ['Opción 1', 'Opción 2', 'Opción 3'])
        st.write('Opciones seleccionadas:', options)
    st.divider()
    st.markdown('''
    <a href="#717af48f" style="text-align: center; display: block;">Volver al principio</a>
    ''', unsafe_allow_html=True)



with c2:
    with st.container(border=True):
        st.markdown('#### Índice')
        st.markdown('[st.checkbox()](#st-checkbox)')
        st.markdown('[st.radio()](#st-radio)')
        st.markdown('[st.selectbox()](#st-selectbox)')
        st.markdown('[st.toggle()](#st-toggle)')
        st.markdown('[st.multiselect()](#st-multiselect)')
