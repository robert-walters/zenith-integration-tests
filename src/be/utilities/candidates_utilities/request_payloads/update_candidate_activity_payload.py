from src.be.definitions.activity_definitions import *
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_activity_payload import \
    create_candidate_activity_required_payload
from src.be.utilities.get_core_api_data import *

resp_user = get_user_id_from_core_api()
resp_team = get_team_id_from_core_api()


def update_candidate_activity_required_payload():
    return {
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "automated": True,
        "hidden": False,
        "type": random_candidate_activity_type()
    }


def update_candidate_activity_full_payload():
    return {
        "email_id": get_email_id_core_api(),
        "outcome": random_activity_outcome(),
        "outcome_date": get_today_date(),
        "notes": random_string(10),
        "event_date": get_today_date(),
        "event_start_time": "00:00",
        "event_end_time": "00:00",
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
        "organisation_id": get_organisation_id_from_core_api(get_location_id_from_core_api()),
        "job_id": get_job_id_from_core_api(),
        "client_ids": [
            get_client_id_from_core_api()
        ],
        "type": random_candidate_activity_type(),
        "created_by": get_user_id_from_core_api()
    }


def missing_required_property_payload(prop):
    payload = create_candidate_activity_required_payload()
    payload.pop(prop)
    return payload


def update_candidate_activity_original_mandatory_payload(candidate_id):
    payload = update_candidate_activity_required_payload()
    payload["candidate_id"] = candidate_id
    return payload


def update_candidate_activity_original_full_payload(candidate_id):
    payload = update_candidate_activity_full_payload()
    payload["candidate_id"] = candidate_id
    return payload
