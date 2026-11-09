"""Static service catalogue.

Keep this module free of Streamlit UI calls: it is imported by many pages
and must not create widgets or navigate the app during import.
"""

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
    "User Portal": "Review a user's requests, account information, and deliverables when secure account services are connected.",
    "Subscription & Payments": "Review subscription information and payment options when a verified payment provider is connected.",
    "Admin Portal": "Manage platform users, requests, access policies, and audit records with administrator permissions.",
    "Platform Roadmap": "Review planned platform milestones and integration status.",
}
