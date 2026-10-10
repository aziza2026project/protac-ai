import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    page='PROTAC Explorer'; st.title(page); st.write(SERVICES.get(page, page))
    st.text_input("Search by compound, target, warhead, E3 ligase, linker, or reference")
    st.info("Scientific database import is not connected yet.")
