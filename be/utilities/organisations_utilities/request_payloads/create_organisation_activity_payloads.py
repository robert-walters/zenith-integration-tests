from src.be.definitions.activity_definitions import random_activity_source, random_activity_event_type, \
    random_activity_outcome, random_organisation_activity_type
from src.be.utilities.get_core_api_data import get_user_id_from_core_api, get_team_id_from_core_api, \
    get_email_id_core_api, get_client_id_from_core_api
from src.be.utilities.useful_functions import get_date_time_format, random_string, get_today_date

resp_user = get_user_id_from_core_api()
resp_team = get_team_id_from_core_api()
client_id = get_client_id_from_core_api()


def create_organisation_activity_required_payload():
    return {"type": random_organisation_activity_type(),
            "responsible_user_id": get_user_id_from_core_api(),
            "responsible_team_id": get_team_id_from_core_api(),
            "client_ids": [client_id]
            }


def create_organisation_activity_full_payload():
    return {
        "email_id": get_email_id_core_api(),
        "outcome": random_activity_outcome(),
        "outcome_date": get_today_date(),
        "notes": random_string(20),
        "event_date": get_today_date(),
        "event_start_time": "00:00:00",
        "event_end_time": "00:00:00",
        "event_date_time": get_date_time_format(),
        "event_type": random_activity_event_type(),
        "event_location": "Online",
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "application_time": get_date_time_format(),
        "source": random_activity_source(),
        "type": random_organisation_activity_type(),
        "created_by": get_user_id_from_core_api(),
        "client_ids": [client_id],
        "hidden": False
    }


def create_organisation_activity_original_mandatory_payload(org_id):
    return {"type": random_organisation_activity_type(),
            "responsible_user_id": get_user_id_from_core_api(),
            "responsible_team_id": get_team_id_from_core_api(),
            "client_ids": [client_id],
            "organisation_id": org_id,
            "record_origin": "organisation"
            }


def create_organisation_activity_original_full_payload(org_id):
    return {
        "email_id": get_email_id_core_api(),
        "outcome": random_activity_outcome(),
        "outcome_date": get_today_date(),
        "notes": random_string(20),
        "event_date": get_today_date(),
        "event_start_time": "00:00:00",
        "event_end_time": "00:00:00",
        "event_date_time": get_date_time_format(),
        "event_type": random_activity_event_type(),
        "event_location": "Online",
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "application_time": get_date_time_format(),
        "source": random_activity_source(),
        "type": random_organisation_activity_type(),
        "created_by": get_user_id_from_core_api(),
        "hidden": False,
        "client_ids": [client_id],
        "organisation_id": org_id,
        "record_origin": "organisation"
    }
