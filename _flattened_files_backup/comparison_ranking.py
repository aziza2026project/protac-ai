import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    page='Comparison & Ranking'; st.title(page); st.write(SERVICES.get(page, page))
    st.multiselect("Comparison evidence",["Chemical descriptors","Experimental measurements","Docking outputs","Ternary-complex assessment"])
    st.info("Only comparable measurements will be ranked together.")
