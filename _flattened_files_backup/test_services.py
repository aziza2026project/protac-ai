from protac_nexus.config.services import SERVICES


def test_service_catalogue_is_plain_data_and_has_expected_core_services():
    assert isinstance(SERVICES, dict)
    assert "Natural Products Explorer" in SERVICES
    assert "Molecular Docking" in SERVICES
    assert "Admin Portal" in SERVICES


def test_every_service_has_a_description():
    assert all(isinstance(name, str) and name for name in SERVICES)
    assert all(isinstance(description, str) and description for description in SERVICES.values())
