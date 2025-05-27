from src.be.definitions.activity_definitions import *
from src.be.utilities.clients_utilities.request_payloads.create_client_activity_payload import \
    create_client_activity_required_payload
from src.be.utilities.get_core_api_data import *

resp_user = get_user_id_from_core_api()
resp_team = get_team_id_from_core_api()


def update_client_activity_required_payload():
    return {
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "type": random_client_activity_type(),
        "hidden": True,
        "automated": False
    }


def update_client_activity_full_payload():
    return {
        "email_id": get_email_id_core_api(),
        "outcome": random_activity_outcome(),
        "outcome_date": get_today_date(),
        "notes": random_string(10),
        "event_date": get_today_date(),
        "event_start_time": "00:00:00",
        "event_end_time": "00:00:00",
        "event_date_time": get_date_time_format(),
        "event_type": random_activity_event_type(),
        "event_location": "Online",
        "responsible_user_id": get_user_id_from_core_api(),
        "other_consultant_ids": [
            get_user_id_from_core_api()
        ],
        "responsible_team_id": get_team_id_from_core_api(),
        "application_time": get_date_time_format(),
        "source": random_activity_source(),
        "meeting_title": "title" + random_string(10),
        "reminder_minutes": 15,
        "is_teams_meeting": False,
        "attachment_ids": None,
        "message": "message" + random_string(30),
        "automated": True,
        "module": "meetings",
        "hidden": False,
        "type": random_client_activity_type(),
        "created_by": get_user_id_from_core_api()
    }


def update_client_activity_original_required_payload(client_id):
    return {
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "type": random_client_activity_type(),
        "hidden": True,
        "automated": False,
        "client_id": client_id
    }


def update_client_activity_original_full_payload(client_id):
    return {
        "email_id": get_email_id_core_api(),
        "outcome": random_activity_outcome(),
        "outcome_date": get_today_date(),
        "notes": random_string(10),
        "event_date": get_today_date(),
        "event_start_time": "00:00:00",
        "event_end_time": "00:00:00",
        "event_date_time": get_date_time_format(),
        "event_type": random_activity_event_type(),
        "event_location": "Online",
        "responsible_user_id": get_user_id_from_core_api(),
        "other_consultant_ids": [
            get_user_id_from_core_api()
        ],
        "responsible_team_id": get_team_id_from_core_api(),
        "application_time": get_date_time_format(),
        "source": random_activity_source(),
        "meeting_title": "title" + random_string(10),
        "reminder_minutes": 15,
        "is_teams_meeting": False,
        "attachment_ids": None,
        "message": "message" + random_string(30),
        "automated": True,
        "module": "meetings",
        "hidden": False,
        "type": random_client_activity_type(),
        "created_by": get_user_id_from_core_api(),
        "client_id": client_id
    }
