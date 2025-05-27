from jsonschema.validators import validate

from src.be.configuration.config_parser import get_config_value
from src.be.definitions.activity_definitions import get_activity_id, create_activity_request, delete_activity_request, \
    get_activity_request, create_original_activity_request, delete_original_activity_request, \
    get_original_activity_request
from src.be.definitions.clients_definitions import get_client_id
from src.be.utilities.clients_utilities.request_payloads.create_client_activity_payload import \
    create_client_activity_required_payload, create_client_activity_full_payload, \
    create_client_activity_original_full_payload
from src.be.utilities.error_schema import error_schema
from src.be.utilities.useful_functions import standard_headers, delete_headers

base_url = get_config_value("base_url")
endpoint = "clients/"
headers = standard_headers()
delete_headers = delete_headers()

client_id = get_client_id(base_url, endpoint, headers)
activity_id = get_activity_id(base_url, endpoint, client_id, create_client_activity_required_payload(), headers)


def test_delete_client_activities_successful_request():
    payload = create_client_activity_full_payload()
    post_response = create_activity_request(base_url, endpoint, client_id, payload, headers)
    assert post_response.status_code == 200
    act_id = post_response.json()['id']
    delete_response = delete_activity_request(base_url, endpoint, client_id, act_id, delete_headers)
    assert delete_response.status_code == 204
    get_response = get_activity_request(base_url, endpoint, client_id, act_id, headers)
    assert get_response.status_code == 404


def test_delete_client_activity_unauthorized():
    post_response = create_activity_request(base_url, endpoint, client_id, create_client_activity_full_payload(),
                                            headers)
    assert post_response.status_code == 200
    act_id = post_response.json()['id']
    delete_response = delete_activity_request(base_url, endpoint, client_id, act_id, "")
    assert delete_response.status_code in (401, 403), f"Expected 401 or 403, but got {delete_response.status_code}"


def test_delete_client_activity_nonexistent_id():
    post_response = create_activity_request(base_url, endpoint, client_id, create_client_activity_full_payload(),
                                            headers)
    assert post_response.status_code == 200
    delete_response = delete_activity_request(base_url, endpoint, client_id, client_id, delete_headers)
    assert delete_response.status_code == 404
    validate(delete_response.json(), schema=error_schema)


def test_delete_client_activity_already_deleted():
    post_response = create_activity_request(base_url, endpoint, client_id, create_client_activity_full_payload(),
                                            headers)
    assert post_response.status_code == 200
    act_id = post_response.json()['id']
    delete_response = delete_activity_request(base_url, endpoint, client_id, act_id, delete_headers)
    assert delete_response.status_code == 204
    delete_response = delete_activity_request(base_url, endpoint, client_id, act_id, delete_headers)
    assert delete_response.status_code == 404
    validate(delete_response.json(), schema=error_schema)


def test_delete_client_activity_original():
    payload = create_client_activity_original_full_payload(client_id)
    create_response = create_original_activity_request(base_url, payload, headers)
    assert create_response.status_code == 200
    act_id = create_response.json()['id']
    delete_response = delete_original_activity_request(base_url, act_id, delete_headers)
    assert delete_response.status_code == 204
    get_response = get_original_activity_request(base_url, act_id, headers)
    assert get_response.status_code == 404
