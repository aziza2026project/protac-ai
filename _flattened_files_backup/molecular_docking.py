import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    page='Molecular Docking'; st.title(page); st.write(SERVICES.get(page, page))
    st.file_uploader("Upload supported structure files",accept_multiple_files=True)
    st.warning("Docking engine not connected. No docking results are fabricated.")
