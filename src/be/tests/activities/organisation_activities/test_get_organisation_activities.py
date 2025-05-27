from jsonschema.validators import validate

from src.be.configuration.config_parser import get_config_value
from src.be.definitions.activity_definitions import get_activity_request, create_activity_request, \
    get_activity_id, \
    create_organisation_activity_required_props, create_organisation_activity_additional_props, \
    create_original_activity_request, get_original_activity_request, \
    create_organisation_activity_original_required_props
from src.be.definitions.organisations_definitions import get_organisation_id
from src.be.utilities.error_schema import error_schema
from src.be.utilities.organisations_utilities.json_schemas.get_organisation_activities_schema import \
    get_organisation_activities_schema
from src.be.utilities.organisations_utilities.request_payloads.create_organisation_activity_payloads import \
    create_organisation_activity_full_payload, create_organisation_activity_original_full_payload
from src.be.utilities.organisations_utilities.request_payloads.create_organisation_payloads import \
    create_organisation_required_payload
from src.be.utilities.useful_functions import validate_response_schema_and_fields, \
    validate_response_with_expected_json, get_random_uuid, standard_headers

base_url = get_config_value("base_url")
endpoint = "organisations/"
headers = standard_headers()

org_id = get_organisation_id(base_url, endpoint, create_organisation_required_payload(), headers)
activity_id = get_activity_id(base_url, endpoint, org_id, create_organisation_activity_full_payload(), headers)


def test_get_organisation_activity_by_id_successful_request():
    create_response = create_activity_request(base_url, endpoint, org_id, create_organisation_activity_full_payload(),
                                              headers)
    assert create_response.status_code == 200
    activity_id = create_response.json()['id']
    get_response = get_activity_request(base_url, endpoint, org_id, activity_id, headers)
    assert get_response.status_code == 200
    validate_response_schema_and_fields(get_response.json(), get_organisation_activities_schema)
    validate_response_with_expected_json(create_organisation_activity_required_props(), get_response.json(),
                                         create_response.json())
    validate_response_with_expected_json(create_organisation_activity_additional_props(), get_response.json(),
                                         create_response.json())


def test_get_organisation_activity_by_unauthorized():
    response = get_activity_request(base_url, endpoint, org_id, activity_id, None)
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"


def test_get_organisation_activity_by_nonexistent_id():
    response = get_activity_request(base_url, endpoint, activity_id, get_random_uuid(), headers)
    assert response.status_code == 404
    schema = error_schema
    validate(response.json(), schema=schema)
    response_fields = set(response.json().keys())
    schema_fields = set(schema.get("properties", {}).keys())
    assert response_fields == schema_fields, f"Response fields do not match schema. Expected: {schema_fields}, \
    Got: {response_fields}"


def test_get_organisation_activity_by_id_misspelled_endpoint():
    response = get_activity_request(base_url, "organisation/", org_id, activity_id, headers)
    assert response.status_code == 404
    schema = error_schema
    validate(response.json(), schema=schema)
    response_fields = set(response.json().keys())
    schema_fields = set(schema.get("properties", {}).keys())
    assert response_fields == schema_fields, f"Response fields do not match schema. Expected: {schema_fields}, \
    Got: {response_fields}"


def test_get_organisation_activity_original():
    create_response = create_original_activity_request(base_url,
                                                       create_organisation_activity_original_full_payload(org_id),
                                                       headers)
    assert create_response.status_code == 200
    get_response = get_original_activity_request(base_url, create_response.json()['id'], headers)
    assert get_response.status_code == 200
    validate_response_with_expected_json(create_organisation_activity_original_required_props(), get_response.json(),
                                         create_response.json())
    validate_response_with_expected_json(create_organisation_activity_additional_props(), get_response.json(),
                                         create_response.json())
