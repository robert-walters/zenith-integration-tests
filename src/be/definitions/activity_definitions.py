import random
import requests
from src.be.utilities.logger import add_log


def create_original_activity_request(base_url, payload, headers):
    response = requests.post(base_url + "activities/", json=payload, headers=headers)
    add_log(response)
    return response


def get_original_activity_request(base_url, activity_id, headers):
    response = requests.get(base_url + "activities/" + activity_id, headers=headers)
    add_log(response)
    return response


def get_original_activity_with_filters_request(base_url, filters, headers):
    response = requests.get(base_url + "activities/", params=filters, headers=headers)
    add_log(response)
    return response


def update_original_activity_request(base_url, activity_id, payload, headers):
    response = requests.put(base_url + "activities/" + activity_id, json=payload, headers=headers)
    add_log(response)
    return response


def delete_original_activity_request(base_url, activity_id, headers):
    response = requests.delete(base_url + "activities/" + activity_id, headers=headers)
    add_log(response)
    return response


def create_activity_request(base_url, endpoint, entity_id, payload, headers):
    response = requests.post(base_url + endpoint + entity_id + "/activities", json=payload, headers=headers)
    add_log(response)
    return response


def update_activity_request(base_url, endpoint, entity_id, act_id, payload, headers):
    response = requests.put(base_url + endpoint + entity_id + "/activities/" + act_id, json=payload, headers=headers)
    add_log(response)
    return response


def delete_activity_request(base_url, endpoint, entity_id, activity_id, headers):
    response = requests.delete(base_url + endpoint + entity_id + "/activities/" + activity_id, headers=headers)
    add_log(response)
    return response


def get_activity_request(base_url, endpoint, entity_id, activity_id, headers):
    response = requests.get(base_url + endpoint + entity_id + "/activities/" + activity_id, headers=headers)
    add_log(response)
    return response


def get_activity_id(base_url, endpoint, entity_id, payload, headers):
    activity_response = create_activity_request(base_url, endpoint, entity_id,
                                                payload, headers)

    assert activity_response.status_code == 200, f"Response: {activity_response.json()}"
    return activity_response.json()['id']


def create_candidate_activity_required_props():
    return ["responsible_user_id", "responsible_team_id", "type"]


def create_candidate_activity_original_required_props():
    return ["responsible_user_id", "responsible_team_id", "type", "record_origin"]


def create_candidate_activity_additional_props():
    return ["outcome_date", "event_date", "email_id", "outcome", "notes",
            "event_date_time", "event_type", "event_location", "other_consultant_ids", "application_time", "source",
            "meeting_title", "reminder_minutes", "is_teams_meeting", "event_start_time", "event_end_time", "message",
            "module", "hidden", "created_by"]


def update_candidate_activity_required_props():
    return ["responsible_user_id", "responsible_team_id", "automated", "type", "hidden"]


def update_candidate_activity_original_required_props():
    return ["responsible_user_id", "responsible_team_id", "organisation_id", "client_ids", "type"]


def update_candidate_activity_additional_props():
    return ["outcome_date", "event_date", "email_id", "outcome", "notes", "event_date_time", "event_type",
            "event_location", "other_consultant_ids", "application_time", "source", "meeting_title", "reminder_minutes",
            "is_teams_meeting", "event_start_time", "event_end_time", "message", "module", ]


def create_client_activity_required_props():
    return ["responsible_user_id", "responsible_team_id", "type"]


def create_client_activity_original_required_props():
    return ["responsible_user_id", "responsible_team_id", "type", "client_ids", "record_origin"]


def create_client_activity_additional_props():
    return ["meeting_title", "reminder_minutes", "is_teams_meeting", "email_id", "outcome", "outcome_date", "notes",
            "event_date", "event_start_time", "event_end_time",
            "event_date_time", "event_type", "event_location", "other_consultant_ids", "application_time",
            "source", "message", "module", "created_by"]


def update_client_activity_required_props():
    return [
        "responsible_user_id", "responsible_team_id", "type", "hidden", "automated"
    ]


def update_client_activity_original_required_props():
    return [
        "responsible_user_id", "responsible_team_id", "type", "hidden", "automated", "client_id"
    ]


def update_client_activity_additional_props():
    return ["email_id", "outcome", "outcome_date", "notes", "event_date", "event_start_time", "event_end_time",
            "event_date_time", "event_type", "event_location", "other_consultant_ids", "application_time",
            "source", "message", "module"]


def create_job_activity_required_props():
    return ["responsible_user_id", "responsible_team_id", "type"]


def create_job_activity_original_required_props():
    return ["responsible_user_id", "responsible_team_id", "type", "record_origin"]


def create_job_activity_additional_props():
    return ["email_id", "outcome", "outcome_date", "notes", "event_date", "event_start_time", "event_end_time",
            "event_date_time", "event_type", "event_location", "created_by", "application_time", "source",
            "hidden", "fee_id", "placement_type", "placement_start_date", "placement_end_date", "bb_boards"]


def update_job_activity_required_props():
    return ["responsible_user_id", "responsible_team_id", "type", "hidden"]


def update_job_activity__original_required_props():
    return ["responsible_user_id", "responsible_team_id", "type", "hidden", "candidate_id"]


def update_job_activity_additional_props():
    return ["email_id", "outcome", "outcome_date", "notes", "event_date", "event_start_time", "event_end_time",
            "event_date_time", "event_type", "event_location", "application_time", "source", "fee_id",
            "placement_type", "placement_start_date", "placement_end_date", "bb_boards"]


def create_organisation_activity_required_props():
    return ["responsible_user_id", "responsible_team_id", "type"]


def create_organisation_activity_original_required_props():
    return ["responsible_user_id", "responsible_team_id", "type", "record_origin"]


def create_organisation_activity_additional_props():
    return ["email_id", "outcome", "outcome_date", "notes", "event_date", "event_start_time", "event_end_time",
            "event_date_time", "event_type", "event_location", "created_by", "application_time", "source",
            "hidden", "client_ids"]


def update_organisation_activity_required_props():
    return ["responsible_user_id", "responsible_team_id", "type", "hidden"]


def update_organisation_activity_original_required_props():
    return ["responsible_user_id", "responsible_team_id", "type", "hidden", "organisation_id"]


def update_organisation_activity_additional_props():
    return ["email_id", "outcome", "outcome_date", "notes", "event_date", "event_start_time", "event_end_time",
            "event_date_time", "event_type", "event_location", "application_time", "source"]


def random_activity_outcome():
    outcomes = ["event_did_not_happen", "wrong_entry", "bb_candidate_green_flagged", "bb_candidate_amber_flagged",
                "reject", "none"]
    return random.choice(outcomes)


def random_candidate_activity_type():
    types = [
        "assessment_test_training", "candidate_call", "candidate_iv", "meeting_consultant", "candidate_review",
        "digital_passport_sent", "email_sent", "email_received", "job_spec_sent", "candidate_privacy_notice_sent",
        "key_info_doc_sent", "mailshot", "reference_check", "spec_cv_sent", "spec_digital_passport_sent",
        "video_profile", "automated_survey", "candidate_event", "candidate_sponsorship",
        "candidate_website_account_created", "e_guide", "email_marketing",
        "international_candidate_management", "referral", "research_survey", "salary_survey",
        "signed_up_for_job_alerts", "webinar", "revenue_assurance", "candidate_registration",
        "key_information_document"]
    return random.choice(types)


def random_client_activity_type():
    types = ["automated_survey", "bd_call", "client_call", "client_event", "client_meeting", "client_sponsorship",
             "client_review", "digital_passport_sent", "e_guide", "email_marketing", "email_sent", "email_received",
             "mailshot", "proposal_submitted", "reference_check", "referral", "research_survey", "salary_survey",
             "spec_cv_sent", "spec_digital_passport_sent", "webinar", "client_job_confirmation", "revenue_assurance"]
    return random.choice(types)


def random_job_activity_type():
    types = ["digital_passport_sent", "email_sent", "email_received", "job_spec_sent", "reference_check",
             "spec_cv_sent", "spec_digital_passport_sent", "automated_survey", "assessment_test_training",
             "client_event", "client_sponsorship", "e_guide", "email_marketing", "referral", "research_survey",
             "salary_survey", "webinar", "job_advert_posted", "broadbean_greenflagged_candidate",
             "broadbean_amberflagged_candidate", "revenue_assurance", "contract_placement_template_created",
             "temporary_fee_completed", "temporary_contract_amendment", "temporary_contract_extended",
             "temporary_contract_terminated", "client_job_confirmation"]
    return random.choice(types)


def random_organisation_activity_type():
    types = ["client_meeting", "digital_passport_sent", "email_sent", "email_received", "proposal_submitted",
             "spec_cv_sent", "spec_digital_passport_sent", "client_job_confirmation", "revenue_assurance"]
    return random.choice(types)


def random_job_activity_placement_type():
    types = ["A", "W", "X", "C", "N", "P", "R", "L", "S", "U", "T", "F", "TC"]
    return random.choice(types)


def random_activity_event_type():
    event_types = ["face_to_face", "video", "phone", "assessment"]
    return random.choice(event_types)


def random_activity_source():
    sources = ["LINKEDIN", "LINKEDIN_SOCIAL", "ROBERTWALTERS_BE", "ROBERTWALTERS_FR", "ROBERTWALTERS_DE",
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
               "JOBSERVE_XML", "REED_PREMIUM", "PNET", "THELAWYER", "CVLIBRARY", "CWJOBS", "PIRICAL", "TOTALJOBS",
               "SEEK_OZ", "ROBERTWALTERS_HK", "ROBERTWALTERS_TW", "ROBERTWALTERS_CN", "RW_WEBSITE",
               "ZENITH_DATABASE", "LINKEDIN_AD", "WP_WEBSITE", "CAREERCROSS", "ENJAPAN_API", "CAREER_CARVER_API",
               "DAIJOB", "INDEED_SPONSORED_CUSTOM", "INDEED_SPONSORED_DEFAULT", "CAREERONE",
               "CONNECTCAREERS_VOLCANIC", "ETHICAL_JOBS", "IWORK", "RECRUIT", "JOBSEARCH_JOB_AU", "APEC",
               "CADREMPLOI", "ENGAGEMENT_JEUNES", "REGIONJOBS", "JOBAT", "JOBSCH", "JOB_UP_NEW", "LINKFINANCE",
               "LINTBERG", "NATIONALE_VACATURE", "POLEEMPLOI_NEW", "STEPSTONE_DE_V2", "STEPSTONE_BE_V2",
               "STEPSTONE_FR", "STEPSTONE_BE_JOBFEED", "STEPSTONE_DE_XML", "STEPSTONE_DE", "VDAB",
               "WELCOME_TO_THE_JUNGLE", "XING_PROFESSIONAL", "MONSTERXML", "FIGARO_EMPLOI", "LEEM",
               "VILLAGEJUSTICE", "JOB_TEASER_EMPLOI_SLOTS", "INFOJOBS", "JOBSEARCH_GOV_AU", "ECAREERFA",
               "CAREERCROSS_HAKEN", "RIKUNABI", "TALENTSEARCH", "GLASSDOOR", "NIKKEICAREERNET", "REED_FEATURED"]
    return random.choice(sources)
