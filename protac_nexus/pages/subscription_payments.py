import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    page='Subscription & Payments'; st.title(page); st.write(SERVICES.get(page, page))
    st.write("Subscription plans and one-off service payments.")
    st.warning("No payment provider is connected. Do not enter payment details here.")
