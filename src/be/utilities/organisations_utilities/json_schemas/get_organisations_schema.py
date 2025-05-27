get_organisations_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "event_id": {
            "type": ["string", "null"]
        },
        "background_information": {
            "type": ["string", "null"]
        },
        "industry": {
            "type": ["string", "null"]
        },
        "is_employer_only": {
            "type": ["boolean", "null"]
        },
        "created_at": {
            "type": ["string"]
        },
        "last_updated_at": {
            "type": ["string"]
        },
        "created_by": {
            "type": ["string", "null"]
        },
        "last_contacted_at": {
            "type": ["string", "null"]
        },
        "industries": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": ["string", "null"]
                    },
                    "industry": {
                        "type": ["string", "null"]
                    }
                }
            }
        },
        "responsible_user_id": {
            "type": ["string", "null"]
        },
        "responsible_team_id": {
            "type": ["string", "null"]
        },
        "registration_number": {
            "type": ["string", "null"]
        },
        "tax_id": {
            "type": ["string", "null"]
        },
        "po_required": {
            "type": ["boolean", "null"]
        },
        "credit_status": {
            "type": "string"
        },
        "credit_expiry": {
            "type": ["string", "null"]
        },
        "credit_notes": {
            "type": ["string", "null"]
        },
        "organisation_traditional_name": {
            "type": ["string", "null"]
        },
        "background_information_updated_by": {
            "type": ["string", "null"]
        },
        "background_information_updated_at": {
            "type": ["string", "null"]
        }
    },
    "required": [
        "id",
        "credit_status",
        "created_at",
        "last_updated_at"
    ]
}
