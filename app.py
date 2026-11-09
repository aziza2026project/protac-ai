
"""PROTAC Nexus - Main Application | Demo User Mode"""

import streamlit as st

from protac_nexus.ui.styles import apply_styles
from protac_nexus.config.services import SERVICES

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


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="PROTAC Nexus",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_styles()


# ==========================================
# DEMO USER CONFIGURATION
# ==========================================

DEMO_MODE = True

if DEMO_MODE:
    st.session_state.demo_mode = True
    st.session_state.user_role = "demo"
    st.session_state.user_email = "demo@protacnexus.local"
    st.session_state.username = "Demo User"
    st.session_state.is_authenticated = True


# ==========================================
# PAGE REGISTRY
# ==========================================

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


# ==========================================
# DEMO PAGE ACCESS
# ==========================================

# Admin Portal is excluded from the Demo User navigation.
DEMO_PAGES = [
    page_name
    for page_name in PAGES
    if page_name != "Admin Portal"
]


# ==========================================
# SERVICE PAGE MAPPING
# ==========================================

SERVICE_PAGE_MAP = {
    "Natural Products Explorer": "Natural Products Explorer",
    "PROTAC Explorer": "PROTAC Explorer",
    "Molecular Docking": "Molecular Docking",
    "3D Structure Visualization": "3D Structure Visualization",
    "Experimental Data Explorer": "Experimental Data Explorer",
    "Comparison & Ranking": "Comparison & Ranking",
    "Ternary Complex Assessment": "Ternary Complex Assessment",
    "Linker Optimization": "Linker Optimization",
    "AI Prediction": "AI Prediction",
    "Export & Reports": "Export & Reports",
    "Research Consultation": "Research Consultation",
    "Research Collaboration": "Research Collaboration",
}


# ==========================================
# SESSION STATE
# ==========================================

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Prevent access to pages outside the Demo User navigation.
if st.session_state.current_page not in DEMO_PAGES:
    st.session_state.current_page = "Home"


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:

    st.markdown("## 🌿 PROTAC Nexus")

    st.caption(
        "Natural Products–Based PROTACs for Cancer Therapy"
    )

    st.divider()

    # Demo User identity
    st.success("🧪 Demo User Session")

    st.caption("Account: demo@protacnexus.local")
    st.caption("Role: Demo User")

    st.divider()

    st.caption("RESEARCH WORKSPACE")

    selected_page = st.radio(
        "Navigation",
        options=DEMO_PAGES,
        index=DEMO_PAGES.index(
            st.session_state.current_page
        ),
        label_visibility="collapsed",
    )

    if selected_page != st.session_state.current_page:
        st.session_state.current_page = selected_page
        st.rerun()

    st.divider()

    st.info(
        "You are using the public Demo environment. "
        "The Admin Portal is restricted."
    )

    st.caption(
        "Some scientific engines and external integrations "
        "may not yet be connected."
    )


# ==========================================
# DEMO MODE BANNER
# ==========================================

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


# ==========================================
# HOME PAGE
# ==========================================

if st.session_state.current_page == "Home":

    st.title("🌿 PROTAC Nexus")

    st.subheader(
        "Natural Products–Based PROTACs for Cancer Therapy"
    )

    st.write(
        "An integrated research workspace for natural products, "
        "PROTAC discovery, molecular modeling, experimental data "
        "and scientific analysis."
    )

    st.divider()

    st.header("Explore Our Services")

    st.write(
        "Select a service to access its dedicated research workspace."
    )

    services_list = list(SERVICES.items())

    # Three-column service layout

    for start in range(0, len(services_list), 3):

        columns = st.columns(3)

        for column, (service_name, description) in zip(
            columns,
            services_list[start:start + 3]
        ):

            with column:

                with st.container(border=True):

                    st.markdown(f"### {service_name}")

                    st.write(description)

                    target_page = SERVICE_PAGE_MAP.get(
                        service_name
                    )

                    if target_page and target_page in DEMO_PAGES:

                        if st.button(
                            "Explore Service →",
                            key=f"service_{service_name}",
                            width="stretch",
                            type="primary",
                        ):

                            st.session_state.current_page = target_page
                            st.rerun()

                    else:

                        st.button(
                            "Coming Soon",
                            key=f"coming_{service_name}",
                            disabled=True,
                            width="stretch",
                        )


# ==========================================
# OTHER SERVICE PAGES
# ==========================================

else:

    current_page = st.session_state.current_page

    # Small Home button

    col_home, col_space = st.columns([1, 9])

    with col_home:

        if st.button(
            "⌂ Home",
            key="small_home_button",
            help="Return to Home Page",
            type="secondary",
        ):

            st.session_state.current_page = "Home"
            st.rerun()

    # Admin Portal protection

    if current_page == "Admin Portal":

        st.error(
            "Access denied. The Admin Portal is not available "
            "in the Demo User environment."
        )

    else:

        PAGES[current_page]()


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "PROTAC Nexus • Demo Environment. "
    "Computational hypotheses must remain distinct "
    "from published and validated experimental results."
)
