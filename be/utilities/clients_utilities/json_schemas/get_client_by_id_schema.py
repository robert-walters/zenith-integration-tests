get_clients_schema = {
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
        "candidate_id": {
            "type": ["string", "null"]
        },
        "first_name": {
            "type": "string"
        },
        "family_name": {
            "type": "string"
        },
        "event_id": {
            "type": "string"
        },
        "gender": {
            "type": ["string", "null"],
            "enum": ["male", "female", "non_binary", "transgender", "intersex", "other", "prefer_not_to_say", None]
        },
        "gender_other": {
            "type": ["string", "null"]
        },
        "preferred_name": {
            "type": ["string", "null"]
        },
        "background_information": {
            "type": ["string", "null"]
        },
        "background_information_updated_by": {
            "type": ["string", "null"]
        },
        "background_information_updated_at": {
            "type": ["string", "null"]
        },
        "created_by": {
            "type": ["string", "null"]
        },
        "last_contacted_at": {
            "type": ["string", "null"]
        },
        "responsible_user_id": {
            "type": ["string", "null"]
        },
        "responsible_team_id": {
            "type": ["string", "null"]
        }
    },
    "required": [
        "id",
        "event_id",
        "first_name",
        "family_name",
        "created_at",
        "last_updated_at"
    ]
}
