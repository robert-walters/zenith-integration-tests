from src.be.definitions.organisations_definitions import random_credit_status
from src.be.utilities.get_core_api_data import *

resp_user = get_user_id_from_core_api()
resp_team = get_team_id_from_core_api()


def create_organisation_required_payload():
    return {"name": random_string(10),
            "is_employer_only": False,
            "responsible_user_id": get_user_id_from_core_api(),
            "responsible_team_id": get_team_id_from_core_api()
            }


def create_organisation_employer_only_required_payload():
    return {"name": random_string(10),
            "is_employer_only": True,
            "responsible_user_id": get_user_id_from_core_api(),
            "testxyz": "just_test"}


def create_organisation_full_payload():
    return {
        "name": get_random_organisation(),
        "background_information": random_string(20),
        "industry": get_random_qualification(),
        "is_employer_only": False,
        "industries": [
            {"industry": "Automotive - Other",
             "type": "Automotive"}
        ],
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "registration_number": random_string(12),
        "tax_id": get_random_tax_id(),
        "po_required": False,
        "credit_status": random_credit_status(),
        "credit_expiry": get_date_time_format(),
        "credit_notes": random_string(25),
        "organisation_traditional_name": get_random_organisation(),
        "background_information_updated_by": get_user_id_from_core_api(),
        "background_information_updated_at": get_date_time_format(),
        "created_by": get_user_id_from_core_api()
    }


def create_organisation_employer_only_full_payload():
    return {
        "name": get_random_organisation(),
        "is_employer_only": True,
    }


def create_organisation_industries_duplicate_payload():
    payload = create_organisation_full_payload()
    payload['industries'] = [
        {
            "industry": "Car Manufacturer (OEM)",
            "type": "Automotive"
        },
        {
            "industry": "Car Manufacturer (OEM)",
            "type": "Automotive"
        }
    ]
    return payload


def create_organisation_more_than_five_industries():
    payload = create_organisation_full_payload()
    payload['industries'] = [
        {
            "industry": "Car Manufacturer (OEM)",
            "type": "Automotive"
        },
        {
            "industry": "Supermarkets/Convenience",
            "type": "Retail"
        },
        {
            "industry": "Ecommerce",
            "type": "Internet"
        },
        {
            "industry": "Sport",
            "type": "Leisure"
        },
        {
            "industry": "Water & Waste",
            "type": "Energy"
        },
        {
            "industry": "Public",
            "type": "Education"
        }
    ]
    return payload
