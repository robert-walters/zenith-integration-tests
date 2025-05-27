from src.be.definitions.activity_definitions import random_organisation_activity_type, random_activity_event_type, \
    random_activity_source, random_job_activity_placement_type, random_activity_outcome
from src.be.utilities.get_core_api_data import *

resp_user = get_user_id_from_core_api()
resp_team = get_team_id_from_core_api()
client_id = get_client_id_from_core_api()


def update_organisation_activity_required_payload():
    return {"type": random_organisation_activity_type(),
            "responsible_user_id": get_user_id_from_core_api(),
            "responsible_team_id": get_team_id_from_core_api(),
            "hidden": True,
            "client_ids": [client_id]
            }


def update_organisation_activity_full_payload():
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
        "placement_start_date": get_date_time_format(),
        "placement_end_date": get_date_time_format(),
        "placement_type": random_job_activity_placement_type(),
        "hidden": False,
        "client_ids": [client_id],

    }


def update_organisation_activity_original_mandatory_payload(org_id):
    return {"type": random_organisation_activity_type(),
            "responsible_user_id": get_user_id_from_core_api(),
            "responsible_team_id": get_team_id_from_core_api(),
            "client_ids": [client_id],
            "hidden": True,
            "organisation_id": org_id
            }


def update_organisation_activity_original_full_payload(org_id):
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
        "placement_start_date": get_date_time_format(),
        "placement_end_date": get_date_time_format(),
        "placement_type": random_job_activity_placement_type(),
        "client_ids": [client_id],
        "hidden": False,
        "organisation_id": org_id
    }
