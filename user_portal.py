import streamlit as st
from protac_nexus.config.services import SERVICES
from protac_nexus.demo_access import is_demo_user


def render():
    page = "User Portal"
    st.title(page)
    st.write(SERVICES[page])

    if is_demo_user(st.session_state):
        st.info(
            "Demo User view: account records, request history, payments, and "
            "deliverables are sample/placeholder areas. No personal account data is connected."
        )

    st.write(
        "Track consultation and collaboration requests, status, payments, "
        "subscriptions, and deliverables."
    )
    st.caption("Authentication and secure database services are not configured.")
