from src.be.utilities.get_core_api_data import *

headers = {
    "Authorization": get_token()
}
base_url = get_config_value("base_url")


def update_client_required_fields_payload():
    return {
        "first_name": get_random_first_name(),
        "family_name": get_random_last_name()}


def update_client_full_payload():
    from src.be.definitions.clients_definitions import random_gender
    payload = update_client_required_fields_payload()
    payload['gender'] = random_gender()
    payload['gender_other'] = random_string(10)
    payload['preferred_name'] = "John Doe"
    payload['background_information'] = random_string(10)
    payload['background_information_updated_by'] = get_user_id_from_core_api()
    payload['background_information_updated_at'] = get_date_time_format()
    payload['responsible_user_id'] = get_user_id_from_core_api()
    payload['responsible_team_id'] = get_team_id_from_core_api()
    return payload


