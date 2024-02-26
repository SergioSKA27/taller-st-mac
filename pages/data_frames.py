import streamlit as st
import pandas as pd
import numpy as np
import random

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

titl, indx = st.columns([0.8,0.2])
titl.title('📋Despliegue de Tablas')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)
st.divider()
c1,c2 = st.columns([0.8,0.2])




with c1:
    st.subheader('st.dataframe()')
    '**Para mostrar dataframes en la interfaz web, podemos usar la función st.dataframe().**'
    with st.echo():
        df = pd.DataFrame({
            'first column': [1, 2, 3, 4],
            'second column': [10, 20, 30, 40],
        })
        st.dataframe(df)

    '**También podemos mostrar tablas con formato de texto con la función st.write().**'
    with st.echo():
        st.write(df)

    '**Ambas opciones son muy similares, sin embargo, st.dataframe() ofrece algunas opciones adicionales para personalizar la apariencia de la tabla.**'
    '**Por ejemplo, podemos ajustar la altura de la tabla con el argumento height y el ancho con el argumento width.**'
    with st.echo():
        st.dataframe(df, height=100, width=300)


    st.subheader('st.data_editor()')
    '**No obstante, st.dataframe() no admite modificar los valores de la tabla, si necesitamos esta funcionalidad, podemos usar la función st.data_editor().**'

    with st.echo():
        st.write('Dataframe original:', df)
        st.write('editar el dataframe')
        df = pd.DataFrame({
            'first column': [1, 2, 3, 4],
            'second column': [10, 20, 30, 40],
        })
        data = st.data_editor(df)

        st.write('Dataframe modificado:', data)

    st.subheader('st.table()')
    '**Si deseamos mostrar una tabla estática, podemos usar la función st.table().**'
    with st.echo():
        st.table(df)


    st.subheader('Opciones de formato')
    '**Podemos personalizar la apariencia de la tabla con el método .style() de pandas.**'

    with st.echo():
        df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

        st.dataframe(df.style.highlight_max(axis=0))

    '**O podemos usar column_config, hide_index y column_order para personalizar la apariencia de la tabla.**'
    '**Aunque estas son opciones de formato mas avanzadas.**'

    with st.echo():
        df = pd.DataFrame(
            {
                "name": ["Roadmap", "Extras", "Issues"],
                "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                "stars": [random.randint(0, 1000) for _ in range(3)],
                "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
            }
        )
        st.dataframe(
            df,
            column_config={
                "name": "App name",
                "stars": st.column_config.NumberColumn(
                    "Github Stars",
                    help="Number of stars on GitHub",
                    format="%d ⭐",
                ),
                "url": st.column_config.LinkColumn("App URL"),
                "views_history": st.column_config.LineChartColumn(
                    "Views (past 30 days)", y_min=0, y_max=5000
                ),
            },
            hide_index=True,
        )
    st.markdown('''
    <a href="#b4c567f0" style="text-align: center; display: block;">Volver al principio</a>
    ''', unsafe_allow_html=True)


with c2:
    with st.container(border=True):
        st.markdown('#### Índice')
        st.markdown('[st.dataframe()](#st-dataframe)')
        st.markdown('[st.data_editor()](#st-data-editor)')
        st.markdown('[st.table()](#st-table)')
        st.markdown('[Opciones de formato](#opciones-de-formato)')
