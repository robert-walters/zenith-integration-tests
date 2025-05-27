post_client_activity_schema = {
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
        "event_id": {
            "type": ["string", "null"]
        },
        "email_id": {
            "type": ["string", "null"]
        },
        "outcome": {
            "type": ["string", "null"],
            "enum": [None, "event_did_not_happen", "wrong_entry", "bb_candidate_green_flagged",
                     "bb_candidate_amber_flagged", "reject", "none"]
        },
        "outcome_date": {
            "type": ["string", "null"]
        },
        "notes": {
            "type": ["string", "null"]
        },
        "type": {
            "type": "string",
            "enum": [
                "automated_survey", "bd_call", "client_call", "client_event", "client_meeting",
                "client_sponsorship", "client_review", "digital_passport_sent", "e_guide", "email_marketing",
                "email_sent", "email_received", "mailshot", "proposal_submitted", "reference_check", "referral",
                "research_survey", "salary_survey", "spec_cv_sent", "spec_digital_passport_sent", "webinar",
                "client_job_confirmation", "revenue_assurance"
            ]
        },
        "activity_group": {
            "type": "string",
            "enum": ["advert_management", "billing", "call", "cv_to_client", "document", "email", "job_stage",
                     "marketing", "meeting", "other"]
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
            "type": ["string", "null"],
            "enum": [None, "face_to_face", "video", "phone", "assessment"]
        },
        "event_location": {
            "type": ["string", "null"]
        },
        "client_ids": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                }
            ]
        },
        "record_origin": {
            "type": ["string", "null"],
            "enum": [None, "candidate", "client", "job", "organisation", "billing", "email", "Profile"]
        },
        "organisation_id": {
            "type": ["string", "null"]
        },
        "candidate_id": {
            "type": ["string", "null"]
        },
        "job_id": {
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
            "type": ["string", "null"]
        },
        "application_time": {
            "type": ["string", "null"]
        },
        "source": {
            "type": ["string", "null"],
            "enum": [
                None, "LINKEDIN", "LINKEDIN_SOCIAL", "ROBERTWALTERS_BE", "ROBERTWALTERS_FR", "ROBERTWALTERS_DE",
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
                "CAREERCROSS_HAKEN", "RIKUNABI", "TALENTSEARCH", "GLASSDOOR", "NIKKEICAREERNET", "REED_FEATURED"
            ]
        },
        "meeting_title": {
            "type": ["string", "null"]
        },
        "reminder_minutes": {
            "type": ["integer", "null"]
        },
        "is_teams_meeting": {
            "type": ["boolean", "null"]
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
            "type": ["string", "null"]
        },
        "automated": {
            "type": "boolean"
        },
        "module": {
            "type": ["string", "null"]
        },
        "meeting_id": {
            "type": ["string", "null"]
        },
        "hidden": {
            "type": ["boolean", "null"]
        }
    },
    "required": [
        "id",
        "type",
        "record_origin",
        "activity_group",
        "responsible_user_id",
        "responsible_team_id",
        "automated",
        "created_at",
        "last_updated_at"
    ]
}
