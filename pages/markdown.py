import streamlit as st

st.markdown('''
<style>
#MainMenu, header {visibility: hidden;}
</style>
''', unsafe_allow_html=True)
t,indx = st.columns([0.8,0.2])
t.title('📑st.markdown()')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)
st.divider()
'''
**st.markdown() es una función que permite mostrar texto en la interfaz web.
Usando markdown, podemos dar formato al texto, como negritas, cursivas, títulos, listas, entre otros.
además de poder agregar emojis y colores al texto.**


'''
with st.echo():
    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)


st.subheader('Mostrando HTML')
'''
**Opcionalmente, podemos pasarle texto en formato html a la función st.markdown().
Por ejemplo, podemos agregar un enlace a una página web, o una imagen.**
'''

with st.echo():
    st.markdown('''
        <a href="https://www.streamlit.io/">Streamlit</a>
    ''')

'**Al ejecutar el código anterior, se mostrará el texto sin formato, para poder ver el enlace, se debe agregar el parámetro unsafe_allow_html=True a la función st.markdown().**'

with st.echo():
    st.markdown('''
        <a href="https://www.streamlit.io/">Streamlit</a>
    ''', unsafe_allow_html=True)

st.markdown('''
        <a href="#ebfeb93a" style="text-align: center; display: block;">Volver al principio</a>
        ''', unsafe_allow_html=True)

