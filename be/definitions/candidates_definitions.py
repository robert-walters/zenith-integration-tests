import requests

from src.be.configuration.config_parser import get_config_value
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_payloads import \
    create_candidate_full_payload
from src.be.utilities.logger import add_log
from src.be.utilities.useful_functions import get_headers


def create_candidate_request(base_url, endpoint, payload, headers):
    response = requests.post(base_url + endpoint, json=payload, headers=headers)
    add_log(response)
    return response


def get_candidates_by_id(base_url, endpoint, params, headers):
    response = requests.get(base_url + endpoint + params, headers=headers)
    add_log(response)
    return response


def delete_candidates_ignore_dependencies_request(base_url, endpoint, params, headers):
    response = requests.delete(base_url + endpoint + params + "?check-dependencies=false", headers=headers)
    add_log(response)
    return response


def delete_candidates_check_dependencies_request(base_url, endpoint, params, headers):
    response = requests.delete(base_url + endpoint + params + "?check-dependencies=true", headers=headers)
    add_log(response)
    return response


def update_candidates(base_url, endpoint, params, payload, headers):
    response = requests.put(base_url + endpoint + params, json=payload, headers=headers)
    add_log(response)
    return response


def get_candidate_id():
    headers = get_headers()

    create_candidate_response = create_candidate_request(get_config_value("base_url"), "candidates/",
                                                         create_candidate_full_payload(), headers)
    assert create_candidate_response.status_code == 200, f"{create_candidate_response.status_code}"
    return create_candidate_response.json()['id']


def candidate_national_info_properties():
    return ["cv_link", "desired_locations", "desired_organisations", "desired_salary_currency",
            "desired_salary_period", "desired_salary_value", "visa_expiry", "visa_type", "preferred_name",
            "preferred_name", "preferred_pronoun", "address_line_1", "address_line_2", "address_line_3",
            "city", "province", "postcode", "country_of_residence", "national_information", "location_remit",
            "client_id", "responsible_user_id", "responsible_team_id", "created_by", "desired_positions",
            "position_type", "rate_currency", "rate_period", "rate_value", "package_breakdown",
            "availability_date", "availability_duration_unit", "availability_duration_value", "total_package",
            "salary_last_updated_at", "identity_reference", "traditional_first_name",
            "traditional_family_name", "passport_number", "hk_number_id", "company_name", "original_source",
            "original_source_recorded_at"]


def candidate_core_info_properties():
    return ["has_meaningful_events", "first_name", "family_name", "skills", "language", "situation_status",
            "gender", "gender_other", "nationality", "industry", "background_information",
            "background_information_updated_by", "background_information_updated_at", "traits_skills",
            "people_skills", "language_skills", "work_education_description", "salary_availability_description",
            "desired_jobs_description"]


def verify_national_candidate_data_in_core_api(post_json, get_core_json):
    national_info = candidate_national_info_properties()
    for prop in national_info:
        assert post_json[prop] == get_core_json[
            prop], f"Expect {prop} - {post_json[prop]} to equals {get_core_json[prop]}"
    assert post_json['responsible_user_id'] == get_core_json[
        'created_by'], f"Expect created_by {post_json['responsible_user_id']} to equals {get_core_json['created_by']}"
    assert "last_contacted_at" in get_core_json
    assert "last_contacted_at" in post_json
    assert "desired_position_type" in get_core_json
    assert "desired_position_type" not in post_json


def verify_core_candidate_data_in_core_api(post_json, get_core_json):
    core_info = candidate_core_info_properties()
    for core_prop in core_info:
        assert post_json[core_prop] == get_core_json['core_candidate'][
            core_prop], f"Expect {core_prop} - {post_json[core_prop]} to equals  {get_core_json['core_candidate'][core_prop]}"
    assert get_core_json['core_candidate']['last_updated_by'] == post_json[
        'last_updated_by'], f"Expect created_by {get_core_json['core_candidate']['last_updated_by']} to equals {post_json['last_updated_by']}"


def validate_the_post_response(payload, post_json):
    national_info = candidate_national_info_properties()
    core_info = candidate_core_info_properties()
    for prop in national_info:
        assert payload[prop] == post_json[prop], f"Expect {prop} - {payload[prop]} to equal {post_json[prop]}"
    for prop in core_info:
        assert payload[prop] == post_json[prop], f"Expect {prop} - {payload[prop]} to equal {post_json[prop]}"
