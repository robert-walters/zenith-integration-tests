from src.be.configuration.config_parser import get_config_value
from src.be.definitions.jobs_definitions import get_jobs_request, create_job_request
from src.be.utilities.error_schema import error_schema
from src.be.utilities.job_utilities.json_schemas.get_jobs_by_id_schema import get_jobs_schema
from src.be.utilities.job_utilities.request_payloads.create_job_payload import create_job_full_payload
from src.be.utilities.useful_functions import get_random_uuid, standard_headers, validate_response_schema_and_fields
from src.be.configuration.config_parser import assert_by_auth_type

base_url = get_config_value("base_url")
endpoint = "jobs/"
headers = standard_headers()

job_id = create_job_request(base_url, endpoint, create_job_full_payload(), headers).json()['id']


def test_get_jobs_by_id_successful_request():
    response = get_jobs_request(base_url, endpoint, job_id, headers)
    assert response.status_code == 200
    validate_response_schema_and_fields(response.json(), get_jobs_schema)


def test_get_jobs_by_id_unauthorized():
    response = get_jobs_request(base_url, endpoint, job_id, "")
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"


def test_get_jobs_by_nonexistent_id():
    response = get_jobs_request(base_url, endpoint, get_random_uuid(), headers)
    assert response.status_code == 404


def test_get_jobs_by_id_misspelled_endpoint():
    response = get_jobs_request(base_url, "job/", get_random_uuid(), headers)
    xapi_setting = get_config_value("xapi")
    config = {"xapi": xapi_setting}
    assert_by_auth_type(response, config)


def test_get_jobs_by_id_wrong_format():
    response = get_jobs_request(base_url, endpoint, get_random_uuid() + "123", headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)
