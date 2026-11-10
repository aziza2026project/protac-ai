import streamlit as st
from protac_nexus.config.services import SERVICES


def render():
    st.error(
        "Admin Portal is not enabled. Secure authentication and server-side "
        "administrator role checks must be implemented first."
    )
    st.title("Admin Portal")
    st.write(SERVICES["Admin Portal"])
