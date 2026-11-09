import streamlit as st
from protac_nexus.config.services import SERVICES
from protac_nexus.demo_access import is_demo_user


def render():
    page = "Research Collaboration"
    st.title(page)
    st.write(SERVICES[page])
    demo = is_demo_user(st.session_state)

    if demo:
        st.info(
            "Demo preview: collaboration submissions are disabled. "
            "No proposal is stored or emailed."
        )

    with st.form("collaboration_proposal_form"):
        st.text_input("Organization / laboratory", disabled=demo)
        st.text_input("Contact email", disabled=demo)
        st.text_area("Project and collaboration goals", disabled=demo)
        st.file_uploader(
            "Supporting files",
            accept_multiple_files=True,
            disabled=demo,
            help="Do not upload confidential or sensitive files to the public demo.",
        )
        st.form_submit_button(
            "Submit proposal",
            disabled=demo,
            type="primary",
        )

    if not demo:
        st.warning(
            "Prototype only: proposal storage, access control, and notifications "
            "must be configured before accepting submissions."
        )
