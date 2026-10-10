from protac_nexus.integrations.providers import PROVIDER_DEFAULTS, search_pubchem, search_chembl


def test_provider_defaults_keep_unselected_engines_swappable():
    assert PROVIDER_DEFAULTS["compound_identity"] == "pubchem"
    assert PROVIDER_DEFAULTS["bioactivity"] == "chembl"
    assert PROVIDER_DEFAULTS["docking_engine"] == "not_configured"
    assert PROVIDER_DEFAULTS["prediction_model"] == "not_configured"


def test_empty_queries_do_not_call_external_services():
    assert search_pubchem("   ") == []
    assert search_chembl("") == []
