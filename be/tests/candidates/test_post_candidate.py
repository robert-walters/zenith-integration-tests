import pytest

from src.be.configuration.config_parser import get_config_value
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_payloads import \
    create_candidate_full_payload, create_candidate_required_fields_payload, missing_first_name_payload, \
    missing_last_name_payload, missing_remit_payload, wrong_remit_format_payload, wrong_situation_status_payload, \
    wrong_responsible_user_payload, missing_responsible_team_payload
from src.be.utilities.error_schema import error_schema
from src.be.utilities.candidates_utilities.json_schemas.post_candidate_schema import post_candidate_schema
from src.be.definitions.candidates_definitions import create_candidate_request, \
    verify_national_candidate_data_in_core_api, verify_core_candidate_data_in_core_api, validate_the_post_response
from src.be.utilities.get_core_api_data import get_candidates_by_id_from_core_api
from src.be.utilities.useful_functions import get_past_date, get_future_date, get_future_date_time, \
    get_past_date_time, standard_headers, validate_response_schema_and_fields

base_url = get_config_value("base_url")
endpoint = "candidates/"
headers = standard_headers()


def test_create_candidate_full_payload():
    payload = create_candidate_full_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    validate_response_schema_and_fields(response.json(), post_candidate_schema)


def test_create_candidate_integration():
    payload = create_candidate_full_payload()
    post_response = create_candidate_request(base_url, endpoint, payload, headers)
    post_json = post_response.json()
    assert post_response.status_code == 200
    candidate_id = post_json['id']
    get_core_json = get_candidates_by_id_from_core_api(candidate_id)
    print(get_core_json.json())
    verify_national_candidate_data_in_core_api(post_json, get_core_json.json())
    verify_core_candidate_data_in_core_api(post_json, get_core_json.json())


def test_create_candidate_mandatory_payload():
    payload = create_candidate_required_fields_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200


def test_create_candidate_without_first_name():
    payload = missing_first_name_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_candidate_without_last_name():
    payload = missing_last_name_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_candidate_missing_remit():
    payload = missing_remit_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_candidate_wrong_remit_format():
    payload = wrong_remit_format_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_candidate_wrong_situation_status():
    payload = wrong_situation_status_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    json_response = response.json()
    assert response.status_code == 400
    error_message = json_response["error"]["errors"][0]["message"]
    assert error_message == "situation_status must be one of the following values: active, passive"
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_candidate_wrong_responsible_user():
    payload = wrong_responsible_user_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_candidate_missing_responsible_user():
    payload = missing_responsible_team_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_candidate_missing_responsible_team():
    payload = missing_responsible_team_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_candidate_comparing_payload_with_the_response():
    payload = create_candidate_full_payload()
    post_response = create_candidate_request(base_url, endpoint, payload, headers)
    post_json = post_response.json()
    validate_the_post_response(payload, post_json)


def test_create_candidate_last_update_at_equals_created_at():
    payload = create_candidate_full_payload()
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    candidate_id = response.json()['id']
    get_core_json = get_candidates_by_id_from_core_api(candidate_id)
    assert get_core_json.json()['last_updated_at'] == get_core_json.json()['created_at']


@pytest.mark.parametrize("date_props", ['expiry_date', 'visa_expiry', 'date_of_birth', 'availability_date'])
def test_create_candidate_min_max_dates_values(date_props):
    payload = create_candidate_full_payload()
    payload[date_props] = get_past_date(101)
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
    payload[date_props] = get_future_date(101)
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


@pytest.mark.parametrize("date_props",
                         ['salary_last_updated_at', 'original_source_recorded_at', 'background_information_updated_at'])
def test_create_candidate_min_max_date_time_values(date_props):
    payload = create_candidate_full_payload()
    payload[date_props] = get_past_date_time(101)
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
    payload[date_props] = get_future_date_time(101)
    response = create_candidate_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


@pytest.mark.parametrize("required_property", create_candidate_required_fields_payload())
def test_create_job_activity_required_property_set_to_null(required_property):
    payload = create_candidate_required_fields_payload()
    payload[required_property] = None
    activity_response = create_candidate_request(base_url, endpoint, payload, headers)
    assert activity_response.status_code == 400


def test_create_candidate_unauthorized():
    payload = create_candidate_required_fields_payload()
    response = create_candidate_request(base_url, endpoint, payload, "")
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"

