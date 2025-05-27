import random

from src.be.configuration.config_parser import get_config_value
from src.be.utilities.get_core_api_data import get_user_id_from_core_api, get_team_id_from_core_api, \
    get_client_id_from_core_api
from src.be.utilities.useful_functions import *

resp_user = get_user_id_from_core_api()
resp_team = get_team_id_from_core_api()
remit = get_config_value("remit")


def random_situation_status():
    statuses = ["active", "passive"]
    return random.choice(statuses)


def create_candidate_required_fields_payload():
    return {"location_remit": remit,
            "situation_status": random_situation_status(),
            "responsible_user_id": get_user_id_from_core_api(),
            "responsible_team_id": get_team_id_from_core_api(),
            "first_name": get_random_first_name(),
            "family_name": get_random_last_name(),
            }


def create_candidate_full_payload():
    return {
        "cv_link": "https://api.digitalzenith.io/command/documents/54e81737-eebe-4b68-887d-d6f5afdd1eef?file_type=pdf",
        "desired_locations": random_country(),
        "desired_organisations": get_random_organisation(),
        "desired_salary_currency": "USD",
        "desired_salary_period": "month",
        "desired_salary_value": 6500,
        "visa_expiry": get_today_date(),
        "visa_type": "au_all_other_aus_visas",
        "preferred_name": "Mr John Doe",
        "preferred_pronoun": "he_him_his",
        "address_line_1": "123 Main Street",
        "address_line_2": "Apt 4B",
        "address_line_3": "Springfield, IL 62704",
        "city": "Dublin",
        "province": "IE Dublin",
        "postcode": "D02 XY45",
        "country_of_residence": "IRL",
        "national_information": {"test": "test"},
        "location_remit": remit,
        "client_id": get_client_id_from_core_api(),
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "created_by": get_user_id_from_core_api(),
        "desired_positions": [
            "INTERIM",
            "PERMANENT"
        ],
        "position_type": "interim",
        "rate_currency": "USD",
        "rate_period": "per_month",
        "rate_value": 47000,
        "package_breakdown": "47K x 12M",
        "availability_date": "2024-06-10",
        "availability_duration_unit": "month",
        "availability_duration_value": 2,
        "total_package": 600000,
        "salary_last_updated_at": get_date_time_format(),
        "identity_reference": "1122003888985",
        "traditional_first_name": get_random_first_name(),
        "traditional_family_name": get_random_last_name(),
        "passport_number": "AB1234567",
        "hk_number_id": "Z987654(3)",
        "scheduler": {
            "record": {
                "age": {
                    "days": 5,
                    "hours": 8,
                    "years": 2
                },
                "deleted": False
            },
            "interval": "5 days",
            "timestamp": "2022-12-31T23:59:59.999Z"
        },
        "has_meaningful_events": False,
        "expiry_date": "2021-02-22",
        "original_source": "LINKEDIN",
        "original_source_recorded_at": "2021-07-23T15:30:00.000Z",
        "company_name": "Apex Consulting Group",
        "first_name": get_random_first_name(),
        "family_name": get_random_last_name(),
        "skills": "Adobe Photoshop, AutoCAD",
        "language": "English",
        "situation_status": random_situation_status(),
        "gender": "male",
        "gender_other": "other",
        "nationality": "british",
        "date_of_birth": "1974-07-25",
        "industry": "Data Scientist",
        "background_information": "Transfer from London Profile",
        "background_information_updated_by": get_user_id_from_core_api(),
        "background_information_updated_at": get_date_time_format(),
        "traits_skills": "Skills: EA",
        "people_skills": "4-5 ppl",
        "language_skills": "Mandarin, Cantonese, and English",
        "work_education_description": "Access, CaseWare, Excel, MS Office, Powerpoint",
        "salary_availability_description": "Notice Period: 3 months",
        "desired_jobs_description": "Engineer",
        "moj_result": "CLEAR",
        "provided_document_type": "AUSTRALIAN_PASSPORT",
        "provided_document_updated_by": get_user_id_from_core_api(),
        "provided_document_updated_at": get_date_time_format(),
        "has_received_additional_documents": True,
        "additional_documents_description": random_string(10),
        "passport_expiry_date": get_today_date(),
        "govt_identification_type": "DRIVERS_LICENSE",
        "govt_identification_updated_by": get_user_id_from_core_api(),
        "govt_identification_updated_at": get_date_time_format(),
        "visa_type_updated_by": get_user_id_from_core_api(),
        "visa_type_updated_at": get_date_time_format(),
        "candidate_province": "AUSTRALIAN_CAPITAL_TERRITORY",
        "company_type": "TRUST",
        "company_abn_code": random_string(20),
        "company_acn_code": random_string(10),
        "company_address": random_string(20),
        "company_notes": random_string(20)
    }


def wrong_remit_format_payload():
    payload = create_candidate_full_payload()
    payload['location_remit'] = random_string(6)
    return payload


def missing_remit_payload():
    payload = create_candidate_full_payload()
    payload.pop("location_remit")
    return payload


def missing_first_name_payload():
    payload = create_candidate_full_payload()
    payload.pop("first_name")
    return payload


def missing_last_name_payload():
    payload = create_candidate_full_payload()
    payload.pop("family_name")
    return payload


missing_last_name_payload()


def wrong_situation_status_payload():
    payload = create_candidate_full_payload()
    payload['situation_status'] = random_string(6)
    return payload


def missing_responsible_user_payload():
    payload = create_candidate_full_payload()
    payload.pop("responsible_user_id")
    return payload


def missing_responsible_team_payload():
    payload = create_candidate_full_payload()
    payload.pop("responsible_team_id")
    return payload


def wrong_responsible_user_payload():
    payload = create_candidate_full_payload()
    payload['responsible_user_id'] = get_random_uuid()
    return payload


def wrong_responsible_team_payload():
    payload = create_candidate_full_payload()
    payload['responsible_user_id'] = get_random_uuid()
    return payload
