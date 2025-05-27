import pytest
from src.be.configuration.config_parser import get_config_value
from src.be.definitions.activity_definitions import get_activity_id, create_activity_request, update_activity_request, \
    update_client_activity_required_props, update_client_activity_additional_props, get_activity_request, \
    create_original_activity_request, update_original_activity_request
from src.be.definitions.clients_definitions import get_client_id
from src.be.utilities.clients_utilities.request_payloads.create_client_activity_payload import \
    create_client_activity_required_payload, create_client_activity_original_full_payload
from src.be.utilities.clients_utilities.request_payloads.update_client_activity_payload import \
    update_client_activity_required_payload, update_client_activity_full_payload, \
    update_client_activity_original_full_payload
from src.be.utilities.useful_functions import validate_response_with_expected_json, get_request_body_json, \
    random_string, standard_headers

base_url = get_config_value("base_url")
endpoint = "clients/"
headers = standard_headers()

client_id = get_client_id(base_url, endpoint, headers)
activity_id = get_activity_id(base_url, endpoint, client_id, create_client_activity_required_payload(), headers)


def test_update_client_activity_excluded_missing_payload_fields():
    act_id = activity_id
    updated_payload = update_client_activity_required_payload()
    updated_response = update_activity_request(base_url, endpoint, client_id, act_id, updated_payload,
                                               headers)
    assert updated_response.status_code == 200
    validate_response_with_expected_json(update_client_activity_required_props(), updated_response.json(),
                                         get_request_body_json(updated_response))
    for prop in update_client_activity_additional_props():
        assert prop not in updated_response.json()


def test_update_client_activity_integration():
    act_id = activity_id
    updated_payload = update_client_activity_full_payload()
    updated_response = update_activity_request(base_url, endpoint, client_id, act_id, updated_payload,
                                               headers)
    assert updated_response.status_code == 200
    get_response = get_activity_request(base_url, endpoint, client_id, act_id, headers)
    assert get_response.status_code == 200
    validate_response_with_expected_json(update_client_activity_additional_props(), updated_response.json(),
                                         get_response.json())


def test_update_client_activity_unauthorized():
    act_id = activity_id
    updated_payload = update_client_activity_required_payload()
    updated_response = update_activity_request(base_url, endpoint, client_id, act_id, updated_payload, None)
    assert updated_response.status_code in (401, 403), f"Expected 401 or 403, but got {updated_response.status_code}"


def test_update_client_activity_missing_payload():
    act_id = activity_id
    updated_response = update_activity_request(base_url, endpoint, client_id, act_id, None, headers)
    assert updated_response.status_code == 400


def test_update_client_activity_wrong_data_type():
    act_id = activity_id
    updated_payload = update_client_activity_full_payload()
    updated_payload["hidden"] = random_string(5)
    updated_response = update_activity_request(base_url, endpoint, client_id, act_id, updated_payload, headers)
    assert updated_response.status_code == 400


def test_update_client_activity_original_full_payload():
    create_response = create_original_activity_request(base_url,
                                                       create_client_activity_original_full_payload(client_id),
                                                       headers)
    assert create_response.status_code == 200
    payload = update_client_activity_original_full_payload(client_id)
    update_response = update_original_activity_request(base_url, create_response.json()['id'], payload, headers)
    assert update_response.status_code == 200
    validate_response_with_expected_json(update_client_activity_required_props(),
                                         get_request_body_json(update_response), update_response.json())


@pytest.mark.parametrize("required_property", create_client_activity_required_payload())
def test_update_client_activity_required_property_set_to_null(required_property):
    payload = create_client_activity_required_payload()
    response = create_activity_request(base_url, endpoint, client_id, payload, headers)
    assert response.status_code == 200
    update_payload = update_client_activity_required_payload()
    update_payload[required_property] = None
    activity_response = update_activity_request(base_url, endpoint, client_id, response.json()['id'], update_payload, headers)
    assert activity_response.status_code == 400
