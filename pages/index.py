import streamlit as st

st.markdown('''
<style>
#MainMenu, header {visibility: hidden;}
</style>
''', unsafe_allow_html=True)
st.title('Indice')
st.divider()
st.subheader('Despliegue de datos')
c1,c2,c3,c4 = st.columns(4)

c1.page_link('pages/write.py', label='st.write()',icon='✍️',use_container_width=True)
c2.page_link('pages/magic.py', label='Magic',icon='🔮',use_container_width=True)
c3.page_link('pages/markdown.py', label='Markdown',icon='📑',use_container_width=True)
c4.page_link('pages/display_text.py', label='Más Opciones para mostrar texto',icon='📚',use_container_width=True)


c5,c6,c7,c8 = st.columns(4)

c5.page_link('pages/titulos.py', label='Titulos',icon='🔖',use_container_width=True)
c6.page_link('pages/data_frames.py', label='Despliegue de Tablas',icon='📋',use_container_width=True)
c7.page_link('pages/media.py', label='Archivos multimedia',icon='🎬',use_container_width=True)

st.subheader('Entrada de datos')
d1,d2,d3,d4 = st.columns(4)
d1.page_link('pages/inputs.py', label='Inputs',icon='📲',use_container_width=True)
d2.page_link('pages/sliders.py', label='Sliders',icon='🎚️',use_container_width=True)
d3.page_link('pages/options.py', label='Opciones',icon='✅',use_container_width=True)
d4.page_link('pages/files.py', label='Archivos',icon='🗃️',use_container_width=True)

d5,d6,d7,d8 = st.columns(4)
d5.page_link('pages/buttons.py', label='Botones',icon='🔘',use_container_width=True)

