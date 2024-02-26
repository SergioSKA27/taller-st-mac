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
t.title('🔘Botones')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)
st.divider()
c1,c2 = st.columns([0.8,0.2])




with c1:
    st.subheader('st.button()')
    '**st.button() es una función que permite mostrar un botón en la interfaz web.**'
    '**El método st.button() recibe un argumento label que es el texto que se mostrará en el botón y un argumento key que es un identificador único para el botón.**'
    '**El método st.button() retorna True si el botón es presionado, de lo contrario retorna False.**'
    with st.echo():
        if st.button('Presioname'):
            st.write('Botón presionado')
        else:
            st.write('Botón no presionado')

    '**Notar que el valor de st.button() se queda en True hasta que otro evento ocurra y forze a la página a refrescarse.**'

    if st.button('Refrescar'):
        st.rerun()
    st.divider()

    st.subheader('st.link_button()')
    '**st.link_button() es una función que permite mostrar un botón que redirige a una página web.**'
    '**El método st.link_button() recibe un argumento label que es el texto que se mostrará en el botón y un argumento url que es la dirección web a la que se redirigirá el botón.**'
    with st.echo():
        st.link_button('Ir a Google', 'https://www.google.com')

    st.markdown('''
    <a href="#b4f0f6d9" style="text-align: center; display: block;">Volver al principio</a>
    ''', unsafe_allow_html=True)

with c2:
    with st.container(border=True):
        st.markdown('#### Índice')
        st.markdown('[st.button()](#st-button)')
        st.markdown('[st.link_button()](#st-link-button)')
