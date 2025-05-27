get_job_activities_schema = {
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
            "type": "string"
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
            "type": ["string", "null"],
            "enum": ["event_did_not_happen", "wrong_entry", "bb_candidate_green_flagged", "bb_candidate_amber_flagged",
                     "reject", "none", None]
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
            "enum": ["face_to_face", "video", "phone", "assessment"]
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
            "type": "string",
            "enum": ["candidate", "client", "job", "organisation", "billing", "email", "Profile"]
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
            "type": ["string", "null"],
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
                     "CAREERCROSS_HAKEN", "RIKUNABI", "TALENTSEARCH", "GLASSDOOR", "NIKKEICAREERNET", "REED_FEATURED"]
        },
        "hidden": {
            "type": "boolean"
        },
        "fee_id": {
            "type": ["string", "null"]
        },
        "placement_start_date": {
            "type": ["string", "null"]
        },
        "placement_end_date": {
            "type": ["string", "null"]
        },
        "placement_type": {
            "type": ["string", "null"],
            "enum": ["A", "W", "X", "C", "N", "P", "R", "L", "S", "U", "T", "F", "TC", None]
        },
        "bb_boards": {
            "type": "array",
            "items": [
                {
                    "type": ["string", "null"]
                }
            ]
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
        "last_updated_at"
    ]
}
