from jsonschema.validators import validate

from src.be.definitions.clients_definitions import get_client_id
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_activity_payload import *
from src.be.utilities.clients_utilities.json_schemas.get_client_activity_schema import get_client_activity_schema
from src.be.utilities.clients_utilities.request_payloads.create_client_activity_payload import \
    create_client_activity_required_payload, create_client_activity_full_payload, \
    create_client_activity_original_full_payload
from src.be.configuration.config_parser import assert_by_auth_type

base_url = get_config_value("base_url")
endpoint = "clients/"
headers = standard_headers()

client_id = get_client_id(base_url, endpoint, headers)
activity_id = get_activity_id(base_url, endpoint, client_id, create_client_activity_required_payload(), headers)


def test_get_client_activity_by_id_successful_request():
    create_response = create_activity_request(base_url, endpoint, client_id,
                                              create_client_activity_full_payload(), headers)
    act_id = create_response.json()['id']
    get_response = get_activity_request(base_url, endpoint, client_id, act_id, headers)
    assert get_response.status_code == 200
    validate_response_schema_and_fields(get_response.json(), get_client_activity_schema)
    validate_response_with_expected_json(create_client_activity_required_props(), get_response.json(),
                                         create_response.json())
    validate_response_with_expected_json(create_client_activity_additional_props(), get_response.json(),
                                         create_response.json())


def test_get_client_activity_by_id_unauthorized():
    response = get_activity_request(base_url, endpoint, client_id, activity_id, None)
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"


def test_get_client_activity_by_nonexistent_id():
    response = get_activity_request(base_url, endpoint, activity_id, get_random_uuid(), headers)
    assert response.status_code == 404


def test_get_client_activity_by_id_misspelled_endpoint():
    response = get_activity_request(base_url, "client/", client_id, activity_id, headers)
    xapi_setting = get_config_value("xapi")
    config = {"xapi": xapi_setting}
    assert_by_auth_type(response, config)


def test_get_client_activity_original():
    create_response = create_original_activity_request(base_url,
                                                       create_client_activity_original_full_payload(client_id),
                                                       headers)
    assert create_response.status_code == 200
    get_response = get_original_activity_request(base_url, create_response.json()['id'], headers)
    assert get_response.status_code == 200
    validate_response_with_expected_json(create_client_activity_original_required_props(), get_response.json(),
                                         create_response.json())
    validate_response_with_expected_json(create_client_activity_additional_props(), get_response.json(),
                                         create_response.json())
