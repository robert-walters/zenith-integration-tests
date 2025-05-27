from src.be.definitions.candidates_definitions import create_candidate_request, get_candidate_id
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_payloads import \
    create_candidate_required_fields_payload
from src.be.utilities.get_core_api_data import *

headers = {
    "Authorization": get_token()
}
base_url = get_config_value("base_url")


def create_client_required_fields_payload():
    return {
        "first_name": get_random_first_name(),
        "family_name": get_random_last_name()}


def create_client_full_payload():
    from src.be.definitions.clients_definitions import random_gender
    payload = create_client_required_fields_payload()
    payload['candidate_id'] = get_candidate_id()
    payload['gender'] = random_gender()
    payload['preferred_name'] = "John Doe"
    payload['background_information'] = random_string(10)
    payload['background_information_updated_by'] = get_user_id_from_core_api()
    payload['background_information_updated_at'] = get_date_time_format()
    payload['responsible_user_id'] = get_user_id_from_core_api()
    payload['responsible_team_id'] = get_team_id_from_core_api()
    payload['created_by'] = get_user_id_from_core_api()
    return payload

