# PROTAC Nexus — UI-first starter

A Streamlit prototype for **Natural Products–Based PROTACs for Cancer Therapy**. This build focuses on preparing the whole application interface and workflows before integrating the remaining scientific datasets and engines.

## Current scope

- Home page and service directory
- Pages for natural products, PROTACs, docking, 3D visualization, experimental data, comparison, ternary-complex assessment, linker optimization, AI prediction, and exports
- Research consultation and collaboration forms (prototype only; submissions are not persisted)
- User, admin, subscription/payment, and platform roadmap pages
- Existing optional PubChem/ChEMBL lookup adapter and RDKit adapter remain in the starter, but the main goal of this phase is the overall app structure
- Scientific caveats to distinguish computational hypotheses from experimental evidence

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Important limitations

This is an early UI prototype, not a production service. User authentication, role-based access, database persistence, secure file storage, request notifications, payment processing, and most scientific computation workflows are **not implemented or connected**. Do not upload confidential files or enter payment details. UI forms do not submit to a real backend. Before launch, implement and test secure server-side access checks, data retention, validation, audit logging, and backups.

## Design approach

Scientific tools and data providers should be integrated behind separate adapters so that a provider or model can be replaced later without redesigning the user interface. Keep source provenance and uncertainty visible. Natural origin alone does not establish anticancer efficacy; docking scores are not experimental binding data; IC50, Ki, Kd, DC50, and Dmax are distinct measurements.


## Modular file layout

Each major screen has its own file in `protac_nexus/pages/`, so changes stay local to that option. Shared service labels live in `protac_nexus/config/services.py`; shared styling lives in `protac_nexus/ui/styles.py`; external integrations live in `protac_nexus/integrations/`. See `docs/PROJECT_STRUCTURE.md`.
