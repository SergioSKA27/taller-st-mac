import streamlit as st


st.markdown('''
<style>
#MainMenu, header {visibility: hidden;}
</style>
''', unsafe_allow_html=True)
t,indx = st.columns([0.8,0.2])
t.title('🔖Titulos')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)
st.divider()
'**Para mostrar un título en la interfaz web, podemos usar la función st.title().**'


with st.echo():
    st.title('Este es un título')

'**Streamlit unicamente permite mostrar un título por página y cada pagina debe tener un título.**'
'**Si deseamos mostrar más de un título en la misma página, podemos usar la función st.header().**'

with st.echo():
    st.header('Este es un título')
    st.header('Este es otro título')

'**Opcionalmente, podemos mostrar un subtítulo con la función st.subheader().**'

with st.echo():
    st.subheader('Este es un subtítulo')

'**También podemos mostrar titulos utilizando markdown y las funciones st.markdown() o st.write().**'
with st.echo():
    st.markdown('# Este es un título')
    st.write('## Este es un subtítulo')

    st.markdown('''
    # Este es un título equivalente a h1
    ## Este es un subtítulo equivalente a h2
    ### Este es un subtítulo equivalente a h3
    #### Este es un subtítulo equivalente a h4
    ##### Este es un subtítulo equivalente a h5
    ###### Este es un subtítulo equivalente a h6
    ''')


st.markdown('''
    <a href="#829ced17" style="text-align: center; display: block;">Volver al principio</a>
    ''', unsafe_allow_html=True)
