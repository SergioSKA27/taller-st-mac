import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t,inx = st.columns([0.8,0.2])
t.title('🔮Magia')
inx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)
st.divider()
'**Los comandos mágicos son una característica de Streamlit que le permite escribir casi cualquier cosa (rebajas, datos, gráficos) sin tener que escribir ningún comando explícito. Simplemente coloque lo que desea mostrar en su propia línea de código y aparecerá en su aplicación. He aquí un ejemplo:**'

with st.echo():
    # Draw a title and some text to the app:
    '''
    # This is the document title

    This is some _markdown_.
    '''

    df = pd.DataFrame({'col1': [1,2,3]})
    df  # 👈 Draw the dataframe

    x = 10
    'x', x  # 👈 Draw the string 'x' and then the value of x

    # Also works with most supported chart types

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    fig  # 👈 Draw a Matplotlib chart

st.markdown('''
        <a href="#c766f772" style="text-align: center; display: block;">Volver al principio</a>
        ''', unsafe_allow_html=True)
