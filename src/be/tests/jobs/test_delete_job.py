from jsonschema.validators import validate

from src.be.configuration.config_parser import get_config_value
from src.be.definitions.candidates_definitions import get_candidate_id
from src.be.definitions.jobs_definitions import create_job_request, delete_job_ignore_dependencies, get_jobs_request, \
    delete_job_checking_dependencies
from src.be.utilities.get_core_api_data import get_job_by_id_from_core_api, add_activity_to_job, add_alert_to_job, \
    add_candidate_to_job
from src.be.utilities.job_utilities.request_payloads.create_job_payload import create_job_required_fields_payload
from src.be.utilities.error_schema import error_schema
from src.be.utilities.useful_functions import get_random_uuid, wrong_headers, standard_headers, delete_headers

base_url = get_config_value("base_url")
endpoint = "jobs/"
headers = standard_headers()
delete_headers = delete_headers()


def test_delete_job_without_dependencies():
    post_response = create_job_request(base_url, endpoint, create_job_required_fields_payload(), headers)
    assert post_response.status_code == 200
    job_id = post_response.json()['id']
    delete_response = delete_job_ignore_dependencies(base_url, endpoint, job_id, delete_headers)
    assert delete_response.status_code == 204
    get_response = get_jobs_request(base_url, endpoint + job_id, "", headers)
    assert get_response.status_code == 404
    core_response = get_job_by_id_from_core_api(job_id)
    assert core_response.status_code == 404


def test_delete_job_wrong_content_type():
    heads = wrong_headers()
    post_response = create_job_request(base_url, endpoint, create_job_required_fields_payload(), headers)
    assert post_response.status_code == 200
    job_id = post_response.json()['id']
    delete_response = delete_job_ignore_dependencies(base_url, endpoint, job_id, heads)
    assert delete_response.status_code in [400, 415]


def test_delete_job_unauthorized():
    post_response = create_job_request(base_url, endpoint, create_job_required_fields_payload(), headers)
    assert post_response.status_code == 200
    job_id = post_response.json()['id']
    delete_response = delete_job_ignore_dependencies(base_url, endpoint, job_id, "")
    assert delete_response.status_code in (401, 403), f"Expected 401 or 403, but got {delete_response.status_code}"


def test_delete_job_nonexistent_id():
    job_id = get_random_uuid()
    delete_response = delete_job_checking_dependencies(base_url, endpoint, job_id, delete_headers)
    assert delete_response.status_code == 404
    validate(delete_response.json(), schema=error_schema)


def test_delete_job_already_deleted():
    post_response = create_job_request(base_url, endpoint, create_job_required_fields_payload(), headers)
    assert post_response.status_code == 200
    job_id = post_response.json()['id']
    delete_response = delete_job_checking_dependencies(base_url, endpoint, job_id, delete_headers)
    assert delete_response.status_code == 204
    delete_response = delete_job_checking_dependencies(base_url, endpoint, job_id, delete_headers)
    assert delete_response.status_code == 404
    validate(delete_response.json(), schema=error_schema)


def test_delete_job_with_activities_checking_dependencies():
    post_response = create_job_request(base_url, endpoint, create_job_required_fields_payload(), headers)
    assert post_response.status_code == 200
    job_id = post_response.json()['id']
    add_activity_to_job(job_id)
    delete_response = delete_job_checking_dependencies(base_url, endpoint, job_id, delete_headers)
    assert delete_response.status_code == 400
    validate(delete_response.json(), schema=error_schema)


def test_delete_job_with_alerts_checking_dependencies():
    post_response = create_job_request(base_url, endpoint, create_job_required_fields_payload(), headers)
    assert post_response.status_code == 200
    job_id = post_response.json()['id']
    add_alert_to_job(job_id)
    delete_response = delete_job_checking_dependencies(base_url, endpoint, job_id, delete_headers)
    assert delete_response.status_code == 400
    validate(delete_response.json(), schema=error_schema)


def test_delete_job_with_candidates_checking_dependencies():
    post_response = create_job_request(base_url, endpoint, create_job_required_fields_payload(), headers)
    assert post_response.status_code == 200
    job_id = post_response.json()['id']
    candidate_id = get_candidate_id()
    add_candidate_to_job(candidate_id, job_id)
    delete_response = delete_job_checking_dependencies(base_url, endpoint, job_id, delete_headers)
    assert delete_response.status_code == 400
    validate(delete_response.json(), schema=error_schema)


def test_delete_job_with_candidates_ignore_dependencies():
    post_response = create_job_request(base_url, endpoint, create_job_required_fields_payload(), headers)
    assert post_response.status_code == 200
    job_id = post_response.json()['id']
    candidate_id = get_candidate_id()
    add_candidate_to_job(candidate_id, job_id)
    delete_response = delete_job_ignore_dependencies(base_url, endpoint, job_id, delete_headers)
    assert delete_response.status_code == 204


def test_delete_job_with_alerts_ignore_dependencies():
    post_response = create_job_request(base_url, endpoint, create_job_required_fields_payload(), headers)
    assert post_response.status_code == 200
    job_id = post_response.json()['id']
    add_alert_to_job(job_id)
    delete_response = delete_job_ignore_dependencies(base_url, endpoint, job_id, delete_headers)
    assert delete_response.status_code == 204


def test_delete_job_with_activities_ignore_dependencies():
    post_response = create_job_request(base_url, endpoint, create_job_required_fields_payload(), headers)
    assert post_response.status_code == 200
    job_id = post_response.json()['id']
    add_activity_to_job(job_id)
    delete_response = delete_job_ignore_dependencies(base_url, endpoint, job_id, delete_headers)
    assert delete_response.status_code == 204
