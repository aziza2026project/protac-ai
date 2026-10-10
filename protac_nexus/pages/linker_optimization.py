import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    page='Linker Optimization'; st.title(page); st.write(SERVICES.get(page, page))
    st.radio("Starting point",["Existing PROTAC","Structure or SMILES"],horizontal=True)
    st.text_input("Compound ID or SMILES")
    st.selectbox("Optimization criterion",["Length","Flexibility","Rotatable bonds","Chemical class"])
    st.selectbox("Mode",["Compare existing linkers","Generate alternatives (engine required)"])
    st.info("Phase 1: compare existing linker records. Generation requires a validated chemistry workflow.")
