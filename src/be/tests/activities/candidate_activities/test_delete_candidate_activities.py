from jsonschema.validators import validate

from src.be.definitions.candidates_definitions import get_candidate_id
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_activity_payload import *
from src.be.utilities.error_schema import error_schema

base_url = get_config_value("base_url")
endpoint = "candidates/"
headers = standard_headers()
delete_headers = delete_headers()

candidate_id = get_candidate_id()
activity_id = get_activity_id(base_url, endpoint, candidate_id, create_candidate_activity_required_payload(), headers)


def test_delete_candidate_activities_without_dependencies():
    payload = create_candidate_activity_full_payload()
    post_response = create_activity_request(base_url, endpoint, candidate_id, payload, headers)
    assert post_response.status_code == 200
    act_id = post_response.json()['id']
    delete_response = delete_activity_request(base_url, endpoint, candidate_id, act_id, delete_headers)
    assert delete_response.status_code == 403
    get_response = get_activity_request(base_url, endpoint, candidate_id, act_id, headers)
    assert get_response.status_code == 200

def test_delete_candidate_activity_unauthorized():
    post_response = create_activity_request(base_url, endpoint, candidate_id, create_candidate_activity_full_payload(),
                                            headers)
    assert post_response.status_code == 200
    act_id = post_response.json()['id']
    delete_response = delete_activity_request(base_url, endpoint, candidate_id, act_id, "")
    assert delete_response.status_code in (401, 403), f"Expected 401 or 403, but got {delete_response.status_code}"


def test_delete_candidate_activity_nonexistent_id():
    post_response = create_activity_request(base_url, endpoint, candidate_id, create_candidate_activity_full_payload(),
                                            headers)
    assert post_response.status_code == 200
    # using candidate id instead of candidate activity id
    delete_response = delete_activity_request(base_url, endpoint, candidate_id, candidate_id, delete_headers)
    assert delete_response.status_code == 403


def test_delete_candidate_activity_already_deleted():
    post_response = create_activity_request(base_url, endpoint, candidate_id, create_candidate_activity_full_payload(),
                                            headers)
    assert post_response.status_code == 200
    act_id = post_response.json()['id']
    delete_response = delete_activity_request(base_url, endpoint, candidate_id, act_id, delete_headers)
    assert delete_response.status_code == 403


def test_delete_candidate_activity_original():
    payload = create_candidate_activity_original_full_payload(candidate_id)
    create_response = create_original_activity_request(base_url, payload, headers)
    assert create_response.status_code == 200
    act_id = create_response.json()['id']
    delete_response = delete_original_activity_request(base_url, act_id, delete_headers)
    assert delete_response.status_code == 403
