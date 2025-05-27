get_candidate_activity_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "created_at": {
            "type": "string"
        },
        "last_updated_at": {
            "type": "string"
        },
        "job_id": {
            "type": ["string", "null"]
        },
        "event_id": {
            "type": "string"
        },
        "candidate_id": {
            "type": "string"
        },
        "email_id": {
            "type": "string"
        },
        "outcome": {
            "type": "string",
            "enum": ["event_did_not_happen", "wrong_entry", "bb_candidate_green_flagged", "bb_candidate_amber_flagged",
                     "reject", "none", None]
        },
        "outcome_date": {
            "type": "string"
        },
        "notes": {
            "type": "string"
        },
        "type": {
            "type": "string",
            "enum": ["client_call", "bd_call", "client_meeting", "proposal_submitted", "client_event",
                     "client_sponsorship", "assessment_test_training", "candidate_call", "candidate_iv",
                     "candidate_review", "digital_passport_sent", "email_sent", "email_received", "job_spec_sent",
                     "key_info_doc_sent", "mailshot", "reference_check", "spec_cv_sent", "spec_digital_passport_sent",
                     "video_profile", "automated_survey", "candidate_event", "candidate_sponsorship",
                     "candidate_website_account_created", "e_guide", "email_marketing",
                     "international_candidate_management", "referral", "research_survey", "salary_survey",
                     "signed_up_for_job_alerts", "webinar", "revenue_assurance", "job_advert_posted",
                     "broadbean_greenflagged_candidate", "broadbean_amberflagged_candidate",
                     "contract_placement_template_created", "temporary_fee_completed", "temporary_contract_amendment",
                     "temporary_contract_extended", "temporary_contract_terminated", "client_job_confirmation",
                     "longlist", "shortlist", "round_1", "round_2", "additional_round", "cv_sent", "offer", "placed",
                     "placed_completed", "placed_backout", "nonplacement_fee_completed", "nonplacement_fee_backout",
                     "email", "placed_temporary_contract", "client_review", "spec_cv", "candidate_privacy_notice_sent",
                     "candidate_registration", "key_information_document", "meeting_consultant",
                     "temporary_contract_completed"]
        },
        "activity_group": {
            "type": "string",
            "enum": ["advert_management", "billing", "call", "cv_to_client",
                     "document", "email", "job_stage", "marketing", "meeting", "other", None]
        },
        "event_date": {
            "type": "string"
        },
        "event_start_time": {
            "type": "string"
        },
        "event_end_time": {
            "type": "string"
        },
        "event_date_time": {
            "type": "string"
        },
        "event_type": {
            "type": "string",
            "enum": ["face_to_face", "video", "phone", "assessment", None]
        },
        "event_location": {
            "type": "string"
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
            "type": "string",
            "enum": ["candidate", "client", "job", "organisation", "billing", "email", "Profile", None]
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
                    "type": "string"
                }
            ]
        },
        "responsible_team_id": {
            "type": "string"
        },
        "created_by": {
            "type": "string"
        },
        "application_time": {
            "type": "string"
        },
        "source": {
            "type": "string",
            "enum": ["LINKEDIN", "LINKEDIN_SOCIAL", "ROBERTWALTERS_BE", "ROBERTWALTERS_FR", "ROBERTWALTERS_DE",
                     "ROBERTWALTERS_IT", "ROBERTWALTERS_LU", "ROBERTWALTERS_CH", "ROBERTWALTERS_BR",
                     "ROBERTWALTERS_CAREERS", "ROBERTWALTERS_CL", "ROBERTWALTERS_MX", "ROBERTWALTERS_CA",
                     "ROBERTWALTERS_AE", "ROBERTWALTERS_ID", "ROBERTWALTERS_SG", "ROBERTWALTERS_TH", "ROBERTWALTERS_MY",
                     "ROBERTWALTERS_PH", "ROBERTWALTERS_VN", "TRABAJANDO", "TRABAJANDO_ES", "WALTERSPEOPLE_CL",
                     "ACCACAREERS_NEW", "BROADBEAN_V2", "JOBSCABI", "ROBERTWALTERS_USA", "EFINANCIAL_NEW",
                     "MONSTER_ASIA_NEW", "JOBSTREET", "JOBSDB", "BROADBEAN_DEMO_BOARD", "BROADBEAN_TEST_BOARD",
                     "ROBERTWALTERS_AFRICA", "ROBERTWALTERS_AU", "ROBERTWALTERS_IE", "ROBERTWALTERS_JP",
                     "ROBERTWALTERS_KR", "ROBERTWALTERS_NL", "ROBERTWALTERS_NZ", "ROBERTWALTERS_PT", "ROBERTWALTERS_ZA",
                     "ROBERTWALTERS_ES", "ROBERTWALTERS_UK", "WALTERSPEOPLE_UK", "WALTERSPEOPLE_BE", "WALTERSPEOPLE_CH",
                     "WALTERSPEOPLE_FR", "WALTERSPEOPLE_IE", "WALTERSPEOPLE_NL", "WALTERSPEOPLE_ES", "JOBSIE",
                     "JOBSERVE_XML", "REED_PREMIUM", "PNET", "THELAWYER", "CVLIBRARY", "CWJOBS", "PIRICAL",
                     "TOTALJOBS", "SEEK_OZ", "ROBERTWALTERS_HK", "ROBERTWALTERS_TW", "ROBERTWALTERS_CN", "RW_WEBSITE",
                     "ZENITH_DATABASE", "LINKEDIN_AD", "WP_WEBSITE", "CAREERCROSS", "ENJAPAN_API", "CAREER_CARVER_API",
                     "DAIJOB", "INDEED_SPONSORED_CUSTOM", "INDEED_SPONSORED_DEFAULT", "CAREERONE",
                     "CONNECTCAREERS_VOLCANIC", "ETHICAL_JOBS", "IWORK", "RECRUIT", "JOBSEARCH_JOB_AU", "APEC",
                     "CADREMPLOI", "ENGAGEMENT_JEUNES", "REGIONJOBS", "JOBAT", "JOBSCH", "JOB_UP_NEW", "LINKFINANCE",
                     "LINTBERG", "NATIONALE_VACATURE", "POLEEMPLOI_NEW", "STEPSTONE_DE_V2", "STEPSTONE_BE_V2",
                     "STEPSTONE_FR", "STEPSTONE_BE_JOBFEED", "STEPSTONE_DE_XML", "STEPSTONE_DE", "VDAB",
                     "WELCOME_TO_THE_JUNGLE", "XING_PROFESSIONAL", "MONSTERXML", "FIGARO_EMPLOI", "LEEM",
                     "VILLAGEJUSTICE", "JOB_TEASER_EMPLOI_SLOTS", "INFOJOBS", "JOBSEARCH_GOV_AU", "ECAREERFA",
                     "CAREERCROSS_HAKEN", "RIKUNABI", "TALENTSEARCH", "GLASSDOOR", "NIKKEICAREERNET", "REED_FEATURED", None]
        },
        "meeting_title": {
            "type": "string"
        },
        "reminder_minutes": {
            "type": "integer"
        },
        "is_teams_meeting": {
            "type": "boolean"
        },
        "attachment_ids": {
            "type": "array",
            "items": [
                {
                    "type": "null"
                }
            ]
        },
        "message": {
            "type": "string"
        },
        "automated": {
            "type": "boolean"
        },
        "module": {
            "type": "string"
        },
        "meeting_id": {
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
        "automated",
        "hidden",
        "created_at",
        "last_updated_at"
    ]
}
