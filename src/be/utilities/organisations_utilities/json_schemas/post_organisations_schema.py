post_organisation_schema = {
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
            "type": "boolean"
        },
        "created_at": {
            "type": "string"
        },
        "last_updated_at": {
            "type": "string"
        },
        "created_by": {
            "type": ["string", "null"]
        },
        "industries": {
            "type": ["array", "null"],
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
            "type": "boolean"
        },
        "credit_status": {
            "type": "string",
            "enum": ["approved", "not_approved", "rejected", "expired"]
        },
        "credit_expiry": {
            "type": ["string", "null"]
        },
        "last_contacted_at": {
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
        "name",
        "credit_status",
        "po_required",
        "is_employer_only",
        "created_at",
        "last_updated_at"
    ]
}

post_organisation_employer_only_schema = {
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
            "type": "string"
        },
        "is_employer_only": {
            "type": "boolean",
            "enum": [True]
        },
        "created_at": {
            "type": "string"
        },
        "last_updated_at": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "name",
        "is_employer_only",
        "created_at",
        "last_updated_at"
    ]
}
