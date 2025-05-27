from src.be.configuration.config_parser import get_config_value
from src.be.definitions.organisations_definitions import create_organisations_request, delete_organisations_request, \
    get_organisations_request, delete_organisations_check_dependencies_request, \
    delete_organisations_ignore_dependencies_request
from src.be.utilities.get_core_api_data import get_organisations_by_id_from_core_api, add_activity_to_organisation, \
    add_alert_to_organisation, add_location_to_organisation
from src.be.utilities.organisations_utilities.request_payloads.create_organisation_payloads import \
    create_organisation_full_payload
from src.be.utilities.useful_functions import get_random_uuid, standard_headers, delete_headers

base_url = get_config_value("base_url")
endpoint = "organisations/"
headers = standard_headers()
delete_headers = delete_headers()


def test_delete_organisations_without_dependencies():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    delete_response = delete_organisations_request(base_url, endpoint, org_id, delete_headers)
    assert delete_response.status_code == 204
    get_response = get_organisations_request(base_url, endpoint, org_id, headers)
    assert get_response.status_code == 404
    core_api_response = get_organisations_by_id_from_core_api(org_id)
    assert core_api_response.status_code == 404, f"Response: {core_api_response.json()}"


def test_delete_organisations_unauthorized():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    delete_response = delete_organisations_request(base_url, endpoint, org_id, None)
    assert delete_response.status_code in (401, 403), f"Expected 401 or 403, but got {delete_response.status_code}"


def test_delete_organisations_nonexistent_id():
    delete_response = delete_organisations_request(base_url, endpoint, get_random_uuid(), delete_headers)
    assert delete_response.status_code == 404


def test_delete_organisations_wrong_endpoint():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(),
                                                   standard_headers())
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    delete_response = delete_organisations_request(base_url, "organisation", org_id, delete_headers)
    assert delete_response.status_code == 404


def test_delete_organisations_with_activities_checking_dependencies():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    add_activity_to_organisation(org_id)
    response = delete_organisations_check_dependencies_request(base_url, endpoint, org_id, delete_headers)
    assert response.status_code == 400


def test_delete_organisations_with_alerts_checking_dependencies():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    add_alert_to_organisation(org_id)
    response = delete_organisations_check_dependencies_request(base_url, endpoint, org_id, delete_headers)
    assert response.status_code == 400


#

def test_delete_organisations_with_locations_checking_dependencies():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    add_location_to_organisation(org_id)
    response = delete_organisations_check_dependencies_request(base_url, endpoint, org_id, delete_headers)
    assert response.status_code == 400


def test_delete_organisations_with_activities_ignore_dependencies():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    add_activity_to_organisation(org_id)
    response = delete_organisations_ignore_dependencies_request(base_url, endpoint, org_id, delete_headers)
    assert response.status_code == 204


def test_delete_organisations_with_alerts_ignore_dependencies():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    add_alert_to_organisation(org_id)
    response = delete_organisations_ignore_dependencies_request(base_url, endpoint, org_id, delete_headers)
    assert response.status_code == 204


#

def test_delete_organisations_with_locations_ignore_dependencies():
    create_response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert create_response.status_code == 200
    org_id = create_response.json()['id']
    add_location_to_organisation(org_id)
    response = delete_organisations_ignore_dependencies_request(base_url, endpoint, org_id, delete_headers)
    assert response.status_code == 204
