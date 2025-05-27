import pytest
from src.be.definitions.organisations_definitions import create_organisations_request, \
    create_organisation_required_props, create_organisation_additional_props, get_organisations_request
from src.be.utilities.organisations_utilities.request_payloads.create_organisation_payloads import *
from src.be.utilities.error_schema import error_schema
from src.be.utilities.organisations_utilities.json_schemas.post_organisations_schema import post_organisation_schema, \
    post_organisation_employer_only_schema

base_url = get_config_value("base_url")
endpoint = "organisations/"
headers = standard_headers()


def test_create_organisations_mandatory_payload():
    response = create_organisations_request(base_url, endpoint, create_organisation_required_payload(), headers)
    assert response.status_code == 200
    validate(response.json(), schema=post_organisation_schema)
    validate_response_with_expected_json(create_organisation_required_props(), response.json(),
                                         get_request_body_json(response))
    validate_response_schema_and_fields(response.json(), post_organisation_schema)


def test_create_organisations_full_payload():
    response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), headers)
    assert response.status_code == 200
    validate(response.json(), schema=post_organisation_schema)
    org_id = response.json()['id']
    get_response = get_organisations_request(base_url, endpoint, org_id, headers)
    assert get_response.status_code == 200
    validate_response_with_expected_json(create_organisation_additional_props(), response.json(), get_response.json())
    validate_response_schema_and_fields(get_response.json(), post_organisation_schema)


def test_create_organisations_employer_only_full_payload():
    response = create_organisations_request(base_url, endpoint, create_organisation_employer_only_full_payload(),
                                            headers)
    assert response.status_code == 200
    validate(response.json(), schema=post_organisation_employer_only_schema)
    org_id = response.json()['id']
    get_response = get_organisations_request(base_url, endpoint, org_id, headers)
    assert get_response.status_code == 200
    assert response.json()['name'] == get_response.json()['name']
    assert response.json()['is_employer_only'] == get_response.json()['is_employer_only']
    validate_response_schema_and_fields(get_response.json(), post_organisation_employer_only_schema)


def test_create_organisations_employer_only_mandatory_payload():
    response = create_organisations_request(base_url, endpoint, create_organisation_employer_only_required_payload(),
                                            headers)
    assert response.status_code == 200
    validate_response_schema_and_fields(response.json(), post_organisation_employer_only_schema)


def test_create_organisations_with_more_than_five_industries():
    response = create_organisations_request(base_url, endpoint, create_organisation_more_than_five_industries(),
                                            headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_organisations_with_duplicate_industries():
    response = create_organisations_request(base_url, endpoint, create_organisation_more_than_five_industries(),
                                            headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_organisations_wrong_data_type():
    payload = create_organisation_full_payload()
    payload['industry'] = 123456
    response = create_organisations_request(base_url, endpoint, payload, headers)
    validate_response_schema_and_fields(response.json(), error_schema)


def test_create_organisations_nonexistent_property_in_payload():
    payload = create_organisation_full_payload()
    payload["my_property"] = random_string(10)
    response = create_organisations_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200
    validate(response.json(), schema=post_organisation_schema)
    assert "my_property" not in response.json()
    validate_response_schema_and_fields(response.json(), post_organisation_schema)


@pytest.mark.parametrize("missing_property", ["name", "responsible_user_id", "responsible_team_id"])
def test_create_organisations_missing_required_payload(missing_property):
    payload = create_organisation_full_payload()
    payload.pop(missing_property)
    response = create_organisations_request(base_url, endpoint, payload, headers)
    assert response.status_code == 400


def test_create_organisations_empty_payload():
    response = create_organisations_request(base_url, endpoint, None, headers)
    assert response.status_code == 400


def test_create_organisations_unauthorized():
    response = create_organisations_request(base_url, endpoint, create_organisation_full_payload(), None)
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"


@pytest.mark.parametrize("required_property", create_organisation_required_payload())
def test_create_organisation_required_property_set_to_null(required_property):
    payload = create_organisation_required_payload()
    payload[required_property] = None
    response = create_organisations_request(base_url, endpoint, payload, headers)
    if required_property == "is_employer_only":
        assert response.status_code == 200
    else:
        assert response.status_code == 400
