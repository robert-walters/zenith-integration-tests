post_organisation_activity_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "created_at": {
            "type": ["string"]
        },
        "last_updated_at": {
            "type": ["string"]
        },
        "job_id": {
            "type": ["string", "null"]
        },
        "event_id": {
            "type": ["string", "null"]
        },
        "candidate_id": {
            "type": ["string", "null"]
        },
        "email_id": {
            "type": ["string", "null"]
        },
        "outcome": {
            "type": ["string", "null"]
        },
        "outcome_date": {
            "type": ["string", "null"]
        },
        "notes": {
            "type": ["string", "null"]
        },
        "type": {
            "type": "string"
        },
        "activity_group": {
            "type": "string"
        },
        "event_date": {
            "type": ["string", "null"]
        },
        "event_start_time": {
            "type": ["string", "null"]
        },
        "event_end_time": {
            "type": ["string", "null"]
        },
        "event_date_time": {
            "type": ["string", "null"]
        },
        "event_type": {
            "type": ["string", "null"]
        },
        "event_location": {
            "type": ["string", "null"]
        },
        "client_ids": {
            "type": "array",
            "items": [
                {
                    "type": ["string", "null"]
                }
            ]
        },
        "record_origin": {
            "type": "string"
        },
        "organisation_id": {
            "type": ["string", "null"]
        },
        "responsible_user_id": {
            "type": "string"
        },
        "other_consultant_ids": {
            "type": "array",
            "items": [
                {
                    "type": ["string", "null"]
                }
            ]
        },
        "responsible_team_id": {
            "type": "string"
        },
        "created_by": {
            "type": ["string", "null"]
        },
        "application_time": {
            "type": ["string", "null"]
        },
        "source": {
            "type": ["string", "null"]
        },
        "hidden": {
            "type": "boolean"
        }
    },
    "required": [
        "id",
        "type",
        "activity_group",
        "record_origin",
        "responsible_user_id",
        "responsible_team_id",
        "hidden",
        "created_at",
        "last_updated_at"]
}
