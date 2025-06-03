from jsonschema.validators import validate
from src.be.definitions.organisations_definitions import get_organisation_id
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_activity_payload import *
from src.be.utilities.error_schema import error_schema
from src.be.utilities.organisations_utilities.request_payloads.create_organisation_activity_payloads import \
    create_organisation_activity_full_payload, create_organisation_activity_original_full_payload
from src.be.utilities.organisations_utilities.request_payloads.create_organisation_payloads import \
    create_organisation_required_payload

base_url = get_config_value("base_url")
endpoint = "organisations/"
headers = standard_headers()
delete_headers = delete_headers()

org_id = get_organisation_id(base_url, endpoint, create_organisation_required_payload(), headers)
activity_id = get_activity_id(base_url, endpoint, org_id, create_organisation_activity_full_payload(), headers)


def test_delete_organisation_activities_without_dependencies():
    payload = create_organisation_activity_full_payload()
    post_response = create_activity_request(base_url, endpoint, org_id, payload, headers)
    assert post_response.status_code == 200
    act_id = post_response.json()['id']
    delete_response = delete_activity_request(base_url, endpoint, org_id, act_id, delete_headers)
    assert delete_response.status_code == 403
    get_response = get_activity_request(base_url, endpoint, org_id, act_id, headers)
    assert get_response.status_code == 200


def test_delete_organisation_activity_unauthorized():
    delete_response = delete_activity_request(base_url, endpoint, org_id, activity_id, "")
    assert delete_response.status_code in (401, 403), f"Expected 401 or 403, but got {delete_response.status_code}"


def test_delete_organisation_activity_nonexistent_id():
    delete_response = delete_activity_request(base_url, endpoint, org_id, org_id, delete_headers)
    assert delete_response.status_code == 403


def test_delete_organisation_activity_already_deleted():
    payload = create_organisation_activity_full_payload()
    post_response = create_activity_request(base_url, endpoint, org_id, payload,
                                            headers)
    assert post_response.status_code == 200
    act_id = post_response.json()['id']
    delete_response = delete_activity_request(base_url, endpoint, org_id, act_id, delete_headers)
    assert delete_response.status_code == 403


def test_delete_organisation_activity_original():
    payload = create_organisation_activity_original_full_payload(org_id)
    create_response = create_original_activity_request(base_url, payload, headers)
    assert create_response.status_code == 200
    act_id = create_response.json()['id']
    delete_response = delete_original_activity_request(base_url, act_id, delete_headers)
    assert delete_response.status_code == 403
    get_response = get_original_activity_request(base_url, act_id, headers)
    assert get_response.status_code == 200
