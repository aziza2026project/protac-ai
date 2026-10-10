import streamlit as st
from protac_nexus.config.services import SERVICES
def render():
    st.title("Explore Services"); st.write("Explore the planned scientific workflows and research support offered by PROTAC Nexus.")
    st.markdown('<span class="pill">Scientific discovery</span><span class="pill">Computational assessment</span><span class="pill">Research support</span><span class="pill">Reports & exports</span>',unsafe_allow_html=True)
    for name,description in SERVICES.items():
        with st.expander(name):
            st.write(description); left,right=st.columns(2)
            with left: st.markdown("**Planned inputs**"); st.write("Compound name or ID, supported molecular representations, target information, structures, or research files, depending on the workflow.")
            with right: st.markdown("**Planned outputs**"); st.write("Traceable records, comparisons, visualizations, or a research report when the required tools are configured.")
            st.caption("Intended functionality only; unavailable integrations are not represented as live.")
