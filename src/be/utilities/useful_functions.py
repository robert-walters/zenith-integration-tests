import json
import string

from dateutil.relativedelta import relativedelta
from jsonschema.validators import validate
from faker import Faker
from datetime import date, datetime, timezone
import random
import uuid

from src.be.configuration.config_parser import get_token, get_config_value

faker = Faker()
xapi_value = get_config_value("xapi")


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def get_random_url():
    return faker.url()


def get_random_first_name():
    return "test_" + faker.first_name()


def get_random_last_name():
    return "test_" + faker.last_name()


def get_random_city():
    return "test_" + faker.city()


def random_country():
    return faker.country()


def get_today_date():
    return str(date.today())


def get_past_date(years):
    return str(date.today() - relativedelta(years=years))


def get_past_date_time(years):
    current_time = datetime.now(timezone.utc)
    past_date_time = current_time - relativedelta(years=years, minutes=30)
    formatted_time = past_date_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    return formatted_time


def get_future_date_time(years):
    current_time = datetime.now(timezone.utc)
    future_date_time = current_time + relativedelta(years=years, minutes=30)
    formatted_time = future_date_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    return formatted_time


def get_future_date(years):
    return str(date.today() + relativedelta(years=years))


def get_random_remit():
    country_codes = [
        'GBR', 'AFG', 'ALA', 'ALB', 'DZA', 'ASM', 'AND', 'AGO', 'AIA', 'ATA', 'ATG', 'ARG', 'ARM', 'ABW', 'AUS', 'AUT',
        'AZE', 'BHS',
        'BHR', 'BGD', 'BRB', 'BLR', 'BEL', 'BLZ', 'BEN', 'BMU', 'BTN', 'BOL', 'BES', 'BIH', 'BWA', 'BVT', 'BRA', 'IOT',
        'BRN', 'BGR',
        'BFA', 'BDI', 'CPV', 'KHM', 'CMR', 'CAN', 'CYM', 'CAF', 'TCD', 'CHL', 'CHN', 'CXR', 'CCK', 'COL', 'COM', 'COG',
        'COD', 'COK',
        'CRI', 'CIV', 'HRV', 'CUB', 'CUW', 'CYP', 'CZE', 'DNK', 'DJI', 'DMA', 'DOM', 'ECU', 'EGY', 'SLV', 'GNQ', 'ERI',
        'EST', 'SWZ',
        'ETH', 'FLK', 'FRO', 'FJI', 'FIN', 'FRA', 'GUF', 'PYF', 'ATF', 'GAB', 'GMB', 'GEO', 'DEU', 'GHA', 'GIB', 'GRC',
        'GRL', 'GRD',
        'GLP', 'GUM', 'GTM', 'GGY', 'GIN', 'GNB', 'GUY', 'HTI', 'HMD', 'VAT', 'HND', 'HKG', 'HUN', 'ISL', 'IND', 'IDN',
        'IRN', 'IRQ',
        'IRL', 'IMN', 'ISR', 'ITA', 'JAM', 'JPN', 'JEY', 'JOR', 'KAZ', 'KEN', 'KIR', 'PRK', 'KOR', 'KWT', 'KGZ', 'LAO',
        'LVA', 'LBN',
        'LSO', 'LBR', 'LBY', 'LIE', 'LTU', 'LUX', 'MAC', 'MDG', 'MWI', 'MYS', 'MDV', 'MLI', 'MLT', 'MHL', 'MTQ', 'MRT',
        'MUS', 'MYT',
        'MEX', 'FSM', 'MDA', 'MCO', 'MNG', 'MNE', 'MSR', 'MAR', 'MOZ', 'MMR', 'NAM', 'NRU', 'NPL', 'NLD', 'NCL', 'NZL',
        'NIC', 'NER',
        'NGA', 'NIU', 'NFK', 'MKD', 'MNP', 'NOR', 'OMN', 'PAK', 'PLW', 'PSE', 'PAN', 'PNG', 'PRY', 'PER', 'PHL', 'PCN',
        'POL', 'PRT',
        'PRI', 'QAT', 'REU', 'ROU', 'RUS', 'RWA', 'BLM', 'SHN', 'KNA', 'LCA', 'MAF', 'SPM', 'VCT', 'WSM', 'SMR', 'STP',
        'SAU', 'SEN',
        'SRB', 'SYC', 'SLE', 'SGP', 'SXM', 'SVK', 'SVN', 'SLB', 'SOM', 'ZAF', 'SGS', 'SSD', 'ESP', 'LKA', 'SDN', 'SUR',
        'SJM', 'SWE',
        'CHE', 'SYR', 'TWN', 'TJK', 'TZA', 'THA', 'TLS', 'TGO', 'TKL', 'TON', 'TTO', 'TUN', 'TUR', 'TKM', 'TCA', 'TUV',
        'UGA', 'UKR',
        'ARE', 'GBR', 'USA', 'UMI', 'URY', 'UZB', 'VUT', 'VEN', 'VNM', 'VGB', 'VIR', 'WLF', 'ESH', 'YEM', 'ZMB', 'ZWE'
    ]
    return random.choice(country_codes)


def get_random_uuid():
    return str(uuid.uuid4())


def get_random_organisation():
    return "test_" + faker.company()


def get_random_qualification():
    return "test_" + faker.job()


def get_random_tax_id():
    return "test_" + faker.ssn()


def get_date_time_format():
    date_obj = datetime.strptime(get_today_date(), "%Y-%m-%d")
    return date_obj.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def get_current_time():
    return datetime.now().strftime("%HH:%M:%S")


def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def random_number(min_number, max_number):
    return random.randint(min_number, max_number)


def get_request_body_json(response):
    return json.loads(response.request.body.decode('utf-8'))


def validate_response_with_expected_json(props_input, response_body, request_body):
    for prop in props_input:
        assert response_body[prop] == request_body[prop], f"Expect {response_body[prop]} to equals {request_body[prop]}"


def missing_required_field_payload(payload, prop):
    data = payload
    data.pop(prop)
    return data


def get_headers(content_type=None):
    if get_config_value("xapi") == "on":
        return {
            'x-api-key': get_config_value("api_key")
        }
    elif get_config_value("xapi") == "off":
        headers = {
            "Authorization": get_token()
        }
        if content_type:
            headers["Content-Type"] = content_type
        return headers
    else:
        raise ValueError("Invalid value for xapi_value. Must be 'on' or 'off'.")


def standard_headers():
    return get_headers("application/json")


def delete_headers():
    return get_headers("text/plain")


def wrong_headers():
    return get_headers("application/xml")


def validate_response_schema_and_fields(response_json, schema):
    validate(response_json, schema=schema)
    response_fields = set(response_json.keys())
    schema_fields = set(schema.get("properties", {}).keys())
    missing_fields = schema_fields - response_fields
    extra_fields = response_fields - schema_fields
    assert response_fields == schema_fields, (
        f"Response fields do not match schema.\n"
        f"Missing fields in response: {missing_fields}\n"
        f"Extra fields in response: {extra_fields}\n"
        f"Expected (Schema Fields): {schema_fields}\n"
        f"Got (Response Fields): {response_fields}"
    )