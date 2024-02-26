import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import asyncio
import random


st.set_page_config(layout="wide")

st.markdown('''
<style>
    #MainMenu, header {visibility: hidden;}
    .centeredtitle {
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 99999;
        position: absolute;
        vertical-align: center;
        margin: 0;
        transform: translateY(200%);
        width: 100%;}
    .centeredtitle h1 {
        font-size: 5em;
        color: rgba(255, 255, 255, 0.8);
        text-shadow: 2px 2px 2px #000;
        margin: 0;
        padding: 0;
        font-family: 'Arial';
        font-weight: 700;
        text-align: center;
    }
    button[kind="primary"] {
        background-color: #f63366;
    }
</style>
<div class="centeredtitle">
<h1>Tutorial Streamlit</h1>
</div>
''', unsafe_allow_html=True)

if st.button('Presioname',type='primary',use_container_width=True):
    st.switch_page('pages/index.py')
nodes = []
edges = []
nodes.append( Node(id="random 1",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?mathematics")
            ) # includes **kwargs
nodes.append( Node(id="random 2",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?python")
            )
nodes.append( Node(id="random 3",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?machine-learning")
            )
nodes.append( Node(id="random 4",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?programming")
            )
nodes.append( Node(id="random 5",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?machine-learning,programming,")
            )
nodes.append( Node(id="random 6",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?python,mathematics")
            )
nodes.append( Node(id="random 7",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?programming,python")
            )
nodes.append( Node(id="random 8",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?web-development")
            )
nodes.append( Node(id="random 9",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?ai,programming")
            )
nodes.append( Node(id="random 10",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?javascript")
            )
nodes.append( Node(id="random 11",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?html,css")
            )
nodes.append( Node(id="random 12",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?linear-algebra")
            )
nodes.append( Node(id="random 13",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?graph-theory")
            )
nodes.append( Node(id="random 14",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?numpy")
            )

nodes.append( Node(id="random 15",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?react")
            )
nodes.append( Node(id="random 16",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?native")
            )
nodes.append( Node(id="random 17",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?code")
            )
nodes.append( Node(id="random 18",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?coding")
            )
nodes.append( Node(id="random 19",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?programming,python,mathematics,web-development,linear-algebra,graph-theory,numpy,react,native,code,coding")
            )
nodes.append( Node(id="random 20",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?programming,python,mathematics,web-development")
            )
nodes.append( Node(id="random 21",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?programming,python,mathematics,web-development,native,code,coding")
            )
nodes.append( Node(id="random 22",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?programming,python,mathematics,html,css,linear-algebra,graph-theory,numpy,react,native,code,coding")
            )
nodes.append( Node(id="random 23",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?web-development,ai,programming,javascript,html,css,linear-algebra,graph-theory,numpy,react,native,code,coding")
            )
nodes.append( Node(id="random 24",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?web-development,ai")
            )
nodes.append( Node(id="random 25",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?html,css,linear-algebra,graph-theory,numpy,react,native,code,coding")
            )
nodes.append( Node(id="random 26",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?html,css,linear-algebra,react,native,code,coding")
            )
nodes.append( Node(id="random 27",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?programming,javascript,html,css,linear-algebra,graph-theory,react,native,code,coding")
            )
nodes.append( Node(id="random 28",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?css,linear-algebra,graph-theory,numpy,react,native,code,coding")
            )
nodes.append( Node(id="random 29",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?css,linear-algebra,graph-theory,numpy,react,native,code,coding")
            )
nodes.append( Node(id="random 30",
                   size=25,
                   shape="circularImage",
                   image="https://source.unsplash.com/random/720x480?programming,python,mathematics,web-development,ai,javascript,html")
            )

for i in range(1,len(nodes)):
    for j in range(1,len(nodes)):
        rand = random.randint(0,1)

        if i != j:
            if rand == 1:
                edges.append(Edge(source=f"random {i}", target=f"random {j}",length=600))

edges.append(Edge(source="random 1", target="random 30",length=600))
config = Config(width=1200,
                height=900,
                directed=False,
                physics=True,
                hierarchical=False,
                # **kwargs
                )

return_value = agraph(nodes=nodes,
                      edges=edges,
                      config=config)


