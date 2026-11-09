import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    page='Experimental Data Explorer'; st.title(page); st.write(SERVICES.get(page, page))
    st.multiselect("Measurement",["IC50","Ki","Kd","DC50","Dmax"])
    st.text_input("Target or compound ID")
    st.caption("Preserve units, assay, cell line, treatment duration, references, and missing values.")
