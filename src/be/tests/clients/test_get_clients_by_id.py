import requests
from jsonschema import validate
from src.be.utilities.get_core_api_data import get_client_id_from_core_api
from src.be.configuration.config_parser import get_config_value
from src.be.definitions.clients_definitions import get_client_request
from src.be.utilities.error_schema import error_schema
from src.be.utilities.clients_utilities.json_schemas.get_client_by_id_schema import get_clients_schema
from src.be.utilities.useful_functions import get_random_uuid, random_string, standard_headers, \
    validate_response_schema_and_fields
from src.be.configuration.config_parser import assert_by_auth_type

base_url = get_config_value("base_url")
endpoint = "clients/"
headers = standard_headers()


def test_get_client_by_id_successful_request():
    client_id = get_client_id_from_core_api()
    response = get_client_request(base_url, endpoint, client_id, headers)
    assert response.status_code == 200
    validate_response_schema_and_fields(response.json(), get_clients_schema)


def test_get_clients_by_unauthorized():
    client_id = get_client_id_from_core_api()
    response = get_client_request(base_url, endpoint, client_id, "")
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"


def test_get_client_by_nonexistent_id():
    response = get_client_request(base_url, endpoint, get_random_uuid(), headers)
    assert response.status_code == 404


def test_get_client_by_id_null():
    response = requests.get(base_url + endpoint, headers=headers)
    assert response.status_code == 404


def test_get_client_by_id_misspelled_endpoint():
    response = get_client_request(base_url, "client/", get_random_uuid(), headers)
    xapi_setting = get_config_value("xapi")
    config = {"xapi": xapi_setting}
    assert_by_auth_type(response, config)


def test_get_client_by_id_wrong_format():
    response = get_client_request(base_url, endpoint, random_string(10), headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)
