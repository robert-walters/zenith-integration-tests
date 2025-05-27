import pytest
from src.be.definitions.candidates_definitions import get_candidate_id
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_activity_payload import *
from src.be.utilities.candidates_utilities.request_payloads.update_candidate_activity_payload import \
    update_candidate_activity_required_payload, \
    update_candidate_activity_full_payload, update_candidate_activity_original_mandatory_payload

base_url = get_config_value("base_url")
endpoint = "candidates/"
headers = standard_headers()

candidate_id = get_candidate_id()
activity_id = get_activity_id(base_url, endpoint, candidate_id, create_candidate_activity_required_payload(), headers)


def test_update_candidate_activity_excluded_missing_payload_fields():
    initial_candidate_activity = create_activity_request(base_url, endpoint, candidate_id,
                                                         create_candidate_activity_full_payload(), headers)
    assert initial_candidate_activity.status_code == 200
    act_id = initial_candidate_activity.json()['id']
    updated_payload = update_candidate_activity_required_payload()
    updated_activity_response = update_activity_request(base_url, endpoint, candidate_id, act_id, updated_payload,
                                                        headers)
    assert updated_activity_response.status_code == 200
    validate_response_with_expected_json(update_candidate_activity_required_props(), updated_activity_response.json(),
                                         get_request_body_json(updated_activity_response))
    for prop in update_candidate_activity_additional_props():
        assert prop in updated_activity_response.json()


def test_update_candidate_activity_integration():
    initial_candidate_activity = create_activity_request(base_url, endpoint, candidate_id,
                                                         create_candidate_activity_full_payload(), headers)
    assert initial_candidate_activity.status_code == 200
    act_id = initial_candidate_activity.json()['id']
    updated_payload = update_candidate_activity_full_payload()
    updated_candidate_response = update_activity_request(base_url, endpoint, candidate_id, act_id, updated_payload,
                                                         headers)
    assert updated_candidate_response.status_code == 200
    get_response = get_activity_request(base_url, endpoint, candidate_id, act_id, headers)
    assert get_response.status_code == 200
    validate_response_with_expected_json(update_candidate_activity_required_props(), updated_candidate_response.json(),
                                         get_response.json())


def test_update_candidate_activity_unauthorized():
    initial_candidate_activity = create_activity_request(base_url, endpoint, candidate_id,
                                                         create_candidate_activity_required_payload(), headers)
    assert initial_candidate_activity.status_code == 200
    act_id = initial_candidate_activity.json()['id']
    updated_payload = update_candidate_activity_required_payload()
    updated_candidate_response = update_activity_request(base_url, endpoint, candidate_id, act_id, updated_payload,
                                                         None)
    assert updated_candidate_response.status_code in (401, 403), f"Expected 401 or 403, but got {updated_candidate_response.status_code}"


def test_update_candidate_activity_missing_payload():
    initial_candidate_activity = create_activity_request(base_url, endpoint, candidate_id,
                                                         create_candidate_activity_required_payload(), headers)
    assert initial_candidate_activity.status_code == 200
    act_id = initial_candidate_activity.json()['id']
    updated_candidate_response = update_activity_request(base_url, endpoint, candidate_id, act_id, None,
                                                         headers)
    assert updated_candidate_response.status_code == 400


def test_update_candidate_activity_wrong_data_type():
    initial_candidate_activity = create_activity_request(base_url, endpoint, candidate_id,
                                                         create_candidate_activity_full_payload(), headers)
    assert initial_candidate_activity.status_code == 200
    act_id = initial_candidate_activity.json()['id']
    updated_payload = update_candidate_activity_full_payload()
    updated_payload["hidden"] = random_string(5)
    updated_candidate_response = update_activity_request(base_url, endpoint, candidate_id, act_id, updated_payload,
                                                         headers)
    assert updated_candidate_response.status_code == 400


def test_update_candidate_activity_original_full_payload():
    create_response = create_original_activity_request(base_url,
                                                       create_candidate_activity_original_full_payload(candidate_id),
                                                       headers)
    assert create_response.status_code == 200
    payload = update_candidate_activity_original_mandatory_payload(candidate_id)
    update_response = update_original_activity_request(base_url, create_response.json()['id'], payload, headers)
    assert update_response.status_code == 200
    validate_response_with_expected_json(update_candidate_activity_required_props(),
                                         get_request_body_json(update_response), update_response.json())


@pytest.mark.parametrize("required_property", create_candidate_activity_required_payload())
def test_update_candidate_activity_required_property_set_to_null(required_property):
    payload = create_candidate_activity_required_payload()
    response = create_activity_request(base_url, endpoint, candidate_id, payload, headers)
    assert response.status_code == 200
    update_payload = update_candidate_activity_required_payload()
    update_payload[required_property] = None
    activity_response = update_activity_request(base_url, endpoint, response.json()['candidate_id'], response.json()['id'], update_payload, headers)
    assert activity_response.status_code == 400
