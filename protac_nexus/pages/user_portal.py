import streamlit as st
from protac_nexus.config.services import SERVICES


def render():
    page = "User Portal"
    st.title(page)
    st.write(SERVICES[page])
    st.write(
        "This area is intended for account details, request history, "
        "subscription status, payments, and deliverables."
    )
    st.info(
        "User sign-in and account storage are not connected yet. "
        "Entering an email in a request form does not create or authenticate an account."
    )
