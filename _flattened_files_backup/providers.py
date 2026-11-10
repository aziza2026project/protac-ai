"""Thin, replaceable clients for public chemistry and bioactivity data APIs.

These clients retrieve source records; they do not infer biological efficacy.
"""
from __future__ import annotations

from typing import Any
import requests

TIMEOUT_SECONDS = 15
USER_AGENT = "PROTAC-Nexus/0.1 (research prototype)"

class ProviderError(RuntimeError):
    """Raised when an external provider cannot return usable data."""


def _get_json(url: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    try:
        response = requests.get(
            url, params=params, timeout=TIMEOUT_SECONDS,
            headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
        )
        if response.status_code == 404:
            return {}
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as exc:
        raise ProviderError(f"External data provider request failed: {exc}") from exc


def search_pubchem(query: str, limit: int = 10) -> list[dict[str, Any]]:
    """Search PubChem by name and return identifiers/structure fields where available."""
    query = query.strip()
    if not query:
        return []
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{requests.utils.quote(query, safe='')}/property/Title,IUPACName,CanonicalSMILES,IsomericSMILES,InChIKey/JSON"
    payload = _get_json(url)
    properties = payload.get("PropertyTable", {}).get("Properties", [])
    results = []
    for item in properties[:max(1, min(limit, 50))]:
        results.append({
            "source": "PubChem",
            "source_id": item.get("CID"),
            "name": item.get("Title") or query,
            "iupac_name": item.get("IUPACName"),
            "canonical_smiles": item.get("ConnectivitySMILES") or item.get("CanonicalSMILES"),
            "isomeric_smiles": item.get("SMILES") or item.get("IsomericSMILES"),
            "inchikey": item.get("InChIKey"),
            "source_url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{item.get('CID')}" if item.get("CID") else "https://pubchem.ncbi.nlm.nih.gov/",
        })
    return results


def search_chembl(query: str, limit: int = 10) -> list[dict[str, Any]]:
    """Search ChEMBL molecules by preferred name or synonym; activity data is separate."""
    query = query.strip()
    if not query:
        return []
    payload = _get_json(
        "https://www.ebi.ac.uk/chembl/api/data/molecule/search.json",
        params={"q": query, "limit": max(1, min(limit, 50))},
    )
    results = []
    for item in payload.get("molecules", []):
        chembl_id = item.get("molecule_chembl_id")
        results.append({
            "source": "ChEMBL",
            "source_id": chembl_id,
            "name": item.get("pref_name") or chembl_id,
            "molecule_type": item.get("molecule_type"),
            "max_phase": item.get("max_phase"),
            "source_url": f"https://www.ebi.ac.uk/chembl/compound_report_card/{chembl_id}/" if chembl_id else "https://www.ebi.ac.uk/chembl/",
        })
    return results


# Engine adapters are intentionally configured by name. A later provider can
# replace an implementation without changing UI/database contracts.
PROVIDER_DEFAULTS = {
    "compound_identity": "pubchem",
    "bioactivity": "chembl",
    "chemistry_toolkit": "rdkit_optional",
    "docking_engine": "not_configured",
    "prediction_model": "not_configured",
    "linker_generator": "not_configured",
    "database": "local_prototype",
    "authentication": "not_configured",
    "payments": "not_configured",
    "email": "not_configured",
}
