import pytest
from jsonschema.validators import validate

from src.be.configuration.config_parser import get_config_value
from src.be.definitions.activity_definitions import create_activity_request, create_client_activity_required_props, \
    create_client_activity_additional_props, get_activity_request, create_original_activity_request
from src.be.definitions.clients_definitions import get_client_id
from src.be.utilities.clients_utilities.request_payloads.create_client_activity_payload import \
    create_client_activity_required_payload, create_client_activity_full_payload, \
    create_client_activity_original_full_payload, create_client_activity_original_mandatory_payload
from src.be.utilities.clients_utilities.json_schemas.post_client_activity_schema import post_client_activity_schema
from src.be.utilities.error_schema import error_schema
from src.be.utilities.useful_functions import validate_response_with_expected_json, \
    missing_required_field_payload, random_string, standard_headers
from src.be.utilities.useful_functions import validate_response_schema_and_fields
from src.be.configuration.config_parser import assert_by_auth_type

base_url = get_config_value("base_url")
endpoint = "clients/"
headers = standard_headers()
client_id = get_client_id(base_url, endpoint, headers)


def test_create_client_activity_mandatory_payload():
    payload = create_client_activity_required_payload()
    create_response = create_activity_request(base_url, endpoint, client_id, payload, headers)
    assert create_response.status_code == 200
    validate_response_schema_and_fields(create_response.json(), post_client_activity_schema)


def test_create_client_activity_full_payload():
    payload = create_client_activity_full_payload()
    create_response = create_activity_request(base_url, endpoint, client_id, payload, headers)
    assert create_response.status_code == 200
    validate_response_schema_and_fields(create_response.json(), post_client_activity_schema)


def test_create_client_activity_integration():
    create_response = create_activity_request(base_url, endpoint, client_id,
                                              create_client_activity_full_payload(), headers)
    act_id = create_response.json()['id']
    assert create_response.status_code == 200
    get_response = get_activity_request(base_url, endpoint, client_id, act_id, headers)
    assert get_response.status_code == 200
    validate_response_with_expected_json(create_client_activity_required_props(), create_response.json(),
                                         get_response.json())
    validate_response_with_expected_json(create_client_activity_additional_props(), create_response.json(),
                                         get_response.json())


@pytest.mark.parametrize("missing_property", create_client_activity_required_props())
def test_create_client_activity_missing_required_properties(missing_property):
    payload = missing_required_field_payload(create_client_activity_required_payload(), missing_property)
    activity_response = create_activity_request(base_url, endpoint, client_id, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_client_activity_unauthorized():
    payload = create_client_activity_required_payload()
    activity_response = create_activity_request(base_url, endpoint, client_id, payload, None)
    assert activity_response.status_code in (401, 403), f"Expected 401 or 403, but got {activity_response.status_code}"


def test_create_client_activity_wrong_endpoint_name():
    payload = create_client_activity_required_payload()
    activity_response = create_activity_request(base_url, "client/", client_id, payload, headers)
    xapi_setting = get_config_value("xapi")
    config = {"xapi": xapi_setting}
    assert_by_auth_type(activity_response, config)


def test_create_client_activity_empty_payload():
    activity_response = create_activity_request(base_url, endpoint, client_id, None, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_client_activity_wrong_type():
    payload = create_client_activity_full_payload()
    payload['type'] = random_string(10)
    activity_response = create_activity_request(base_url, endpoint, client_id, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_client_activity_wrong_source():
    payload = create_client_activity_full_payload()
    payload['source'] = random_string(10)
    activity_response = create_activity_request(base_url, endpoint, client_id, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_client_activity_wrong_event_type():
    payload = create_client_activity_full_payload()
    payload['event_type'] = random_string(10)
    activity_response = create_activity_request(base_url, endpoint, client_id, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)

def test_create_client_activity_wrong_outcome():
    payload = create_client_activity_full_payload()
    payload['outcome'] = random_string(10)
    activity_response = create_activity_request(base_url, endpoint, client_id, payload, headers)
    assert activity_response.status_code == 400
    validate_response_schema_and_fields(activity_response.json(), error_schema)


def test_create_client_activity_original_full_payload():
    payload = create_client_activity_original_full_payload(client_id)
    activity_response = create_original_activity_request(base_url, payload, headers)
    assert activity_response.status_code == 200
    validate_response_schema_and_fields(activity_response.json(), post_client_activity_schema)


def test_create_client_activity_original_mandatory_payload():
    payload = create_client_activity_original_mandatory_payload(client_id)
    activity_response = create_original_activity_request(base_url, payload, headers)
    assert activity_response.status_code == 200
    validate_response_schema_and_fields(activity_response.json(), post_client_activity_schema)


@pytest.mark.parametrize("required_property", create_client_activity_required_props())
def test_create_client_activity_required_property_set_to_null(required_property):
    payload = missing_required_field_payload(create_client_activity_required_payload(), required_property)
    payload[required_property] = None
    activity_response = create_activity_request(base_url, endpoint, client_id, payload, headers)
    assert activity_response.status_code == 400
