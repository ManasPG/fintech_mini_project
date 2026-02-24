import streamlit as st

def analysis_card(title, description):
    with st.container(border=True):
        st.markdown(f"### {title}")
        st.markdown(description)
        return st.checkbox("Select", key=title)
    
def render_logo():
    st.image("logo.png", width=150)
