import streamlit as st
from protac_nexus.config.services import SERVICES
from protac_nexus.demo_access import is_demo_user


def render():
    page = "Subscription & Payments"
    st.title(page)
    st.write(SERVICES[page])

    if is_demo_user(st.session_state):
        st.info(
            "Demo User access: this page is view-only. Subscription changes and "
            "payments are disabled in the public demo."
        )

    st.subheader("Platform access")
    st.write(
        "Subscription plans and paid research services will be displayed here "
        "after the account and billing systems are connected."
    )
    st.warning(
        "No payment provider is connected. Do not enter card details or send "
        "payment information through this prototype."
    )
