import pytest
from jsonschema import validate

from src.be.configuration.config_parser import get_config_value
from src.be.definitions.jobs_definitions import create_job_request, create_job_required_properties, \
    create_job_additional_properties, get_jobs_request
from src.be.utilities.job_utilities.json_schemas.post_jobs_schema import post_jobs_schema
from src.be.utilities.job_utilities.request_payloads.create_job_payload import create_job_required_fields_payload, \
    create_job_full_payload, wrong_job_type_payload, wrong_agreement_type_payload
from src.be.utilities.useful_functions import get_random_remit, get_request_body_json, \
    validate_response_with_expected_json, random_string, missing_required_field_payload, get_past_date, \
    get_future_date, standard_headers, validate_response_schema_and_fields

base_url = get_config_value("base_url")
endpoint = "jobs/"
headers = standard_headers()
remit = get_random_remit()


def test_create_job_mandatory_payload():
    payload = create_job_required_fields_payload()
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    validate_response_schema_and_fields(response.json(), post_jobs_schema)


def test_create_job_full_payload():
    payload = create_job_full_payload()
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    validate_response_schema_and_fields(response.json(), post_jobs_schema)


def test_create_job_response_against_get_request():
    payload = create_job_full_payload()
    response = create_job_request(base_url, endpoint, payload, headers)
    response_body = response.json()
    assert response.status_code == 200
    job_id = response_body['id']
    get_response = get_jobs_request(base_url, endpoint, job_id, headers=headers).json()
    validate_response_with_expected_json(create_job_required_properties(), response_body, get_response)
    validate_response_with_expected_json(create_job_additional_properties(), response_body, get_response)
    validate_response_schema_and_fields(response.json(), post_jobs_schema)


def test_create_job_with_nonexistent_property():
    payload = create_job_required_fields_payload()
    non_property = random_string(10)
    payload[non_property] = random_string(10)
    response = create_job_request(base_url, endpoint, payload, headers)
    response_body = response.json()
    assert response.status_code == 200
    assert non_property not in response_body
    job_id = response_body['id']
    get_response = get_jobs_request(base_url, endpoint, job_id, headers=headers)
    assert get_response.status_code == 200
    assert non_property not in get_response.json()


def test_create_job_wrong_property_data_type():
    payload = create_job_required_fields_payload()
    payload["target_fee"] = random_string(10)
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


@pytest.mark.parametrize("missing_property", create_job_required_properties())
def test_create_job_missing_required_field(missing_property):
    payload = missing_required_field_payload(create_job_required_fields_payload(), missing_property)
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


def test_create_job_empty_payload():
    response = create_job_request(base_url, endpoint, "{}", headers)
    assert response.status_code == 400


def test_create_job_unauthorized():
    payload = create_job_required_fields_payload()
    response = create_job_request(base_url, endpoint, payload, "")
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"


def test_create_job_wrong_job_type():
    payload = wrong_job_type_payload()
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


def test_create_job_wrong_agreement_type():
    payload = wrong_agreement_type_payload()
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


def test_create_job_wrong_source():
    payload = wrong_job_type_payload()
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


@pytest.mark.parametrize("date_props", ['preferred_start_date'])
def test_create_candidate_expiry_date_min_max_values(date_props):
    payload = create_job_full_payload()
    payload[date_props] = get_past_date(100)
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
    payload[date_props] = get_future_date(101)
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


@pytest.mark.parametrize("required_property", create_job_required_properties())
def test_create_job_required_property_set_to_null(required_property):
    payload = missing_required_field_payload(create_job_required_fields_payload(), required_property)
    payload[required_property] = None
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
