import pytest
from src.be.configuration.config_parser import get_config_value
from src.be.utilities.error_schema import error_schema
from src.be.utilities.candidates_utilities.json_schemas.post_candidate_schema import post_candidate_schema
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_payloads import \
    create_candidate_required_fields_payload, create_candidate_full_payload, missing_first_name_payload
from src.be.definitions.candidates_definitions import get_candidate_id, update_candidates, create_candidate_request
from src.be.utilities.get_core_api_data import get_candidates_by_id_from_core_api
from src.be.utilities.useful_functions import get_random_first_name, get_random_last_name, get_random_remit, \
    get_random_uuid, get_future_date, get_past_date, get_date_time_format, get_past_date_time, get_future_date_time, \
    standard_headers, validate_response_schema_and_fields

base_url = get_config_value("base_url")
endpoint = "candidates/"
headers = standard_headers()
first_name = get_random_first_name()
last_name = get_random_last_name()
remit = get_random_remit()


def test_update_candidate_excluded_missing_payload_fields():
    candidate_id = get_candidate_id()
    updated_payload = create_candidate_required_fields_payload()
    update_response = update_candidates(base_url, endpoint, candidate_id, updated_payload, headers)
    assert update_response.status_code == 200
    assert update_response.json()['id'] == candidate_id
    assert "desired_positions" not in update_response.json()


def test_update_candidate_unauthorized_request():
    candidate_id = get_candidate_id()
    payload = create_candidate_required_fields_payload()
    update_response = update_candidates(base_url, endpoint, candidate_id, payload, "")
    assert update_response.status_code in (401, 403), f"Expected 401 or 403, but got {update_response.status_code}"


def test_update_candidate_validate_json_schema():
    candidate_id = get_candidate_id()
    updated_payload = create_candidate_full_payload()
    update_response = update_candidates(base_url, endpoint, candidate_id, updated_payload, headers)
    assert update_response.status_code == 200
    validate_response_schema_and_fields(update_response.json(), post_candidate_schema)


def test_update_candidate_missing_required_field():
    candidate_id = get_candidate_id()
    updated_payload = missing_first_name_payload()
    update_response = update_candidates(base_url, endpoint, candidate_id, updated_payload, headers)
    assert update_response.status_code == 400
    validate_response_schema_and_fields(update_response.json(), error_schema)


def test_update_candidate_nonexistent_candidate():
    candidate_id = get_random_uuid()
    updated_payload = create_candidate_required_fields_payload()
    update_response = update_candidates(base_url, endpoint, candidate_id, updated_payload, headers)
    assert update_response.status_code == 404
    validate_response_schema_and_fields(update_response.json(), error_schema)


def test_update_candidate_with_extra_payload_field():
    candidate_id = get_candidate_id()
    updated_payload = create_candidate_required_fields_payload()
    updated_payload['extra_field'] = "extra value"
    update_response = update_candidates(base_url, endpoint, candidate_id, updated_payload, headers)
    assert update_response.status_code == 200
    assert "extra_field" not in update_response.json()


def test_update_candidate_with_empty_payload():
    candidate_id = get_candidate_id()
    update_response = update_candidates(base_url, endpoint, candidate_id, "{}", headers)
    assert update_response.status_code == 400
    validate_response_schema_and_fields(update_response.json(), error_schema)


def test_update_candidate_with_invalid_data_types():
    candidate_id = get_candidate_id()
    updated_payload = create_candidate_required_fields_payload()
    updated_payload['situation_status'] = 123456
    update_response = update_candidates(base_url, endpoint, candidate_id, updated_payload, headers)
    assert update_response.status_code == 400
    validate_response_schema_and_fields(update_response.json(), error_schema)


def test_update_candidate_integration_with_core_api():
    payload = create_candidate_full_payload()
    post_response = create_candidate_request(base_url, endpoint, payload, headers)
    assert post_response.status_code == 200
    candidate_id = post_response.json()['id']
    updated_payload = create_candidate_full_payload()
    update_response = update_candidates(base_url, endpoint, candidate_id, updated_payload, headers)
    assert update_response.status_code == 200
    core_api_response = get_candidates_by_id_from_core_api(candidate_id)
    assert update_response.json()['id'] == post_response.json()['id']
    assert update_response.json()['first_name'] != post_response.json()['first_name']
    assert update_response.json()['first_name'] == core_api_response.json()['core_candidate']['first_name']
    assert update_response.json()['family_name'] == core_api_response.json()['core_candidate']['family_name']
    assert update_response.json()['location_remit'] == core_api_response.json()['location_remit']


def test_update_candidate_last_updated_at_greater_than_created_at():
    candidate_id = get_candidate_id()
    updated_payload = create_candidate_required_fields_payload()
    update_response = update_candidates(base_url, endpoint, candidate_id, updated_payload, headers)
    assert update_response.status_code == 200
    core_api_data = get_candidates_by_id_from_core_api(candidate_id)
    assert core_api_data.json()["created_at"] < core_api_data.json()['last_updated_at']


def test_update_candidate_created_at_should_not_be_present():
    candidate_id = get_candidate_id()
    updated_payload = create_candidate_required_fields_payload()
    updated_payload['created_at'] = get_date_time_format()
    update_response = update_candidates(base_url, endpoint, candidate_id, updated_payload, headers)
    assert update_response.status_code == 200
    assert update_response.json()['created_at'] != get_date_time_format()


@pytest.mark.parametrize("date_props", ['expiry_date', 'visa_expiry', 'date_of_birth', 'availability_date'])
def test_update_candidate_expiry_date_min_max_values(date_props):
    payload = create_candidate_full_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    payload[date_props] = get_past_date(101)
    update_response = update_candidates(base_url, endpoint, response.json()['id'], payload, headers)
    assert update_response.status_code == 400
    payload[date_props] = get_future_date(101)
    update_response = update_candidates(base_url, endpoint, response.json()['id'], payload, headers)
    assert update_response.status_code == 400


@pytest.mark.parametrize("date_props",
                         ['salary_last_updated_at', 'original_source_recorded_at', 'background_information_updated_at'])
def test_update_candidate_min_max_date_time_values(date_props):
    payload = create_candidate_full_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    payload[date_props] = get_past_date_time(101)
    update_response = update_candidates(base_url, endpoint, response.json()['id'], payload, headers)
    assert update_response.status_code == 400
    payload[date_props] = get_future_date_time(101)
    update_response = update_candidates(base_url, endpoint, response.json()['id'], payload, headers)
    assert update_response.status_code == 400


@pytest.mark.parametrize("required_property", create_candidate_required_fields_payload())
def test_update_candidate_required_property_set_to_null(required_property):
    payload = create_candidate_required_fields_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    update_payload = create_candidate_required_fields_payload()
    update_payload[required_property] = None
    activity_response = update_candidates(base_url, endpoint, response.json()['id'], update_payload, headers)
    assert activity_response.status_code == 400
