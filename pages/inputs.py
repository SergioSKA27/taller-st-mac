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
t.title('📲Inputs')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)
st.divider()
c1,c2 = st.columns([0.8,0.2])




with c1:
    st.subheader('st.text_input()')
    '**st.text_input() es una función que permite mostrar un input de texto en la interfaz web.**'
    '**El método st.text_input() recibe un argumento label que es el texto que se mostrará al lado del input de texto y un argumento value que es el valor por defecto del input de texto.**'
    '**El método st.text_input() retorna el valor ingresado por el usuario o el valor por defecto.**'
    with st.echo():
        value = st.text_input('Ingresa un texto', value='Texto por defecto')
        st.write('Texto ingresado:', value)

    st.divider()

    st.subheader('st.number_input()')
    '**st.number_input() es una función que permite mostrar un input de número en la interfaz web.**'
    '**El método st.number_input() recibe un argumento label que es el texto que se mostrará al lado del input de número, un argumento min_value que es el valor mínimo del input de número, un argumento max_value que es el valor máximo del input de número y un argumento value que es el valor por defecto del input de número.**'
    '**El método st.number_input() retorna el valor ingresado por el usuario o el valor por defecto.**'
    with st.echo():
        value = st.number_input('Ingresa un número', min_value=0, max_value=100, value=50)
        st.write('Número ingresado:', value)

    '**Notar que el input leerá el valor ingresado de acuerdo al tipo de dato del valor por defecto.**'
    with st.echo():
        intn = st.number_input('Ingresa un número entero', value=50)
        fnum = st.number_input('Ingresa un número flotante', value=50.0)
        st.write('Número entero ingresado:', intn)
        st.write('Número flotante ingresado:', fnum)

    st.divider()
    st.subheader('st.text_area()')
    '**st.text_area() es una función que permite mostrar un input de texto de múltiples líneas en la interfaz web.**'
    '**El método st.text_area() recibe un argumento label que es el texto que se mostrará al lado del input de texto de múltiples líneas y un argumento value que es el valor por defecto del input de texto de múltiples líneas.**'
    '**El método st.text_area() retorna el valor ingresado por el usuario o el valor por defecto.**'
    with st.echo():
        value = st.text_area('Ingresa un texto de múltiples líneas', value='Texto por defecto')
        st.write('Texto ingresado:', value)

    st.divider()
    st.subheader('st.date_input()')
    st.write('**st.date_input() es una función que permite mostrar un input de fecha en la interfaz web.**')
    st.write('**El método st.date_input() recibe un argumento label que es el texto que se mostrará al lado del input de fecha y un argumento value que es el valor por defecto del input de fecha.**')
    st.write('**El método st.date_input() retorna el valor ingresado por el usuario o el valor por defecto.**')
    st.write('**El valor ingresado por el usuario es un objeto de tipo datetime.date.**')
    with st.echo():
        value = st.date_input('Ingresa una fecha', value=datetime.date(2021, 1, 1))
        st.write('Fecha ingresada:', value)

    st.divider()
    st.subheader('st.time_input()')
    '**st.time_input() es una función que permite mostrar un input de tiempo en la interfaz web.**'
    '**El método st.time_input() recibe un argumento label que es el texto que se mostrará al lado del input de tiempo y un argumento value que es el valor por defecto del input de tiempo.**'
    '**El método st.time_input() retorna el valor ingresado por el usuario o el valor por defecto.**'
    '**El valor ingresado por el usuario es un objeto de tipo datetime.time.**'
    with st.echo():
        value = st.time_input('Ingresa una hora', value=datetime.time(12, 0))
        st.write('Hora ingresada:', value)

    '**Podeos combinar st.date_input() y st.time_input() para mostrar un input de fecha y tiempo.**'
    '**Y unir los valores ingresados en un objeto de tipo datetime.datetime utilizando el metodo datetime.combine().**'
    with st.echo():
        date = st.date_input('fecha ', value=datetime.date(2021, 1, 1))
        time = st.time_input('hora', value=datetime.time(12, 0))
        value = datetime.datetime.combine(date, time)
        st.write('Fecha y hora ingresada:', value)

    st.divider()

    st.subheader('st.color_picker()')
    '**st.color_picker() es una función que permite mostrar un input de color en la interfaz web.**'
    '**El método st.color_picker() recibe un argumento label que es el texto que se mostrará al lado del input de color y un argumento value que es el valor por defecto del input de color.**'
    '**El método st.color_picker() retorna el valor ingresado por el usuario o el valor por defecto.**'
    with st.echo():
        value = st.color_picker('Elige un color', value='#ff0000')
        st.write('Color ingresado:', value)
    st.divider()
    st.subheader('st.camera_input()')
    '**st.camera_input() es una función que permite mostrar un input de cámara en la interfaz web.**'
    '**El método st.camera_input() recibe un argumento label que es el texto que se mostrará al lado del input de cámara.**'
    with st.echo():
        value = st.camera_input('Haz clic para tomar una foto')
        if value is not None:
            st.image(value, caption='Foto tomada', use_column_width=True)

    st.markdown('''
    <a href="#d4d99250" style="text-align: center; display: block;">Volver al principio</a>
    ''', unsafe_allow_html=True)

with c2:
    with st.container(border=True):
        st.markdown('#### Índice')
        st.markdown('[st.text_input()](#st-text-input)')
        st.markdown('[st.number_input()](#st-number-input)')
        st.markdown('[st.text_area()](#st-text-area)')
        st.markdown('[st.date_input()](#st-date-input)')
        st.markdown('[st.time_input()](#st-time-input)')
        st.markdown('[st.color_picker()](#st-color-picker)')
        st.markdown('[st.camera_input()](#st-camera-input)')
