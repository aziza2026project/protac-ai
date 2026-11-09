import streamlit as st

SERVICES = {
    "Natural Products Explorer": "Explore natural compounds and derivatives, their sources, structures, targets, and literature.",
    "PROTAC Explorer": "Search PROTACs, targets, warheads, E3 ligands, linkers, and references.",
    "Molecular Docking": "Submit supported structures to a configured docking engine.",
    "3D Structure Visualization": "Explore supported protein and ligand structures.",
    "Experimental Data Explorer": "Review published IC50, Ki, Kd, DC50, and Dmax values with assay context.",
    "Comparison & Ranking": "Compare compounds using clear, scientifically appropriate criteria.",
    "Ternary Complex Assessment": "Assess possible POI–PROTAC–E3 arrangements, with uncertainty and limitations.",
    "Linker Optimization": "Compare existing linkers; generate alternatives only when a validated chemistry workflow is connected.",
    "AI Prediction": "Use an existing suitable model only after its task and input requirements are validated.",
    "Export & Reports": "Export supported results with references and provenance.",
    "Research Consultation": "Submit a research question, description, and supporting files for review.",
    "Research Collaboration": "Propose a collaboration with a lab, researcher, or organization.",
}

st.subheader("PROTAC Nexus Services")

# Initialize selected service
if "selected_service" not in st.session_state:
    st.session_state.selected_service = None

# Display services as buttons
for service, description in SERVICES.items():
    if st.button(service, key=f"service_{service}", use_container_width=True):
        st.session_state.selected_service = service

# Display selected service
if st.session_state.selected_service:
    selected = st.session_state.selected_service

    st.markdown(f"### {selected}")
    st.write(SERVICES[selected])

    # Navigate to the selected service
    if selected == "Natural Products Explorer":
        st.switch_page("pages/natural_products.py")

    elif selected == "PROTAC Explorer":
        st.switch_page("pages/protac_explorer.py")

    elif selected == "Molecular Docking":
        st.switch_page("pages/molecular_docking.py")

    elif selected == "3D Structure Visualization":
        st.switch_page("pages/structure_visualization.py")

    elif selected == "Experimental Data Explorer":
        st.switch_page("pages/experimental_data.py")

    elif selected == "Comparison & Ranking":
        st.switch_page("pages/comparison.py")

    elif selected == "Ternary Complex Assessment":
        st.switch_page("pages/ternary_complex.py")

    elif selected == "Linker Optimization":
        st.switch_page("pages/linker_optimization.py")

    elif selected == "AI Prediction":
        st.switch_page("pages/ai_prediction.py")

    elif selected == "Export & Reports":
        st.switch_page("pages/export_reports.py")

    elif selected == "Research Consultation":
        st.switch_page("pages/research_consultation.py")

    elif selected == "Research Collaboration":
        st.switch_page("pages/research_collaboration.py")