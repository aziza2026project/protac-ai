import streamlit as st
from protac_nexus.config.services import SERVICES


def render():
    page = "Research Consultation"
    st.title(page)
    st.write(SERVICES[page])

    with st.form("consultation_request_form"):
        email = st.text_input("Email", placeholder="name@institution.org")
        description = st.text_area("Describe what you want done")
        files = st.file_uploader("Supporting files", accept_multiple_files=True)
        submitted = st.form_submit_button("Submit request", type="primary")

    if submitted:
        st.warning(
            "The request has not been sent or saved: secure request storage and "
            "email notifications are not connected yet."
        )
        if email or description or files:
            st.caption("Your entries are available only in this current form session.")
