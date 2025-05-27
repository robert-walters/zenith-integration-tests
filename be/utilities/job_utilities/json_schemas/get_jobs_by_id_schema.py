get_jobs_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "string", "format": "uuid"},
        "event_id": {"type": "string", "format": "uuid"},
        "last_updated_at": {"type": "string"},
        "created_at": {"type": "string"},
        "organisation_id": {"type": "string", "format": "uuid"},
        "location_id": {"type": "string", "format": "uuid"},
        "title": {"type": "string"},
        "preferred_start_date": {"type": "string", "format": "date"},
        "type": {"type": "string"},
        "rate_currency": {
            "type": ["string", "null"],
            "patternProperties": {
                "^[A-Z]{3}$": {"type": "string"}
            },
        },
        "rate_min_value": {"type": ["number"]},
        "rate_max_value": {"type": ["number"]},
        "rate_period": {"type": ["string", "null"]},
        "contract_length_unit": {"type": "string"},
        "contract_length_value": {"type": "number"},
        "target_fee": {"type": ["number"]},
        "bonus_package": {"type": "string"},
        "status": {
            "type": ["string"],
            "enum": ["live", "lead", "dummy", "closed_successfully", "closed_internally", "closed_by_competitor",
                     "cancelled", "on_hold", "completed_successfully", None]
        },
        "agreement_type": {"type": "string"},
        "specification": {"type": ["string", "null"]},
        "background_information": {"type": ["string", "null"]},
        "background_information_updated_at": {"type": "string", "format": "date-time"},
        "live_since": {"type": ["string", "null"]},
        "lead_since": {"type": ["string", "null"]},
        "last_activity": { "anyOf": [{ "type": "string", "format": "date" }, { "type": "null" }] },
        "source": {"type": "string"},
        "exclusive": {"type": "string"},
        "margin_markup": {"type": "number"},
        "job_posting_required": {"type": "boolean"},
        "rpo": {"type": ["string", "null"]},
        "timesheet_unit": {"type": ["string", "null"]},
        "cv_submission": {"type": "string"},
        "date_closed": { "anyOf": [{ "type": "string", "format": "date" }, { "type": "null" }] },
        "location_remit": {"type": "string"},
        "responsible_user_id": {"type": "string", "format": "uuid"},
        "responsible_team_id": {"type": "string", "format": "uuid"},
        "other_consultant_ids": {
            "type": "array",
            "items": {"type": "string", "format": "uuid"}
        },
        "created_by": {"type": "string", "format": "uuid"},
        "short_id": {"type": "string"},
        "last_contacted_at": {"type": ["string", "null"]},
        "broadbean_advert_references": {
            "type": "array",
            "items": {"type": "string"}
        },
        "function_or_cost_centre": {"type": ["string", "null"]},
        "required_days_and_hours_note": {"type": ["string", "null"]},
        "payment_interval": {"type": ["string", "null"]},
        "job_description": {"type": ["string", "null"]},
        "experience_note": {"type": ["string", "null"]},
        "expenses_note": {"type": ["string", "null"]},
        "health_and_safety_note": {"type": "string"},
        "client_terminate_note": {"type": "string"},
        "candidate_terminate_note": {"type": "string"},
        "contract_id": {"type": ["string", "null"]},
        "tenure_category_id": {"type": ["string", "null"]},
        "background_information_updated_by": {"type": "string"},
        "broadbean_advert_details": {
            "type": ["object", "null"],
            "properties": {
                "status": {
                    "type": "string",
                    "enum": ["Live", "Deleted", "Being_edited"]
                },
                "removal_time": {
                    "type": "string",
                    "format": "date-time"
                },
                "flags": {
                    "type": "object"
                },
                "documents": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "candidate_id": {
                                "type": "string"
                            },
                            "document_ids": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                }
                            }
                        },
                        "required": ["candidate_id", "document_ids"]
                    }
                },
                "candidates": {
                    "type": "object"
                },
                "advert_objects": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "values": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "reference": {
                                            "type": "string"
                                        },
                                        "removal_time": {
                                            "type": "string",
                                            "format": "date-time"
                                        }
                                    },
                                    "required": ["reference", "removal_time"]
                                }
                            },
                            "channels": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "string"
                                        },
                                        "status": {
                                            "type": "string",
                                            "enum": ["Live", "Deleted", "Being_edited"]
                                        },
                                        "removal_time": {
                                            "type": "string",
                                            "format": "date-time"
                                        }
                                    },
                                    "required": ["id", "status", "removal_time"]
                                }
                            }
                        },
                        "required": ["id", "values", "channels"]
                    }
                }
            },
            "required": ["status", "removal_time", "flags", "documents", "advert_objects"]
        }
    },
    "required": [
        "id",
        "event_id",
        "location_remit",
        "created_at",
        "last_updated_at"
    ]
}
