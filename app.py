"""Application shell only. Individual screens are in protac_nexus/pages/."""
import streamlit as st
from protac_nexus.ui.styles import apply_styles
from protac_nexus.config.services import SERVICES
from protac_nexus.pages import (home, explore_services, natural_products_explorer, protac_explorer, molecular_docking, structure_visualization, experimental_data, comparison_ranking, ternary_assessment, linker_optimization, ai_prediction, export_reports, research_consultation, research_collaboration, user_portal, subscription_payments, admin_portal, platform_roadmap)

st.set_page_config(page_title="PROTAC Nexus", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")
apply_styles()
PAGES={"Home":home.render,"Explore Services":explore_services.render,"Natural Products Explorer":natural_products_explorer.render,"PROTAC Explorer":protac_explorer.render,"Molecular Docking":molecular_docking.render,"3D Structure Visualization":structure_visualization.render,"Experimental Data Explorer":experimental_data.render,"Comparison & Ranking":comparison_ranking.render,"Ternary Complex Assessment":ternary_assessment.render,"Linker Optimization":linker_optimization.render,"AI Prediction":ai_prediction.render,"Export & Reports":export_reports.render,"Research Consultation":research_consultation.render,"Research Collaboration":research_collaboration.render,"User Portal":user_portal.render,"Subscription & Payments":subscription_payments.render,"Admin Portal":admin_portal.render,"Platform Roadmap":platform_roadmap.render}
with st.sidebar:
    st.markdown("## 🌿 PROTAC Nexus")
    st.caption("Natural Products–Based PROTACs for Cancer Therapy")
    st.caption("RESEARCH WORKSPACE")
    page=st.radio("Navigation",list(PAGES),label_visibility="collapsed")
    st.divider()
    st.caption("Early prototype — secure workflows and some scientific engines are not connected yet.")
PAGES[page]()
st.divider()
st.caption("PROTAC Nexus • Early UI prototype. Computational hypotheses must remain distinct from published and validated experimental results.")
