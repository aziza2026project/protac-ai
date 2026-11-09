import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    page='Export & Reports'; st.title(page); st.write(SERVICES.get(page, page))
    st.selectbox("Export format",["CSV","Excel","PDF report","SDF (when supported)"])
    st.info("Export becomes available when real results are connected.")
