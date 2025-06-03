from src.be.configuration.config_parser import get_config_value
from src.be.utilities.clients_utilities.request_payloads.create_client_payload import create_client_full_payload
from src.be.utilities.get_core_api_data import get_client_by_id_from_core_api, add_activity_to_client, \
    add_alert_to_client, add_review_to_client
from src.be.definitions.clients_definitions import create_client_request, delete_client_request, get_client_request, \
    delete_clients_check_dependencies_request, delete_clients_ignore_dependencies_request
from src.be.utilities.useful_functions import standard_headers, delete_headers

base_url = get_config_value("base_url")
endpoint = "clients/"
headers = standard_headers()
delete_headers = delete_headers()


def test_delete_client_without_dependencies():
    create_response = create_client_request(base_url, endpoint, create_client_full_payload(), headers)
    assert create_response.status_code == 200
    client_id = create_response.json()['id']
    delete_response = delete_client_request(base_url, endpoint, client_id, delete_headers)
    assert delete_response.status_code == 403
    get_response = get_client_request(base_url, endpoint, client_id, headers)
    assert get_response.status_code == 200
    core_api_response = get_client_by_id_from_core_api(client_id)
    assert core_api_response.status_code == 200


def test_delete_client_with_activities_checking_dependencies():
    create_response = create_client_request(base_url, endpoint, create_client_full_payload(), headers)
    assert create_response.status_code == 200
    client_id = create_response.json()['id']
    add_activity_to_client(client_id)
    response = delete_clients_check_dependencies_request(base_url, endpoint, client_id, delete_headers)
    assert response.status_code == 403


def test_delete_client_with_alerts_checking_dependencies():
    create_response = create_client_request(base_url, endpoint, create_client_full_payload(), headers)
    assert create_response.status_code == 200
    client_id = create_response.json()['id']
    add_alert_to_client(client_id)
    response = delete_clients_check_dependencies_request(base_url, endpoint, client_id, delete_headers)
    assert response.status_code == 403


def test_delete_client_with_reviews_checking_dependencies():
    create_response = create_client_request(base_url, endpoint, create_client_full_payload(), headers)
    assert create_response.status_code == 200
    client_id = create_response.json()['id']
    add_review_to_client(client_id)
    response = delete_clients_check_dependencies_request(base_url, endpoint, client_id, delete_headers)
    assert response.status_code == 403


def test_delete_client_with_activities_ignore_dependencies():
    create_response = create_client_request(base_url, endpoint, create_client_full_payload(), headers)
    assert create_response.status_code == 200
    client_id = create_response.json()['id']
    add_activity_to_client(client_id)
    response = delete_clients_ignore_dependencies_request(base_url, endpoint, client_id, delete_headers)
    assert response.status_code == 403


def test_delete_client_with_alerts_ignore_dependencies():
    create_response = create_client_request(base_url, endpoint, create_client_full_payload(), headers)
    assert create_response.status_code == 200
    client_id = create_response.json()['id']
    add_alert_to_client(client_id)
    response = delete_clients_ignore_dependencies_request(base_url, endpoint, client_id, delete_headers)
    assert response.status_code == 403


def test_delete_client_with_reviews_ignore_dependencies():
    create_response = create_client_request(base_url, endpoint, create_client_full_payload(), headers)
    assert create_response.status_code == 200
    client_id = create_response.json()['id']
    add_review_to_client(client_id)
    response = delete_clients_ignore_dependencies_request(base_url, endpoint, client_id, delete_headers)
    assert response.status_code == 403


def test_delete_client_unauthorized():
    create_response = create_client_request(base_url, endpoint, create_client_full_payload(), headers)
    assert create_response.status_code == 200
    client_id = create_response.json()['id']
    response = delete_clients_ignore_dependencies_request(base_url, endpoint, client_id, "")
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"

