import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    page='3D Structure Visualization'; st.title(page); st.write(SERVICES.get(page, page))
    st.file_uploader("Upload structure files",accept_multiple_files=True)
    st.info("A molecular viewer will be integrated after choosing supported formats and a viewer.")
