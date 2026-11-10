import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    page='Ternary Complex Assessment'; st.title(page); st.write(SERVICES.get(page, page))
    st.text_input("Protein of Interest (POI)")
    st.text_input("Warhead / POI ligand")
    st.text_input("E3 ligase")
    st.file_uploader("Optional supported structure files",accept_multiple_files=True)
    st.warning("Requires a configured structural workflow. An estimate is not proof of degradation.")
