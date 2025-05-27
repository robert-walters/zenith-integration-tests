import pytest
from jsonschema.validators import validate

from src.be.configuration.config_parser import get_config_value
from src.be.utilities.get_core_api_data import get_client_by_id_from_core_api
from src.be.utilities.clients_utilities.request_payloads.create_client_payload import \
    create_client_required_fields_payload, create_client_full_payload
from src.be.definitions.clients_definitions import create_client_request, create_client_required_props, \
    get_client_request, create_client_additional_props
from src.be.utilities.clients_utilities.json_schemas.post_client_schema import post_client_schema
from src.be.utilities.useful_functions import get_request_body_json, random_string, \
    validate_response_with_expected_json, missing_required_field_payload, standard_headers, \
    validate_response_schema_and_fields

base_url = get_config_value("base_url")
endpoint = "clients/"
headers = standard_headers()


def test_create_client_mandatory_payload():
    payload = create_client_required_fields_payload()
    response = create_client_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    validate_response_schema_and_fields(response.json(), post_client_schema)


def test_create_client_full_payload():
    payload = create_client_full_payload()
    response = create_client_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    validate_response_schema_and_fields(response.json(), post_client_schema)


def test_create_client_response_against_get_request():
    payload = create_client_full_payload()
    response = create_client_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    validate(response.json(), schema=post_client_schema)
    client_id = response.json()['id']
    get_response = get_client_request(base_url, endpoint, client_id, headers=headers)
    assert get_response.status_code == 200
    validate_response_schema_and_fields(response.json(), post_client_schema)


def test_create_client_integration():
    payload = create_client_full_payload()
    response = create_client_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    validate(response.json(), schema=post_client_schema)
    client_id = response.json()['id']
    core_api_data = get_client_by_id_from_core_api(client_id)
    assert core_api_data.status_code == 200
    validate_response_schema_and_fields(response.json(), post_client_schema)
    validate_response_with_expected_json(create_client_required_props(), response.json(), core_api_data.json())
    validate_response_with_expected_json(create_client_additional_props(), response.json(), core_api_data.json())


def test_create_client_with_nonexistent_property():
    payload = create_client_required_fields_payload()
    non_property = random_string(10)
    payload[non_property] = random_string(10)
    response = create_client_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    assert non_property not in response.json()
    client_id = response.json()['id']
    get_response = get_client_request(base_url, endpoint, client_id, headers=headers)
    assert get_response.status_code == 200
    assert non_property not in get_response.json()


@pytest.mark.parametrize("missing_property", create_client_required_props())
def test_create_client_missing_required_field(missing_property):
    payload = missing_required_field_payload(create_client_required_fields_payload(), missing_property)
    response = create_client_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


def test_create_client_empty_payload():
    response = create_client_request(base_url, endpoint, "{}", headers)
    assert response.status_code == 400


def test_create_client_unauthorized():
    payload = create_client_required_fields_payload()
    response = create_client_request(base_url, endpoint, payload, "")
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"


@pytest.mark.parametrize("required_property", create_client_required_props())
def test_create_client_required_property_set_to_null(required_property):
    payload = missing_required_field_payload(create_client_required_fields_payload(), required_property)
    payload[required_property] = None
    response = create_client_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400
