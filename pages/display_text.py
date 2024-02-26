import streamlit as st


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
t.title('📚Más opciones para mostrar texto')
indx.page_link('pages/index.py', label='Volver al índice principal',icon='📝',use_container_width=True)
st.divider()

c1,c2 = st.columns([0.8,0.2])


with c1:
    '**Además de las funciones st.title(), st.subheader(), st.markdown() y st.write(), Streamlit nos ofrece otras opciones para mostrar texto en la interfaz web.**'


    st.subheader('st.text()')
    '**st.text() es una función que permite mostrar texto en la interfaz web. A diferencia de st.write(), st.text() no admite formato de texto, solo muestra el texto sin formato.**'

    with st.echo():
        st.text('Este es un texto sin formato')

    st.subheader('st.code()')
    '**st.code() es una función que permite mostrar texto en la interfaz web con formato de código.**'

    with st.echo():
        st.code('#Codigo ejemplo\nimport streamlit as st')



    st.subheader('st.latex()')
    '**st.latex() es una función que permite mostrar texto en la interfaz web con formato latex.**'
    with st.echo():
        st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

    st.subheader('st.caption()')
    '**st.caption() es una función que permite mostrar texto en la interfaz web como una anotación o leyenda.**'

    with st.echo():
        st.caption('Esta es una leyenda')


    st.subheader('st.divider()')
    '**st.divider() es una función que permite mostrar una línea divisoria en la interfaz web.**'

    with st.echo():
        st.write('Texto arriba')
        st.divider()
    st.markdown('''
        <a href="#e379963d" style="text-align: center; display: block;">Volver al principio</a>
        ''', unsafe_allow_html=True)

with c2:
    with st.container(border=True):
        st.markdown('#### Índice')
        st.markdown('[st.text()](#st-text)')
        st.markdown('[st.code()](#st-code)')
        st.markdown('[st.latex()](#st-latex)')
        st.markdown('[st.caption()](#st-caption)')
        st.markdown('[st.divider()](#st-divider)')


