
"""PROTAC Nexus - Main Application"""

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
# SESSION STATE
# ==========================================

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:

    st.markdown("## 🌿 PROTAC Nexus")

    st.caption(
        "Natural Products–Based PROTACs for Cancer Therapy"
    )

    st.caption("RESEARCH WORKSPACE")

    st.divider()

    selected_page = st.radio(
        "Navigation",
        options=list(PAGES.keys()),
        index=list(PAGES.keys()).index(
            st.session_state.current_page
        ),
        label_visibility="collapsed",
    )

    st.session_state.current_page = selected_page

    st.divider()

    st.caption(
        "Early prototype — secure workflows and some "
        "scientific engines are not connected yet."
    )


# ==========================================
# MAIN CONTENT
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

    # Map service names to registered application pages
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

    services_list = list(SERVICES.items())

    # Display services in three columns
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

                    if target_page:

                        if st.button(
                            "Open Service →",
                            key=f"service_button_{service_name}",
                            use_container_width=True,
                            type="primary",
                        ):

                            st.session_state.current_page = target_page

                            st.rerun()

                    else:

                        st.button(
                            "Coming Soon",
                            key=f"coming_{service_name}",
                            disabled=True,
                            use_container_width=True,
                        )


else:

    PAGES[st.session_state.current_page]()


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "PROTAC Nexus • Early UI prototype. "
    "Computational hypotheses must remain distinct "
    "from published and validated experimental results."
)
