import pytest
from src.be.configuration.config_parser import get_config_value
from src.be.definitions.jobs_definitions import create_job_request, update_job_request, \
    update_job_required_properties, update_job_additional_properties
from src.be.utilities.get_core_api_data import get_job_by_id_from_core_api
from src.be.utilities.job_utilities.request_payloads.update_job_payload import update_job_required_fields_payload, \
    update_job_full_payload
from src.be.utilities.job_utilities.request_payloads.create_job_payload import create_job_full_payload, \
    create_job_required_fields_payload
from src.be.utilities.useful_functions import get_random_remit, validate_response_with_expected_json, \
    get_request_body_json, get_past_date, get_future_date, standard_headers

base_url = get_config_value("base_url")
endpoint = "jobs/"
headers = standard_headers()
remit = get_random_remit()


def test_update_job_excluded_missing_payload_fields():
    initial_job = create_job_request(base_url, endpoint, create_job_full_payload(), headers)
    assert initial_job.status_code == 200
    job_id = initial_job.json()['id']
    updated_payload = update_job_required_fields_payload()
    updated_job_response = update_job_request(base_url, endpoint, job_id, updated_payload, headers)
    assert updated_job_response.status_code == 200
    validate_response_with_expected_json(update_job_required_properties(), updated_job_response.json(),
                                         get_request_body_json(updated_job_response))
    for prop in update_job_additional_properties():
        assert prop in updated_job_response.json()


def test_update_job_integration():
    initial_job = create_job_request(base_url, endpoint, create_job_full_payload(), headers)
    assert initial_job.status_code == 200
    job_id = initial_job.json()['id']
    updated_payload = update_job_full_payload()
    updated_job_response = update_job_request(base_url, endpoint, job_id, updated_payload, headers)
    assert updated_job_response.status_code == 200
    core_api_response = get_job_by_id_from_core_api(job_id)
    assert core_api_response.status_code == 200
    validate_response_with_expected_json(update_job_required_properties(), updated_job_response.json(),
                                         core_api_response.json())
    validate_response_with_expected_json(update_job_additional_properties(), updated_job_response.json(),
                                         core_api_response.json())


def test_update_job_unauthorized():
    initial_job = create_job_request(base_url, endpoint, create_job_full_payload(), headers)
    assert initial_job.status_code == 200
    job_id = initial_job.json()['id']
    updated_payload = update_job_required_fields_payload()
    updated_job_response = update_job_request(base_url, endpoint, job_id, updated_payload, "")
    assert updated_job_response.status_code in (401, 403), f"Expected 401 or 403, but got {updated_job_response.status_code}"


def test_update_job_missing_payload():
    initial_job = create_job_request(base_url, endpoint, create_job_full_payload(), headers)
    assert initial_job.status_code == 200
    job_id = initial_job.json()['id']
    updated_job_response = update_job_request(base_url, endpoint, job_id, "", headers)
    assert updated_job_response.status_code == 400


def test_update_job_wrong_data_type():
    initial_job = create_job_request(base_url, endpoint, create_job_full_payload(), headers)
    assert initial_job.status_code == 200
    job_id = initial_job.json()['id']
    update_payload = update_job_required_fields_payload()
    update_payload["job_posting_required"] = "true"
    updated_job_response = update_job_request(base_url, endpoint, job_id, update_payload, headers)
    assert updated_job_response.status_code == 400


@pytest.mark.parametrize("date_props", ['preferred_start_date'])
def test_create_candidate_expiry_date_min_max_values(date_props):
    payload = update_job_full_payload()
    payload[date_props] = get_past_date(100)
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
    payload[date_props] = get_future_date(101)
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


@pytest.mark.parametrize("required_property", create_job_required_fields_payload())
def test_update_job_required_property_set_to_null(required_property):
    payload = create_job_required_fields_payload()
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    update_payload = create_job_required_fields_payload()
    update_payload[required_property] = None
    activity_response = update_job_request(base_url, endpoint, response.json()['id'], update_payload, headers)
    assert activity_response.status_code == 400
