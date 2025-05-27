post_jobs_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "event_id": {
            "type": "string"
        },
        "last_updated_at": {
            "type": "string"
        },
        "created_at": {
            "type": "string"
        },
        "organisation_id": {
            "type": ["string", "null"]
        },
        "location_id": {
            "type": ["string", "null"]
        },
        "title": {
            "type": ["string", "null"]
        },
        "preferred_start_date": {
            "type": ["string", "null"]
        },
        "type": {
            "type": ["string", "null"]
        },
        "rate_currency": {
            "type": ["string", "null"],
            "enum": [
                None, "AUD", "BHD", "BRL", "CAD", "CLP", "CNY", "GBP", "HKD", "IDR", "JPY",
                "KRW", "KWD", "MYR", "MXN", "NZD", "PHP", "QAR", "SAR", "SGD", "ZAR",
                "CHF", "TWD", "THB", "AED", "VND", "EGP", "INR", "JOD", "PKR", "OMR",
                "IRR", "IQD", "ILS", "TRY", "SYP", "YER", "AFN", "EUR", "ALL", "DZD",
                "USD", "AOA", "XCD", "ARS", "AMD", "AWG", "AZN", "BSD", "BDT", "BBD",
                "BZD", "XOF", "BMD", "BTN", "BOB", "BAM", "BWP", "NOK", "BND", "BGN",
                "BIF", "CVE", "KHR", "XAF", "KYD", "COP", "KMF", "CRC", "HRK", "CUP",
                "ANG", "CYP", "CZK", "CDF", "DKK", "DJF", "DOP", "ERN", "EEK", "SZL",
                "ETB", "FKP", "FJD", "XPF", "GMD", "GEL", "GHC", "GIP", "GTQ", "GGP",
                "GNF", "GYD", "HTG", "HNL", "HUF", "ISK", "IMP", "JMD", "JEP", "KZT",
                "KES", "KGS", "LAK", "LVL", "LBP", "LSL", "LRD", "LYD", "LTL", "MOP",
                "MGF", "MWK", "MVR", "MTL", "MRO", "MUR", "MDL", "MNT", "MAD", "MZM",
                "MMK", "NAD", "NPR", "NIO", "NGN", "KPW", "MKD", "PAB", "PGK", "PYG",
                "PEN", "PLN", "RON", "RUB", "RWF", "WST", "STD", "CSD", "SCR", "SLL",
                "SKK", "SIT", "SBD", "SOS", "SSP", "LKR", "SDD", "SRD", "SEK", "TJS",
                "TZS", "TOP", "TTD", "TND", "TMT", "UGX", "UAH", "UYU", "UZS", "VUV",
                "VEB", "ZMK", "ZWD", "AAD", "RMB", "BYN"
            ]
        },
        "rate_min_value": {
            "type": ["integer", "string", "null"]
        },
        "rate_max_value": {
            "type": ["integer", "string", "null"]
        },
        "rate_period": {
            "type": ["string", "null"]
        },
        "contract_length_unit": {
            "type": ["string", "null"]
        },
        "contract_length_value": {
            "type": ["integer", "string", "null"]
        },
        "target_fee": {
            "type": ["integer", "string", "null"]
        },
        "bonus_package": {
            "type": ["string", "null"]
        },
        "status": {
            "type": ["string", "null"],
            "enum": [
                None, "live", "lead", "dummy", "closed_successfully", "closed_internally", "closed_by_competitor",
                "cancelled", "on_hold", "completed_successfully"
            ]
        },
        "agreement_type": {
            "type": ["string", "null"],
            "enum": [None, "mapping", "contingent", "agreement_tbc", "exclusive", "non_exclusive",
                     "exclusive_no_placement_no_fee", "no_placement_no_fee", "retainer", "retainer_shortlist"]
        },
        "specification": {
            "type": ["string", "null"]
        },
        "background_information": {
            "type": ["string", "null"]
        },
        "background_information_updated_at": {
            "type": ["string", "null"]
        },
        "live_since": {
            "type": ["string", "null"]
        },
        "lead_since": {
            "type": ["string", "null"]
        },
        "last_activity": {
            "type": ["string", "null"]
        },
        "source": {
            "type": ["string", "null"],
            "enum": [None, "bd_call", "client_meeting", "ad_chase", "lead_from_colleague", "lead_from_candidate", "rpo", "psa", "inbound_call_from_client", "marketing_lead", "rw_client_development_director"]
        },
        "exclusive": {
            "type": ["string", "null"],
            "enum": ["yes", "no", "tbc"]
        },
        "margin_markup": {
            "type": ["integer", "string", "null"]
        },
        "job_posting_required": {
            "type": "boolean"
        },
        "rpo": {
            "type": ["string", "null"]
        },
        "timesheet_unit": {
            "type": ["string", "null"]
        },
        "cv_submission": {
            "type": ["string", "null"]
        },
        "date_closed": {
            "type": ["string", "null"]
        },
        "location_remit": {
            "type": ["string", "null"]
        },
        "responsible_user_id": {
            "type": ["string", "null"]
        },
        "responsible_team_id": {
            "type": ["string", "null"]
        },
        "other_consultant_ids": {
            "type": ["array", "null"],
            "items": [
                {
                    "type": "string"
                }
            ]
        },
        "created_by": {
            "type": ["string", "null"]
        },
        "short_id": {
            "type": "string"
        },
        "last_contacted_at": {
            "type": ["string", "null"]
        },
        "broadbean_advert_details": {
            "type": ["object", "null"],
            "properties": {
                "flags": {
                    "type": "object",
                    "properties": {
                        "red": {
                            "type": ["integer", "string"]
                        },
                        "none": {
                            "type": ["integer", "string"]
                        },
                        "green": {
                            "type": ["integer", "string"]
                        },
                        "yellow": {
                            "type": ["integer", "string"]
                        }
                    },
                    "required": [
                        "red",
                        "none",
                        "green",
                        "yellow"
                    ]
                },
                "status": {
                    "type": ["string", "null"]
                },
                "documents": {
                    "type": ["array", "null"],
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "candidate_id": {
                                    "type": "string"
                                },
                                "document_ids": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "string"
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "candidate_id",
                                "document_ids"
                            ]
                        }
                    ]
                },
                "candidates": {
                    "type": ["array", "null"],
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "values": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "email": {
                                                    "type": "string"
                                                },
                                                "rank": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "email",
                                                "rank"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "values"
                            ]
                        }
                    ]
                },
                "removal_time": {
                    "type": ["string", "null"]
                },
                "advert_objects": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "values": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "channels": {
                                            "type": "array",
                                            "items": [
                                                {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {
                                                            "type": "string"
                                                        },
                                                        "status": {
                                                            "type": "string"
                                                        },
                                                        "removal_time": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "status",
                                                        "removal_time"
                                                    ]
                                                }
                                            ]
                                        },
                                        "reference": {
                                            "type": ["string", "null"]
                                        },
                                        "removal_time": {
                                            "type": ["string", "null"]
                                        }
                                    },
                                    "required": [
                                        "channels",
                                        "reference",
                                        "removal_time"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "id",
                        "values"
                    ]
                }
            },
            "required": [
                "flags",
                "status",
                "documents",
                "candidates",
                "removal_time",
                "advert_objects"
            ]
        },
        "broadbean_advert_references": {
            "type": ["array", "null"],
            "items": [
                {
                    "type": "string"
                }
            ]
        },
        "function_or_cost_centre": {
            "type": ["string", "null"]
        },
        "required_days_and_hours_note": {
            "type": ["string", "null"]
        },
        "payment_interval": {
            "type": ["string", "null"]
        },
        "job_description": {
            "type": ["string", "null"]
        },
        "experience_note": {
            "type": ["string", "null"]
        },
        "expenses_note": {
            "type": ["string", "null"]
        },
        "health_and_safety_note": {
            "type": ["string", "null"]
        },
        "client_terminate_note": {
            "type": ["string", "null"]
        },
        "candidate_terminate_note": {
            "type": ["string", "null"]
        },
        "contract_id": {
            "type": ["string", "null"]
        },
        "tenure_category_id": {
            "type": ["string", "null"]
        },
        "background_information_updated_by": {
            "type": ["string", "null"]
        }
    },
    "required": [
        "id",
        "event_id",
        "short_id",
        "created_at",
        "last_updated_at"
    ]
}
