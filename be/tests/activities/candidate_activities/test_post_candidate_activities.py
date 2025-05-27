import pytest

from src.be.definitions.candidates_definitions import get_candidate_id
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_activity_payload import *
from src.be.utilities.error_schema import error_schema
from src.be.utilities.candidates_utilities.json_schemas.post_candidate_activity_schema import \
    post_candidate_activity_schema

base_url = get_config_value("base_url")
endpoint = "candidates/"
headers = standard_headers()
candidate_id = get_candidate_id()


def test_create_candidate_activity_mandatory_payload():
    payload = create_candidate_activity_required_payload()
    activity_response = create_activity_request(base_url, endpoint, candidate_id, payload, headers)
    assert activity_response.status_code == 200
    validate_response_schema_and_fields(activity_response.json(), post_candidate_activity_schema)
    validate_response_with_expected_json(create_candidate_activity_required_props(), activity_response.json(),
                                         get_request_body_json(activity_response))


def test_create_candidate_activity_full_payload():
    payload = create_candidate_activity_full_payload()
    activity_response = create_activity_request(base_url, endpoint, candidate_id, payload, headers)
    assert activity_response.status_code == 200
    validate_response_schema_and_fields(activity_response.json(), post_candidate_activity_schema)
    validate_response_with_expected_json(create_client_activity_additional_props(), activity_response.json(),
                                         get_request_body_json(activity_response))


def test_create_candidate_activities_integration():
    create_response = create_activity_request(base_url, endpoint, candidate_id,
                                              create_candidate_activity_full_payload(), headers)
    assert create_response.status_code == 200
    get_core_response = get_activity_for_candidate(candidate_id)
    assert get_core_response.status_code == 200, f"Response: {get_core_response.json()}"
    assert any(obj['id'] == create_response.json()['id'] for obj in get_core_response.json()['results'])


@pytest.mark.parametrize("missing_property", create_candidate_activity_required_payload().keys())
def test_create_candidate_activity_missing_required_properties(missing_property):
    payload = missing_required_field_payload(create_candidate_activity_required_payload(), missing_property)
    activity_response = create_activity_request(base_url, endpoint, candidate_id, payload, headers)
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_candidate_activity_unauthorized():
    payload = create_candidate_activity_required_payload()
    activity_response = create_activity_request(base_url, endpoint, candidate_id, payload, None)
    assert activity_response.status_code in (401, 403), f"Expected 401 or 403, but got {activity_response.status_code}"


def test_create_candidate_activity_misspelled_endpoint():
    payload = create_candidate_activity_required_payload()
    activity_response = create_activity_request(base_url, "candidate/", candidate_id, payload, headers)
    assert activity_response.status_code == 404


def test_create_candidate_activity_empty_payload():
    activity_response = create_activity_request(base_url, endpoint, candidate_id, None, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_candidate_activity_wrong_type():
    payload = create_candidate_activity_full_payload()
    payload['type'] = random_string(10)
    activity_response = create_activity_request(base_url, endpoint, candidate_id, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_candidate_activity_wrong_source():
    payload = create_candidate_activity_full_payload()
    payload['source'] = random_string(10)
    activity_response = create_activity_request(base_url, endpoint, candidate_id, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_candidate_activity_wrong_event_type():
    payload = create_candidate_activity_full_payload()
    payload['event_type'] = random_string(10)
    activity_response = create_activity_request(base_url, endpoint, candidate_id, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_candidate_activity_wrong_outcome():
    payload = create_candidate_activity_full_payload()
    payload['outcome'] = random_string(10)
    activity_response = create_activity_request(base_url, endpoint, candidate_id, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_candidate_activity_original_full_payload():
    payload = create_candidate_activity_original_full_payload(candidate_id)
    activity_response = create_original_activity_request(base_url, payload, headers)
    assert activity_response.status_code == 200
    validate_response_schema_and_fields(activity_response.json(), post_candidate_activity_schema)


def test_create_candidate_activity_original_mandatory_payload():
    payload = create_candidate_activity_original_mandatory_payload(candidate_id)
    activity_response = create_original_activity_request(base_url, payload, headers)
    assert activity_response.status_code == 200
    validate_response_schema_and_fields(activity_response.json(), post_candidate_activity_schema)


def test_create_candidate_activity_original_wrong_record_origin():
    payload = create_candidate_activity_original_full_payload(candidate_id)
    payload['record_origin'] = "clients"
    activity_response = create_original_activity_request(base_url, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_candidate_activity_original_missing_entity_id():
    payload = create_candidate_activity_original_full_payload(candidate_id)
    del payload["candidate_id"]
    activity_response = create_original_activity_request(base_url, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


@pytest.mark.parametrize("required_property", create_candidate_activity_required_payload())
def test_create_candidate_activity_required_property_set_to_null(required_property):
    payload = missing_required_field_payload(create_candidate_activity_required_payload(), required_property)
    payload[required_property] = None
    activity_response = create_activity_request(base_url, endpoint, candidate_id, payload, headers)
    assert activity_response.status_code == 400
