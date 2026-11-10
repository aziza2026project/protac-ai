import streamlit as st
from protac_nexus.config.services import SERVICES
from protac_nexus.demo_access import is_demo_user


def render():
    page = "Research Consultation"
    st.title(page)
    st.write(SERVICES[page])
    demo = is_demo_user(st.session_state)

    if demo:
        st.info(
            "Demo preview: you can inspect this form, but submissions are disabled. "
            "No information is stored or emailed."
        )

    with st.form("consultation_request_form"):
        st.text_input("Email", disabled=demo, placeholder="name@institution.org")
        st.text_area("Describe what you want done", disabled=demo)
        st.file_uploader(
            "Supporting files",
            accept_multiple_files=True,
            disabled=demo,
            help="Do not upload confidential or sensitive files to the public demo.",
        )
        st.form_submit_button(
            "Submit request",
            disabled=demo,
            type="primary",
        )

    if not demo:
        st.warning(
            "Prototype only: secure request storage, admin review, quotation, "
            "and notification workflows must be configured before accepting submissions."
        )
