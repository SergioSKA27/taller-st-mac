import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.markdown('''
<style>
#MainMenu, header {visibility: hidden;}
</style>
''', unsafe_allow_html=True)
t,indx = st.columns([0.8,0.2])
t.title('✍️st.write()')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)

st.divider()
'**Con el método st.write() podemos mostrar texto, dataframes, gráficos, entre otros.**'

with st.echo():

    st.write(1234)

    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
    }))

'**El método st.write() es muy versátil podemos pasarle multiples argumentos y el método se encargará de mostrarlos en la interfaz web.**'
with st.echo():
    data_frame = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
    })
    st.write('1 + 1 = ', 2)

    st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')
'**También podemos mostrar gráficos con el método st.write().**'

with st.echo():
    df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

    st.write(c)

st.markdown('''
    <a href="#91be9ad1" style="text-align: center; display: block;">Volver al principio</a>
    ''', unsafe_allow_html=True)
