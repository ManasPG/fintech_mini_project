import streamlit as st

def render_navbar(active_page="Dashboard"):
    st.markdown(
        f"""
        <div class="navbar">
            <div class="nav-pill">
                <span class="nav-item {'active' if active_page=='Dashboard' else ''}">Dashboard</span>
                <span class="nav-item {'active' if active_page=='Reports' else ''}">Reports</span>
                <span class="nav-item {'active' if active_page=='Analytics' else ''}">Analytics</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
