import streamlit as st
from protac_nexus.config.services import SERVICES
from protac_nexus.demo_access import is_demo_user


def render():
    if is_demo_user(st.session_state):
        st.error("Access denied: Admin Portal is not available to Demo Users.")
        st.stop()

    page = "Admin Portal"
    st.title(page)
    st.write(SERVICES[page])
    st.write(
        "Manage consultation and collaboration requests, quotes, deposits, "
        "progress, users, and deliverables."
    )
    st.info(
        "Admin authentication, role permissions, database, notifications, "
        "and audit logs must be configured before production use."
    )
