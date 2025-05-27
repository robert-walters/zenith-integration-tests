import random

import requests

from src.be.utilities.logger import add_log


def get_organisations_request(base_url, endpoint, params, headers):
    response = requests.get(base_url + endpoint + params, headers=headers)
    add_log(response)
    return response


def create_organisations_request(base_url, endpoint, payload, headers):
    response = requests.post(base_url + endpoint, json=payload, headers=headers)
    add_log(response)
    return response


def update_organisations_request(base_url, endpoint, org_id, payload, headers):
    response = requests.put(base_url + endpoint + org_id, json=payload, headers=headers)
    add_log(response)
    return response


def delete_organisations_request(base_url, endpoint, org_id, headers):
    response = requests.delete(base_url + endpoint + org_id, headers=headers)
    add_log(response)
    return response


def delete_organisations_check_dependencies_request(base_url, endpoint, params, headers):
    response = requests.delete(base_url + endpoint + params + "?check-dependencies=true", headers=headers)
    add_log(response)
    return response


def delete_organisations_ignore_dependencies_request(base_url, endpoint, params, headers):
    response = requests.delete(base_url + endpoint + params + "?check-dependencies=false", headers=headers)
    add_log(response)
    return response


def get_organisation_id(base_url, endpoint, payload, headers):
    create_response = create_organisations_request(base_url, endpoint, payload, headers)
    assert create_response.status_code == 200, f"Response: {create_response.status_code}"
    return create_response.json()['id']


def random_credit_status():
    statuses = ["approved", "not_approved", "rejected", "expired"]
    return random.choice(statuses)


def random_industries():
    industries = ["Financial Services", "Insurance", "Healthcare & Life sciences", "Retail", "Industrial" "Automotive"]
    return random.choice(industries)


def create_organisation_required_props():
    return ["name", "responsible_user_id", "responsible_team_id"]


def create_organisation_additional_props():
    return ["background_information", "industry", "industries", "registration_number", "tax_id", "credit_expiry",
            "credit_notes", "organisation_traditional_name", "background_information_updated_by",
            "background_information_updated_at", "created_by"]


def update_organisation_required_props():
    return ["name", "credit_status", "po_required", "is_employer_only", "responsible_user_id", "responsible_team_id"]


def update_organisation_additional_props():
    return ["background_information", "industry", "industries", "registration_number", "tax_id", "credit_expiry",
            "credit_notes", "organisation_traditional_name", "background_information_updated_by",
            "background_information_updated_at"]
