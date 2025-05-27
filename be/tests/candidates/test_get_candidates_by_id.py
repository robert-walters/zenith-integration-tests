from jsonschema import validate

from src.be.configuration.config_parser import get_config_value
from src.be.utilities.error_schema import error_schema
from src.be.utilities.candidates_utilities.json_schemas.get_candidate_by_id_schema import get_candidate_by_id_schema
from src.be.definitions.candidates_definitions import get_candidate_id, get_candidates_by_id
from src.be.utilities.useful_functions import get_random_uuid, standard_headers, validate_response_schema_and_fields

base_url = get_config_value("base_url")
endpoint = "candidates/"
headers = standard_headers()
candidate_id = get_candidate_id()


def test_get_candidate_by_id_successful_request():
    response = get_candidates_by_id(base_url, endpoint, candidate_id, headers)
    assert response.status_code == 200


def test_get_candidate_by_id_unauthorized():
    response = get_candidates_by_id(base_url, endpoint, candidate_id, "")
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"


def test_get_candidate_by_id_nonexistent_id():
    response = get_candidates_by_id(base_url, endpoint, get_random_uuid(), headers)
    assert response.status_code == 404
    validate_response_schema_and_fields(response.json(), error_schema)


def test_get_candidate_by_id_json_schema():
    response = get_candidates_by_id(base_url, endpoint, candidate_id, headers)
    validate_response_schema_and_fields(response.json(), get_candidate_by_id_schema)


def test_get_candidate_by_id_misspelled_endpoint():
    response = get_candidates_by_id(base_url, "wrong" + endpoint, candidate_id, headers)
    assert response.status_code == 404
    validate_response_schema_and_fields(response.json(), error_schema)


def test_get_candidate_by_id_wrong_format():
    response = get_candidates_by_id(base_url, endpoint, "%test", headers)
    assert response.status_code == 400
    validate_response_schema_and_fields(response.json(), error_schema)
