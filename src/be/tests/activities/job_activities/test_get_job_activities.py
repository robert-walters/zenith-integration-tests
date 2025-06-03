from src.be.configuration.config_parser import get_config_value
from src.be.definitions.activity_definitions import get_activity_request, create_activity_request, \
    create_job_activity_required_props, create_job_activity_additional_props, get_activity_id, \
    create_original_activity_request, get_original_activity_request, create_job_activity_original_required_props
from src.be.definitions.jobs_definitions import get_job_id
from src.be.utilities.error_schema import error_schema
from src.be.utilities.job_utilities.json_schemas.get_job_activities_schema import get_job_activities_schema
from src.be.utilities.job_utilities.request_payloads.create_job_activity_payload import \
    create_job_activity_full_payload, create_job_activity_original_full_payload
from src.be.utilities.job_utilities.request_payloads.create_job_payload import create_job_required_fields_payload
from src.be.utilities.useful_functions import validate_response_with_expected_json, get_random_uuid, standard_headers, \
     validate_response_schema_and_fields
from src.be.configuration.config_parser import assert_by_auth_type

base_url = get_config_value("base_url")
endpoint = "jobs/"
headers = standard_headers()

job_id = get_job_id(base_url, endpoint, create_job_required_fields_payload(), headers)
activity_id = get_activity_id(base_url, endpoint, job_id, create_job_activity_full_payload(), headers)


def test_get_job_activity_by_id_successful_request():
    create_response = create_activity_request(base_url, endpoint, job_id, create_job_activity_full_payload(), headers)
    assert create_response.status_code == 200
    activity_id = create_response.json()['id']
    get_response = get_activity_request(base_url, endpoint, job_id, activity_id, headers)
    assert get_response.status_code == 200
    validate_response_schema_and_fields(get_response.json(), get_job_activities_schema)
    validate_response_with_expected_json(create_job_activity_required_props(), get_response.json(),
                                         create_response.json())
    validate_response_with_expected_json(create_job_activity_additional_props(), get_response.json(),
                                         create_response.json())


def test_get_job_activity_by_id_unauthorized():
    response = get_activity_request(base_url, endpoint, job_id, activity_id, None)
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"


def test_get_job_activity_by_nonexistent_id():
    response = get_activity_request(base_url, endpoint, activity_id, get_random_uuid(), headers)
    assert response.status_code == 404
    validate_response_schema_and_fields(response.json(), error_schema)


def test_get_job_activity_by_id_misspelled_endpoint():
    response = get_activity_request(base_url, "job/", job_id, activity_id, headers)
    xapi_setting = get_config_value("xapi")
    config = {"xapi": xapi_setting}
    assert_by_auth_type(response, config)


def test_get_job_activity_original():
    create_response = create_original_activity_request(base_url,
                                                       create_job_activity_original_full_payload(job_id),
                                                       headers)
    assert create_response.status_code == 200
    get_response = get_original_activity_request(base_url, create_response.json()['id'], headers)
    assert get_response.status_code == 200
    validate_response_with_expected_json(create_job_activity_original_required_props(), get_response.json(),
                                         create_response.json())
    validate_response_with_expected_json(create_job_activity_additional_props(), get_response.json(),
                                         create_response.json())
