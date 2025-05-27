import pytest
from src.be.configuration.config_parser import get_config_value
from src.be.definitions.activity_definitions import get_activity_id, update_activity_request, \
    get_activity_request, \
    update_organisation_activity_required_props, update_organisation_activity_additional_props, \
    create_original_activity_request, update_original_activity_request, \
    update_candidate_activity_original_required_props, create_activity_request
from src.be.definitions.jobs_definitions import get_job_id
from src.be.utilities.organisations_utilities.request_payloads.create_organisation_activity_payloads import \
    create_organisation_activity_full_payload, create_organisation_activity_original_full_payload, \
    create_organisation_activity_required_payload
from src.be.utilities.organisations_utilities.request_payloads.create_organisation_payloads import \
    create_organisation_required_payload
from src.be.utilities.organisations_utilities.request_payloads.update_organisation_activity_payloads import \
    update_organisation_activity_required_payload, update_organisation_activity_full_payload, \
    update_organisation_activity_original_mandatory_payload
from src.be.utilities.useful_functions import validate_response_with_expected_json, get_request_body_json, \
    standard_headers, missing_required_field_payload

base_url = get_config_value("base_url")
endpoint = "organisations/"
headers = standard_headers()

org_id = get_job_id(base_url, endpoint, create_organisation_required_payload(), headers)
activity_id = get_activity_id(base_url, endpoint, org_id, create_organisation_activity_full_payload(), headers)


def test_update_organisation_activity_excluded_missing_payload_fields():
    updated_payload = update_organisation_activity_required_payload()
    updated_response = update_activity_request(base_url, endpoint, org_id, activity_id, updated_payload,
                                               headers)
    assert updated_response.status_code == 200
    validate_response_with_expected_json(update_organisation_activity_required_props(), updated_response.json(),
                                         get_request_body_json(updated_response))
    for prop in update_organisation_activity_additional_props():
        assert prop in updated_response.json()


def test_update_organisation_activity_integration():
    updated_payload = update_organisation_activity_full_payload()
    updated_response = update_activity_request(base_url, endpoint, org_id, activity_id, updated_payload,
                                               headers)
    assert updated_response.status_code == 200
    get_response = get_activity_request(base_url, endpoint, org_id, activity_id, headers)
    assert get_response.status_code == 200
    validate_response_with_expected_json(update_organisation_activity_additional_props(), updated_response.json(),
                                         get_response.json())


def test_update_organisation_activity_unauthorized():
    updated_payload = update_organisation_activity_required_payload()
    updated_response = update_activity_request(base_url, endpoint, org_id, activity_id, updated_payload,
                                               None)
    assert updated_response.status_code in (401, 403), f"Expected 401 or 403, but got {updated_response.status_code}"


def test_update_organisation_activity_missing_payload():
    updated_candidate_response = update_activity_request(base_url, endpoint, org_id, activity_id, None,
                                                         headers)
    assert updated_candidate_response.status_code == 400


def test_update_organisation_activity_wrong_data_type():
    updated_payload = update_organisation_activity_full_payload()
    updated_payload["event_location"] = 123456
    updated_candidate_response = update_activity_request(base_url, endpoint, org_id, activity_id, updated_payload,
                                                         headers)
    assert updated_candidate_response.status_code == 400


def test_update_candidate_activity_original_full_payload():
    create_response = create_original_activity_request(base_url,
                                                       create_organisation_activity_original_full_payload(org_id),
                                                       headers)
    assert create_response.status_code == 200
    payload = update_organisation_activity_original_mandatory_payload(org_id)
    update_response = update_original_activity_request(base_url, create_response.json()['id'], payload, headers)
    assert update_response.status_code == 200
    validate_response_with_expected_json(update_candidate_activity_original_required_props(),
                                         get_request_body_json(update_response), update_response.json())


@pytest.mark.parametrize("required_property", create_organisation_activity_required_payload().keys())
def test_update_organisations_activity_required_property_set_to_null(required_property):
    create_payload = create_organisation_activity_required_payload()
    response = create_activity_request(base_url, endpoint, org_id, create_payload, headers)
    assert response.status_code == 200
    update_payload = missing_required_field_payload(create_payload, required_property)
    update_payload[required_property] = None
    update_response = update_activity_request(base_url, endpoint, org_id, response.json()['id'],
                                              update_payload, headers)
    assert update_response.status_code == 400
