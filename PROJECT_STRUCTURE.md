# Project structure and modular development

The app is intentionally split into small files so an option can be changed without rewriting the entire app.

- `app.py`: application setup, sidebar navigation, and page router only.
- `protac_nexus/pages/`: one file per screen/service. Edit the matching file to change that page.
- `protac_nexus/config/services.py`: shared service names and descriptions.
- `protac_nexus/ui/styles.py`: shared visual theme and CSS.
- `protac_nexus/integrations/`: replaceable adapters for external data sources and chemistry tools.
- `data/raw/`: reserved for original data files; preserve originals.
- `data/processed/`: generated/cleaned data only.
- `tests/`: automated checks.

## Add a new page
1. Create a module in `protac_nexus/pages/`, e.g. `my_feature.py`.
2. Add a `render()` function containing only that page's UI.
3. Import the module in `app.py` and add it to `PAGES`.

This is a modular prototype, not yet a production system. Authentication, secure storage, request persistence, email, payments, and several scientific engines still need implementation and testing.
