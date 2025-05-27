import pytest

from src.be.configuration.config_parser import get_config_value
from src.be.utilities.clients_utilities.request_payloads.update_client_payload import update_client_full_payload, \
    update_client_required_fields_payload
from src.be.utilities.get_core_api_data import get_client_by_id_from_core_api
from src.be.utilities.clients_utilities.request_payloads.create_client_payload import \
    create_client_required_fields_payload
from src.be.definitions.clients_definitions import *
from src.be.utilities.error_schema import error_schema
from src.be.utilities.useful_functions import get_random_uuid, validate_response_with_expected_json, standard_headers, \
    validate_response_schema_and_fields

base_url = get_config_value("base_url")
endpoint = "clients/"
headers = standard_headers()


def test_update_client_successful_request():
    payload = create_client_full_payload()
    client_id = create_client_request(base_url, endpoint, payload, headers).json()['id']
    updated_payload = update_client_full_payload()
    update_response = update_client_request(base_url, endpoint, client_id, updated_payload, headers)
    assert update_response.status_code == 200
    assert update_response.json()['id'] == client_id
    validate_response_with_expected_json(update_client_required_props(), update_response.json(), updated_payload)
    validate_response_with_expected_json(update_client_additional_props(), update_response.json(), updated_payload)


def test_update_client_integration():
    payload = create_client_full_payload()
    client_id = create_client_request(base_url, endpoint, payload, headers).json()['id']
    updated_payload = update_client_full_payload()
    update_response = update_client_request(base_url, endpoint, client_id, updated_payload, headers)
    assert update_response.status_code == 200
    core_api_data = get_client_by_id_from_core_api(client_id)
    assert core_api_data.status_code == 200
    validate_response_with_expected_json(update_client_required_props(), update_response.json(), core_api_data.json())
    validate_response_with_expected_json(update_client_additional_props(), update_response.json(), core_api_data.json())


def test_update_client_unauthorized():
    payload = create_client_required_fields_payload()
    client_id = create_client_request(base_url, endpoint, payload, headers).json()['id']
    updated_payload = update_client_required_fields_payload()
    update_response = update_client_request(base_url, endpoint, client_id, updated_payload, "")
    assert update_response.status_code in (401, 403), f"Expected 401 or 403, but got {update_response.status_code}"


def test_update_client_missing_required_field():
    payload = create_client_required_fields_payload()
    client_id = create_client_request(base_url, endpoint, payload, headers).json()['id']
    updated_payload = update_client_required_fields_payload()
    updated_payload.pop("first_name", None)  # Ensure 'first_name' is missing
    update_response = update_client_request(base_url, endpoint, client_id, updated_payload, headers)
    assert update_response.status_code == 400
    validate_response_schema_and_fields(update_response.json(), error_schema)


def test_update_client_nonexistent_client():
    client_id = get_random_uuid()
    updated_payload = update_client_required_fields_payload()
    update_response = update_client_request(base_url, endpoint, client_id, updated_payload, headers)
    assert update_response.status_code == 404
    validate_response_schema_and_fields(update_response.json(), error_schema)


def test_update_client_with_extra_payload_field():
    payload = create_client_required_fields_payload()
    client_id = create_client_request(base_url, endpoint, payload, headers).json()['id']
    updated_payload = update_client_required_fields_payload()
    updated_payload['extra_field'] = "extra value"
    update_response = update_client_request(base_url, endpoint, client_id, updated_payload, headers)
    assert update_response.status_code == 200
    assert "extra_field" not in update_response.json()


def test_update_client_with_empty_payload():
    payload = update_client_required_fields_payload()
    client_id = create_client_request(base_url, endpoint, payload, headers).json()['id']
    update_response = update_client_request(base_url, endpoint, client_id, "{}", headers)
    assert update_response.status_code == 400
    validate_response_schema_and_fields(update_response.json(), error_schema)


def test_update_client_with_invalid_data_types():
    payload = update_client_required_fields_payload()
    client_id = create_client_request(base_url, endpoint, payload, headers).json()['id']
    payload['first_name'] = 123456  # Invalid data type for 'first_name'
    update_response = update_client_request(base_url, endpoint, client_id, payload, headers)
    assert update_response.status_code == 400
    validate_response_schema_and_fields(update_response.json(), error_schema)


@pytest.mark.parametrize("required_property", create_client_required_fields_payload())
def test_update_client_required_property_set_to_null(required_property):
    payload = create_client_required_fields_payload()
    response = create_client_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    update_payload = create_client_required_fields_payload()
    update_payload[required_property] = None
    activity_response = update_client_request(base_url, endpoint, response.json()['id'], update_payload, headers)
    assert activity_response.status_code == 400
