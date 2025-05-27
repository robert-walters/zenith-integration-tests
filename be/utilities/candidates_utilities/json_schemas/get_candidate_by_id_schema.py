get_candidate_by_id_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": ["string"],
        },
        "event_id": {
            "type": ["string"],
        },
        "cv_link": {
            "type": ["string", "null"],
        },
        "desired_locations": {
            "type": ["string", "null"],
        },
        "desired_organisations": {
            "type": ["string", "null"],
        },
        "desired_salary_currency": {
            "type": ["string", "null"],
        },
        "desired_salary_period": {
            "type": ["string", "null"],
        },
        "desired_salary_value": {
            "type": ["number", "null"],
        },
        "visa_expiry": {
            "type": ["string", "null"],
        },
        "visa_type": {
            "type": ["string", "null"],
        },
        "preferred_name": {
            "type": ["string", "null"],
        },
        "preferred_pronoun": {
            "type": ["string", "null"],
        },
        "address_line_1": {
            "type": ["string", "null"],
        },
        "address_line_2": {
            "type": ["string", "null"],
        },
        "address_line_3": {
            "type": ["string", "null"],
        },
        "city": {
            "type": ["string", "null"],
        },
        "province": {
            "type": ["string", "null"],
        },
        "postcode": {
            "type": ["string", "null"],
        },
        "country_of_residence": {
            "type": ["string", "null"],
        },
        "national_information": {
            "type": ["object", "null"],
        },
        "location_remit": {
            "type": ["string"],
        },
        "client_id": {
            "type": ["string", "null"],
        },
        "responsible_user_id": {
            "type": ["string", "null"],
        },
        "responsible_team_id": {
            "type": ["string", "null"],
        },
        "last_contacted_at": {
            "type": ["string", "null"],
        },
        "last_updated_at": {
            "type": ["string"],
        },
        "created_by": {
            "type": ["string", "null"],
        },
        "desired_positions": {
            "type": ["array"],
            "items": {"type": "string"},
        },
        "position_type": {
            "type": ["string", "null"],
        },
        "rate_currency": {
            "type": ["string", "null"],
        },
        "rate_period": {
            "type": ["string", "null"],
        },
        "rate_value": {
            "type": ["number", "null"],
        },
        "package_breakdown": {
            "type": ["string", "null"],
        },
        "availability_date": {
            "type": ["string", "null"],
        },
        "availability_duration_unit": {
            "type": ["string", "null"],
        },
        "availability_duration_value": {
            "type": ["number", "null"],
        },
        "total_package": {
            "type": ["number", "null"],
        },
        "salary_last_updated_at": {
            "type": ["string", "null"],
        },
        "identity_reference": {
            "type": ["string", "null"],
        },
        "traditional_first_name": {
            "type": ["string", "null"],
        },
        "traditional_family_name": {
            "type": ["string", "null"],
        },
        "passport_number": {
            "type": ["string", "null"],
        },
        "hk_number_id": {
            "type": ["string", "null"],
        },
        "scheduler": {
            "type": ["object", "null"],
        },
        "has_meaningful_events": {
            "type": ["boolean"],
        },
        "expiry_date": {
            "type": ["string", "null"],
        },
        "original_source": {
            "type": ["string", "null"],
        },
        "original_source_recorded_at": {
            "type": ["string", "null"],
        },
        "company_name": {
            "type": ["string", "null"],
        },
        "first_name": {
            "type": ["string", "null"],
        },
        "family_name": {
            "type": ["string", "null"],
        },
        "skills": {
            "type": ["string", "null"],
        },
        "language": {
            "type": ["string", "null"],
        },
        "situation_status": {
            "type": ["string", "null"],
        },
        "gender": {
            "type": ["string", "null"],
        },
        "gender_other": {
            "type": ["string", "null"],
        },
        "nationality": {
            "type": ["string", "null"],
        },
        "date_of_birth": {
            "type": ["string", "null"],
        },
        "industry": {
            "type": ["string", "null"],
        },
        "created_at": {
            "type": ["string"],
        },
        "background_information": {
            "type": ["string", "null"],
        },
        "traits_skills": {
            "type": ["string", "null"],
        },
        "people_skills": {
            "type": ["string", "null"],
        },
        "language_skills": {
            "type": ["string", "null"],
        },
        "work_education_description": {
            "type": ["string", "null"],
        },
        "salary_availability_description": {
            "type": ["string", "null"],
        },
        "desired_jobs_description": {
            "type": ["string", "null"],
        },
        "last_updated_by": {
            "type": ["string", "null"],
        },
        "background_information_updated_at": {
            "type": ["string", "null"]
        },
        "sofi_number": {
            "type": ["string", "null"]
        },
        "purchase_acc_ref": {
            "type": ["string", "null"]
        },
        "pay_frequency": {
            "type": ["string", "null"]
        },
        "visa_type_updated_by": {
            "type": ["string", "null"]
        },
        "trade_btw_number": {
            "type": ["string", "null"]
        },
        "moj_result": {
            "type": ["string", "null"],
            "enum": [None, "CLEAR", "RESULT"]
        },
        "trade_reg_co_name": {
            "type": ["string", "null"]
        },
        "company_pay_type": {
            "type": ["string", "null"]
        },
        "pay_type": {
            "type": ["string", "null"],
            "enum": [None, "MGT", "PAY"]
        },
        "bank_acc_2nd_name": {
            "type": ["string", "null"]
        },
        "provided_document_type": {
            "type": ["string", "null"]
        },
        "company_type": {
            "type": ["string", "null"],
            "enum": [None, "NONE", "TRUST", "INCORPORATED"]
        },
        "trade_kvk_number": {
            "type": ["string", "null"]
        },
        "has_received_additional_documents": {
            "type": ["boolean", "null"]
        },
        "other_govt_identification": {
            "type": ["string", "null"]
        },
        "visa_type_updated_at": {
            "type": ["string", "null"]
        },
        "company_acn_code": {
            "type": ["string", "null"]
        },
        "bank_acc_name": {
            "type": ["string", "null"]
        },
        "company_address": {
            "type": ["string", "null"]
        },
        "company_notes": {
            "type": ["string", "null"]
        },
        "provided_document_updated_at": {
            "type": ["string", "null"]
        },
        "bank_acc_number": {
            "type": ["string", "null"]
        },
        "govt_identification_type": {
            "type": ["string", "null"],
            "enum": [None, "DRIVERS_LICENSE", "OTHER"]
        },
        "additional_documents_description": {
            "type": ["string", "null"]
        },
        "provided_document_updated_by": {
            "type": ["string", "null"]
        },
        "company_abn_code": {
            "type": ["string", "null"]
        },
        "background_information_updated_by": {
            "type": ["string", "null"]
        },
        "govt_identification_updated_at": {
            "type": ["string", "null"]
        },
        "candidate_province": {
            "type": ["string", "null"],
            "enum": [None, "AUSTRALIAN_CAPITAL_TERRITORY", "NEW_SOUTH_WALES", "NORTHERN_TERRITORY", "SOUTH_AUSTRALIA",
                     "WESTERN_AUSTRALIA", "QUEENSLAND", "TASMANIA", "VICTORIA"]
        },
        "bank_name": {
            "type": ["string", "null"]
        },
        "pay_method": {
            "type": ["string", "null"]
        },
        "passport_expiry_date": {
            "type": ["string", "null"]
        },
        "bank_sort_code": {
            "type": ["string", "null"]
        },
        "govt_identification_updated_by": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "id",
        "event_id",
        "location_remit",
        "desired_positions",
        "created_at",
        "last_updated_at",
    ],
}
