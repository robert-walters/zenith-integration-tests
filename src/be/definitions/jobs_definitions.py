import random

import requests

from src.be.utilities.logger import add_log, logger


def create_job_request(base_url, endpoint, payload, headers):
    response = requests.post(base_url + endpoint, json=payload, headers=headers)
    add_log(response)
    return response


def update_job_request(base_url, endpoint, job_id, payload, headers):
    response = requests.put(base_url + endpoint + job_id, json=payload, headers=headers)
    add_log(response)
    return response


def delete_job_request(base_url, endpoint, job_id, headers):
    response = requests.delete((base_url + endpoint + job_id), headers=headers)
    add_log(response)
    return response


def delete_job_ignore_dependencies(base_url, endpoint, job_id, headers):
    response = requests.delete(base_url + endpoint + job_id + "?check-dependencies=false", headers=headers)
    add_log(response)
    return response


def delete_job_checking_dependencies(base_url, endpoint, job_id, headers):
    response = requests.delete(base_url + endpoint + job_id + "?check-dependencies=true", headers=headers)
    add_log(response)
    return response


def get_jobs_request(base_url, endpoint, params, headers):
    response = requests.get(base_url + endpoint + params, headers=headers)
    add_log(response)
    return response


def get_job_id(base_url, endpoint, payload, headers):
    response = create_job_request(base_url, endpoint, payload, headers)
    assert response.status_code == 200, f"Response: {response.json()}"
    return response.json()['id']


def random_job_type():
    job_types = ["perm", "temp", "interim", "temp_to_perm"]
    return random.choice(job_types)


def random_job_agreement_type():
    agreement_types = ["mapping", "contingent", "agreement_tbc", "exclusive", "non_exclusive",
                       "exclusive_no_placement_no_fee", "no_placement_no_fee", "retainer", "retainer_shortlist"]
    return random.choice(agreement_types)


def random_currency_rate():
    currencies = [
        "AUD", "BHD", "BRL", "CAD", "CLP", "CNY", "GBP", "HKD", "IDR", "JPY",
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
    return random.choice(currencies)


def random_job_source():
    sources = ["bd_call", "client_meeting", "ad_chase", "lead_from_colleague",
               "lead_from_candidate", "rpo", "psa", "inbound_call_from_client",
               "marketing_lead", "rw_client_development_director"]
    return random.choice(sources)


def random_rate_period():
    periods = ["per_hour", "per_day", "per_week", "per_month", "per_annum"]
    return random.choice(periods)


def random_status():
    statuses = ["live", "lead", "dummy", "closed_successfully", "closed_internally", "closed_by_competitor",
                "cancelled", "on_hold", "completed_successfully"]
    return random.choice(statuses)


def random_rpo():
    rpo = ["allegis", "ams", "cielo", "guidant_global", "pontoon", "pro_unlimited", "resource_solutions",
           "sourcebreaker", "other", "direct"]
    return random.choice(rpo)


def random_contract_length_unit():
    units = ["week", "day", "month"]
    return random.choice(units)


def random_payment_interval():
    intervals = ["WEEKLY", "FORTNIGHTLY", "MONTHLY"]
    return random.choice(intervals)


def create_job_required_properties():
    return ["organisation_id", "location_id", "title", "type", "agreement_type", "source",
            "responsible_user_id", "responsible_team_id"]


def update_job_required_properties():
    return ["organisation_id", "location_id", "title", "type", "agreement_type", "source",
            "responsible_user_id", "responsible_team_id", "short_id", "location_remit", "job_posting_required",
            "exclusive"]


def update_job_additional_properties():
    return ["preferred_start_date", "rate_currency", "rate_min_value", "rate_max_value", "rate_period",
            "contract_length_unit", "target_fee", "bonus_package", "status", "specification",
            "background_information", "margin_markup", "timesheet_unit", "cv_submission",
            "required_days_and_hours_note", "payment_interval", "rpo"]


def create_job_additional_properties():
    return ["preferred_start_date", "rate_currency", "rate_min_value", "rate_max_value", "rate_period",
            "contract_length_unit", "target_fee", "bonus_package", "status", "specification",
            "background_information", "margin_markup", "job_posting_required", "timesheet_unit", "cv_submission",
            "short_id", "required_days_and_hours_note", "payment_interval", "rpo"]
