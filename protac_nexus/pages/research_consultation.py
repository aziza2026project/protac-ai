import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    page='Research Consultation'; st.title(page); st.write(SERVICES.get(page, page))
    with st.form("consultation"):
        st.text_input("Email")
        st.text_area("Describe what you want done")
        st.file_uploader("Supporting files",accept_multiple_files=True)
        submitted=st.form_submit_button("Submit request")
    if submitted: st.warning("Prototype only: request not stored or emailed. Secure backend, admin review, quote, and deposit workflow are not connected.")
