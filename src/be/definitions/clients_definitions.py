import random

import requests

from src.be.utilities.logger import add_log
from src.be.utilities.clients_utilities.request_payloads.create_client_payload import create_client_full_payload


def get_client_request(base_url, endpoint, params, headers):
    response = requests.get(base_url + endpoint + params, headers=headers)
    add_log(response)
    return response


def create_client_request(base_url, endpoint, payload, headers):
    response = requests.post(base_url + endpoint, json=payload, headers=headers)
    add_log(response)
    return response


def update_client_request(base_url, endpoint, client_id, payload, headers):
    response = requests.put(base_url + endpoint + client_id, json=payload, headers=headers)
    add_log(response)
    return response


def delete_client_request(base_url, endpoint, client_id, headers):
    response = requests.delete(base_url + endpoint + client_id, headers=headers)
    add_log(response)
    return response


def delete_clients_check_dependencies_request(base_url, endpoint, params, headers):
    response = requests.delete(base_url + endpoint + params + "?check-dependencies=true", headers=headers)
    add_log(response)
    return response


def delete_clients_ignore_dependencies_request(base_url, endpoint, params, headers):
    response = requests.delete(base_url + endpoint + params + "?check-dependencies=false", headers=headers)
    add_log(response)
    return response


def get_client_id(base_url, endpoint, headers):
    payload = create_client_full_payload()
    create_response = create_client_request(base_url, endpoint, payload, headers)
    assert create_response.status_code == 200, f"Response: {create_response.json()}"
    return create_response.json()['id']


def random_gender():
    genders = ["male", "female", "non_binary", "transgender", "intersex", "other", "prefer_not_to_say"]
    return random.choice(genders)


def create_client_required_props():
    return ["first_name", "family_name"]


def create_client_additional_props():
    return ["candidate_id", "gender", "preferred_name", "background_information", "background_information_updated_by",
            "background_information_updated_at", "responsible_user_id", "responsible_team_id", "created_by"]


def update_client_required_props():
    return ["first_name", "family_name"]


def update_client_additional_props():
    return ["gender", "gender_other", "preferred_name", "background_information", "background_information_updated_by",
            "background_information_updated_at", "responsible_user_id", "responsible_team_id"]
