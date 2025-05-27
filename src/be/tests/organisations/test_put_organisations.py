import pytest

from src.be.configuration.config_parser import get_config_value
from src.be.definitions.organisations_definitions import create_organisations_request, update_organisations_request, \
    update_organisation_additional_props, get_organisations_request, update_organisation_required_props
from src.be.utilities.organisations_utilities.request_payloads.create_organisation_payloads import \
    create_organisation_full_payload, create_organisation_employer_only_full_payload, \
    create_organisation_required_payload
from src.be.utilities.organisations_utilities.request_payloads.update_organisation_payloads import \
    update_organisation_required_payload, update_organisation_full_payload, \
    update_organisation_employer_only_required_payload
from src.be.utilities.useful_functions import validate_response_with_expected_json, standard_headers

base_url = get_config_value("base_url")
endpoint = "organisations/"
headers = standard_headers()


def test_update_organisations_employer_only_excluded_missing_payload_fields():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_employer_only_full_payload(),
                                                   headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    update_response = update_organisations_request(base_url, endpoint, org_id,
                                                   update_organisation_employer_only_required_payload(), headers)
    assert update_response.status_code == 200


def test_update_organisations_excluded_missing_payload_fields():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    update_response = update_organisations_request(base_url, endpoint, org_id,
                                                   update_organisation_required_payload(), headers)
    assert update_response.status_code == 200
    for prop in update_organisation_additional_props():
        assert prop in update_response.json()


def test_update_organisation_compare_with_get():
    create_response = create_organisations_request(base_url, endpoint,
                                                   create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    updated_payload = update_organisation_full_payload()
    updated_response = update_organisations_request(base_url, endpoint, org_id, updated_payload, headers)
    assert updated_response.status_code == 200
    get_response = get_organisations_request(base_url, endpoint, org_id, headers)
    assert get_response.status_code == 200
    validate_response_with_expected_json(update_organisation_required_props(), updated_response.json(),
                                         get_response.json())
    validate_response_with_expected_json(update_organisation_additional_props(), updated_response.json(),
                                         get_response.json())


def test_update_organisation_unauthorized():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    updated_payload = update_organisation_full_payload()
    updated_response = update_organisations_request(base_url, endpoint, org_id, updated_payload, None)
    assert updated_response.status_code in (401, 403), f"Expected 401 or 403, but got {updated_response.status_code}"


def test_update_organisation_missing_payload():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    updated_response = update_organisations_request(base_url, endpoint, org_id, None, headers)
    assert updated_response.status_code == 400


def test_update_organisation_wrong_data_type():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    updated_payload = update_organisation_full_payload()
    updated_payload['credit_expiry'] = 123456
    updated_response = update_organisations_request(base_url, endpoint, org_id, updated_payload, headers)
    assert updated_response.status_code == 400


@pytest.mark.parametrize("required_property", create_organisation_required_payload())
def test_update_organisation_required_property_set_to_null(required_property):
    payload = create_organisation_required_payload()
    response = create_organisations_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    update_payload = create_organisation_required_payload()
    update_payload[required_property] = None
    activity_response = update_organisations_request(base_url, endpoint, response.json()['id'], update_payload, headers)
    assert activity_response.status_code == 400
