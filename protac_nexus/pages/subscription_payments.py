import streamlit as st
from protac_nexus.config.services import SERVICES


def render():
    page = "Subscription & Payments"
    st.title(page)
    st.write(SERVICES[page])
    st.subheader("Platform access")
    st.write(
        "Subscription plans and paid research services will be displayed here "
        "after account and billing systems are connected."
    )
    st.warning(
        "No payment provider is connected. Do not enter card details or send "
        "payment information through this application yet."
    )
