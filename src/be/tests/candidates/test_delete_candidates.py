from src.be.configuration.config_parser import get_config_value
from src.be.utilities.get_core_api_data import get_candidates_by_id_from_core_api, get_contacts_for_candidate, \
    add_contact_to_candidate, add_alert_to_candidate, get_alerts_for_candidate, add_suitability_industry_to_candidate, \
    add_suitability_language_to_candidate, add_qualification_to_candidate, add_review_to_candidate, \
    add_interview_notes_to_candidate, add_activity_to_candidate
from src.be.definitions.candidates_definitions import get_candidate_id, delete_candidates_ignore_dependencies_request, \
    get_candidates_by_id, delete_candidates_check_dependencies_request
from src.be.utilities.useful_functions import get_random_uuid, standard_headers, delete_headers

base_url = get_config_value("base_url")
endpoint = "candidates/"
headers = standard_headers()
delete_headers = delete_headers()


def test_delete_candidate_without_dependencies():
    candidate_id = get_candidate_id()
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403
    get_response = get_candidates_by_id(base_url, endpoint, candidate_id, headers)
    assert get_response.status_code == 200
    get_core_response = get_candidates_by_id_from_core_api(candidate_id)
    assert get_core_response.status_code == 200


def test_delete_candidate_with_activities_checking_dependencies():
    candidate_id = get_candidate_id()
    add_activity_to_candidate(candidate_id)
    response = delete_candidates_check_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403


def test_delete_candidate_with_contacts_checking_dependencies():
    candidate_id = get_candidate_id()
    add_contact_to_candidate(candidate_id)
    response = delete_candidates_check_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403
    candidate_contacts = get_contacts_for_candidate(candidate_id)
    assert candidate_contacts.json()['metadata']['total'] == 1


def test_delete_candidate_with_alerts_checking_dependencies():
    candidate_id = get_candidate_id()
    add_alert_to_candidate(candidate_id)
    response = delete_candidates_check_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403
    candidate_alerts = get_alerts_for_candidate(candidate_id)
    assert candidate_alerts.json()['metadata']['total'] == 1


def test_delete_candidate_with_suitability_industries_checking_dependencies():
    candidate_id = get_candidate_id()
    add_suitability_industry_to_candidate(candidate_id)
    response = delete_candidates_check_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403


def test_delete_candidate_with_suitability_language_checking_dependencies():
    candidate_id = get_candidate_id()
    add_suitability_language_to_candidate(candidate_id)
    response = delete_candidates_check_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403


def test_delete_candidate_with_qualification_checking_dependencies():
    candidate_id = get_candidate_id()
    add_qualification_to_candidate(candidate_id)
    response = delete_candidates_check_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403


def test_delete_candidate_with_reviews_checking_dependencies():
    candidate_id = get_candidate_id()
    add_review_to_candidate(candidate_id)
    response = delete_candidates_check_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403


def test_delete_candidate_with_interview_notes_checking_dependencies():
    candidate_id = get_candidate_id()
    add_interview_notes_to_candidate(candidate_id)
    response = delete_candidates_check_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403


def test_delete_candidate_with_interview_notes_ignore_dependencies():
    candidate_id = get_candidate_id()
    add_interview_notes_to_candidate(candidate_id)
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403


def test_delete_candidate_with_reviews_ignore_dependencies():
    candidate_id = get_candidate_id()
    add_review_to_candidate(candidate_id)
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403


def test_delete_candidate_with_qualification_ignore_dependencies():
    candidate_id = get_candidate_id()
    add_qualification_to_candidate(candidate_id)
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403


def test_delete_candidate_with_suitability_language_ignore_dependencies():
    candidate_id = get_candidate_id()
    add_suitability_language_to_candidate(candidate_id)
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403
    get_response = get_candidates_by_id(base_url, endpoint, candidate_id, headers)
    assert get_response.status_code == 200
    get_core_response = get_candidates_by_id_from_core_api(candidate_id)
    assert get_core_response.status_code == 200


def test_delete_candidate_with_activities_ignore_dependencies():
    candidate_id = get_candidate_id()
    add_activity_to_candidate(candidate_id)
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403
    get_response = get_candidates_by_id(base_url, endpoint, candidate_id, headers)
    assert get_response.status_code == 200
    get_core_response = get_candidates_by_id_from_core_api(candidate_id)
    assert get_core_response.status_code == 200


def test_delete_candidate_with_contacts_ignore_dependencies():
    candidate_id = get_candidate_id()
    add_contact_to_candidate(candidate_id)
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403
    get_response = get_candidates_by_id(base_url, endpoint, candidate_id, headers)
    assert get_response.status_code == 200
    get_core_response = get_candidates_by_id_from_core_api(candidate_id)
    assert get_core_response.status_code == 200
    candidate_contacts = get_contacts_for_candidate(candidate_id)
    assert candidate_contacts.json()['metadata']['total'] == 1


def test_delete_candidate_with_alerts_ignore_dependencies():
    candidate_id = get_candidate_id()
    add_alert_to_candidate(candidate_id)
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403
    get_response = get_candidates_by_id(base_url, endpoint, candidate_id, headers)
    assert get_response.status_code == 200
    get_core_response = get_candidates_by_id_from_core_api(candidate_id)
    assert get_core_response.status_code == 200
    candidate_alerts = get_alerts_for_candidate(candidate_id)
    assert candidate_alerts.json()['metadata']['total'] == 1


def test_delete_candidate_without_auth():
    candidate_id = get_candidate_id()
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, "")
    assert response.status_code in (401, 403), f"Expected 401 or 403, but got {response.status_code}"
    get_response = get_candidates_by_id(base_url, endpoint, candidate_id, headers)
    assert get_response.status_code == 200
    get_core_response = get_candidates_by_id_from_core_api(candidate_id)
    assert get_core_response.status_code == 200


def test_delete_candidate_wrong_candidate_id():
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, get_random_uuid(), delete_headers)
    assert response.status_code == 403


def test_delete_candidate_already_deleted():
    candidate_id = get_candidate_id()
    response = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response.status_code == 403
    response2 = delete_candidates_ignore_dependencies_request(base_url, endpoint, candidate_id, delete_headers)
    assert response2.status_code == 403
