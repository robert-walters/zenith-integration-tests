from jsonschema import validate
from src.be.utilities.get_core_api_data import get_organisation_id_from_core_api, get_location_id_from_core_api
from src.be.configuration.config_parser import get_config_value
from src.be.definitions.organisations_definitions import get_organisations_request
from src.be.utilities.error_schema import error_schema
from src.be.utilities.organisations_utilities.json_schemas.get_organisations_schema import get_organisations_schema
from src.be.utilities.useful_functions import get_random_uuid, standard_headers, validate_response_schema_and_fields

base_url = get_config_value("base_url")
endpoint = "organisations/"
headers = standard_headers()


def test_get_organisations_by_id_successful_request():
    org_id = get_organisation_id_from_core_api(get_location_id_from_core_api())
    response = get_organisations_request(base_url, endpoint, org_id, headers)
    assert response.status_code == 200
    validate_response_schema_and_fields(response.json(), get_organisations_schema)


def test_get_organisations_by_id_unauthorized():
    org_id = get_organisation_id_from_core_api(get_location_id_from_core_api())
    response = get_organisations_request(base_url, endpoint, org_id, "")
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"


def test_get_organisations_by_nonexistent_id():
    response = get_organisations_request(base_url, endpoint, get_random_uuid(), headers)
    assert response.status_code == 404


def test_get_organisations_by_id_misspelled_endpoint():
    response = get_organisations_request(base_url, "organisation/", get_random_uuid(), headers)
    assert response.status_code == 404
    validate_response_schema_and_fields(response.json(), error_schema)


def test_get_organisations_by_id_wrong_format():
    response = get_organisations_request(base_url, endpoint, get_random_uuid() + "123", headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)
