from src.be.definitions.activity_definitions import random_activity_source, random_job_activity_type, \
    random_activity_event_type, random_job_activity_placement_type, random_activity_outcome
from src.be.utilities.get_core_api_data import get_user_id_from_core_api, get_team_id_from_core_api, \
    get_email_id_core_api, get_fee_id_from_core_api
from src.be.utilities.useful_functions import random_string, get_date_time_format, get_today_date


def create_job_activity_required_fields_payload():
    return {
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "type": random_job_activity_type()
    }


def create_job_activity_full_payload():
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
        "type": random_job_activity_type(),
        "fee_id": get_fee_id_from_core_api(),
        "placement_start_date": get_date_time_format(),
        "placement_end_date": get_date_time_format(),
        "placement_type": random_job_activity_placement_type(),
        "bb_boards": [random_string(10)],
        "created_by": get_user_id_from_core_api(),
        "hidden": False
    }


def create_job_activity_original_mandatory_payload(job_id):
    return {
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "type": random_job_activity_type(),
        "record_origin": "job",
        "job_id": job_id
    }


def create_job_activity_original_full_payload(job_id):
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
        "type": random_job_activity_type(),
        "fee_id": get_fee_id_from_core_api(),
        "placement_start_date": get_date_time_format(),
        "placement_end_date": get_date_time_format(),
        "placement_type": random_job_activity_placement_type(),
        "bb_boards": [random_string(10)],
        "created_by": get_user_id_from_core_api(),
        "hidden": False,
        "record_origin": "job",
        "job_id": job_id
    }
