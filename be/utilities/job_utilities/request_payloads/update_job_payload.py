from src.be.utilities.get_core_api_data import *
from src.be.definitions.jobs_definitions import *

resp_user = get_user_id_from_core_api()
resp_team = get_team_id_from_core_api()
location_id = get_location_id_from_core_api()
org_id = get_organisation_id_from_core_api(location_id)
remit = get_random_remit()


def update_job_required_fields_payload():
    return {
        "organisation_id": org_id,
        "location_id": location_id,
        "title": get_random_qualification(),
        "type": random_job_type(),
        "agreement_type": random_job_agreement_type(),
        "source": random_job_source(),
        "location_remit": get_config_value("remit"),
        "job_posting_required": True,
        "exclusive": "yes",
        "responsible_user_id": resp_user,
        "responsible_team_id": resp_team,
        "short_id": random_string(6)
    }


def update_job_full_payload():
    add_contract_to_organisation(org_id)
    contract_id = get_contract_by_org_id(org_id).json()['results'][0]['id']
    payload = update_job_required_fields_payload()
    payload['preferred_start_date'] = get_today_date()
    payload['rate_currency'] = random_currency_rate()
    payload['rate_min_value'] = random.randint(1, 100)
    payload['rate_max_value'] = random.randint(200, 1000)
    payload['rate_period'] = random_rate_period()
    payload['contract_length_unit'] = random_contract_length_unit()
    payload['target_fee'] = random.randint(1, 12)
    payload['bonus_package'] = "bp_" + random_string(10)
    payload['status'] = random_status()
    payload['specification'] = "spec_" + random_string(10)
    payload['background_information'] = "bg_info_" + random_string(10)
    payload['background_information_updated_by'] = get_user_id_from_core_api()
    payload['tenure_category_id'] = get_random_uuid()
    payload['contract_id'] = contract_id
    payload['candidate_terminate_note'] = random_string(10)
    payload['client_terminate_note'] = random_string(10)
    payload['health_and_safety_note'] = random_string(30)
    payload['expenses_note'] = random_string(10)
    payload['experience_note'] = random_string(10)
    payload['function_or_cost_centre'] = random_string(10)
    payload['required_days_and_hours_note'] = random_string(10)
    payload['intervals'] = random_payment_interval()
    payload['margin_markup'] = random.randint(1, 10)
    payload['timesheet_unit'] = "daily"
    payload['cv_submission'] = "client_portal"
    payload['short_id'] = random_string(6)
    payload['required_days_and_hours_note'] = random_string(5)
    payload['payment_interval'] = "WEEKLY"
    payload['rpo'] = random_rpo()
    payload['other_consultant_ids'] = [get_random_uuid()]
    return payload




def wrong_job_type_payload():
    payload = update_job_required_fields_payload()
    payload['type'] = random_string(5)
    return payload


def wrong_agreement_type_payload():
    payload = update_job_required_fields_payload()
    payload['agreement_type'] = random_string(5)
    return payload


def wrong_job_source_payload():
    payload = update_job_required_fields_payload()
    payload['source'] = random_string(5)
    return payload
