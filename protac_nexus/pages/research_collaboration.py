import streamlit as st
from protac_nexus.config.services import SERVICES


def render():
    page = "Research Collaboration"
    st.title(page)
    st.write(SERVICES[page])

    with st.form("collaboration_proposal_form"):
        organization = st.text_input("Organization / laboratory")
        email = st.text_input("Contact email", placeholder="name@institution.org")
        goals = st.text_area("Project and collaboration goals")
        files = st.file_uploader("Supporting files", accept_multiple_files=True)
        submitted = st.form_submit_button("Submit proposal", type="primary")

    if submitted:
        st.warning(
            "The proposal has not been sent or saved: proposal storage and "
            "notifications are not connected yet."
        )
        if organization or email or goals or files:
            st.caption("Your entries are available only in this current form session.")
