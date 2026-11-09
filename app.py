"""PROTAC Nexus main application — public Demo User environment."""

import streamlit as st

from protac_nexus.config.services import SERVICES
from protac_nexus.demo_access import (
    DEMO_EMAIL,
    DEMO_ROLE,
    DEMO_USERNAME,
)
from protac_nexus.ui.styles import apply_styles
from protac_nexus.pages import (
    home,
    explore_services,
    natural_products_explorer,
    protac_explorer,
    molecular_docking,
    structure_visualization,
    experimental_data,
    comparison_ranking,
    ternary_assessment,
    linker_optimization,
    ai_prediction,
    export_reports,
    research_consultation,
    research_collaboration,
    user_portal,
    subscription_payments,
    admin_portal,
    platform_roadmap,
)


# Streamlit page configuration must be the first Streamlit command.
st.set_page_config(
    page_title="PROTAC Nexus",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_styles()

# IMPORTANT:
# This is an intentionally public, read-only demo identity, not authentication.
# Do not connect it to production data, privileged actions, or payment workflows.
DEMO_MODE = True
if DEMO_MODE:
    st.session_state["demo_mode"] = True
    st.session_state["user_role"] = DEMO_ROLE
    st.session_state["user_email"] = DEMO_EMAIL
    st.session_state["username"] = DEMO_USERNAME


PAGES = {
    "Home": home.render,
    "Explore Services": explore_services.render,
    "Natural Products Explorer": natural_products_explorer.render,
    "PROTAC Explorer": protac_explorer.render,
    "Molecular Docking": molecular_docking.render,
    "3D Structure Visualization": structure_visualization.render,
    "Experimental Data Explorer": experimental_data.render,
    "Comparison & Ranking": comparison_ranking.render,
    "Ternary Complex Assessment": ternary_assessment.render,
    "Linker Optimization": linker_optimization.render,
    "AI Prediction": ai_prediction.render,
    "Export & Reports": export_reports.render,
    "Research Consultation": research_consultation.render,
    "Research Collaboration": research_collaboration.render,
    "User Portal": user_portal.render,
    "Subscription & Payments": subscription_payments.render,
    "Admin Portal": admin_portal.render,
    "Platform Roadmap": platform_roadmap.render,
}

# Public Demo Users cannot navigate to the Admin Portal.
DEMO_PAGES = [name for name in PAGES if name != "Admin Portal"]

SERVICE_PAGE_MAP = {
    name: name
    for name in (
        "Natural Products Explorer",
        "PROTAC Explorer",
        "Molecular Docking",
        "3D Structure Visualization",
        "Experimental Data Explorer",
        "Comparison & Ranking",
        "Ternary Complex Assessment",
        "Linker Optimization",
        "AI Prediction",
        "Export & Reports",
        "Research Consultation",
        "Research Collaboration",
    )
}

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Enforce the demo page allow-list on every rerun.
if st.session_state["current_page"] not in DEMO_PAGES:
    st.session_state["current_page"] = "Home"


with st.sidebar:
    st.markdown("## 🌿 PROTAC Nexus")
    st.caption("Natural Products–Based PROTACs for Cancer Therapy")
    st.divider()

    st.success("🧪 Demo User Session")
    st.caption(f"Account: {DEMO_EMAIL}")
    st.caption("Role: Demo User")
    st.caption("Public, read-only demonstration")

    st.divider()
    st.caption("RESEARCH WORKSPACE")

    selected_page = st.radio(
        "Navigation",
        options=DEMO_PAGES,
        index=DEMO_PAGES.index(st.session_state["current_page"]),
        label_visibility="collapsed",
    )

    if selected_page != st.session_state["current_page"]:
        st.session_state["current_page"] = selected_page
        st.rerun()

    st.divider()
    st.info(
        "You are exploring PROTAC Nexus as a Demo User. "
        "Admin access, submissions, and payments are disabled."
    )
    st.caption(
        "Some scientific engines and external integrations are not connected yet."
    )


st.markdown(
    """
    <div style="
        padding: 10px 16px;
        border-radius: 8px;
        background-color: rgba(30, 136, 100, 0.10);
        border: 1px solid rgba(30, 136, 100, 0.35);
        margin-bottom: 15px;
    ">
        🧪 <b>DEMO ENVIRONMENT</b>
        <span style="margin-left: 8px;">
            You are exploring PROTAC Nexus as a Demo User.
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)


current_page = st.session_state["current_page"]

if current_page == "Home":
    st.title("🌿 PROTAC Nexus")
    st.subheader("Natural Products–Based PROTACs for Cancer Therapy")
    st.write(
        "An integrated research workspace for natural products, PROTAC discovery, "
        "molecular modeling, experimental data and scientific analysis."
    )
    st.divider()
    st.header("Explore Our Services")
    st.write("Select a service to access its dedicated research workspace.")

    service_items = list(SERVICES.items())
    for start in range(0, len(service_items), 3):
        columns = st.columns(3)
        for column, (service_name, description) in zip(
            columns, service_items[start : start + 3]
        ):
            with column:
                with st.container(border=True):
                    st.markdown(f"### {service_name}")
                    st.write(description)
                    target_page = SERVICE_PAGE_MAP.get(service_name)
                    if target_page in DEMO_PAGES:
                        if st.button(
                            "Explore Service →",
                            key=f"service_{service_name}",
                            width="stretch",
                            type="primary",
                        ):
                            st.session_state["current_page"] = target_page
                            st.rerun()
                    else:
                        st.button(
                            "Preview in sidebar",
                            key=f"coming_{service_name}",
                            disabled=True,
                            width="stretch",
                        )
else:
    if st.button(
        "⌂ Home",
        key="small_home_button",
        help="Return to Home Page",
        type="secondary",
    ):
        st.session_state["current_page"] = "Home"
        st.rerun()

    # Defense in depth: this branch should be unreachable for Demo Users.
    if current_page == "Admin Portal":
        st.error("Access denied: Admin Portal is restricted.")
    else:
        PAGES[current_page]()


st.divider()
st.caption(
    "PROTAC Nexus • Public Demo Environment. Computational hypotheses must remain "
    "distinct from published and validated experimental results."
)
