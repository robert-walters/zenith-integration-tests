import pytest

from src.be.configuration.config_parser import get_config_value
from src.be.definitions.activity_definitions import get_original_activity_with_filters_request
from src.be.utilities.error_schema import error_schema
from src.be.utilities.useful_functions import random_string, get_random_uuid, standard_headers, \
    validate_response_schema_and_fields

base_url = get_config_value("base_url")
headers = standard_headers()


@pytest.mark.parametrize("type_filter", ['candidate_call', 'revenue_assurance', "spec_cv_sent"])
def test_get_activities_filtering_by_type(type_filter):
    filters = {"type": type_filter}
    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 200
    assert len(get_response.json()['results']) != 0
    assert all(record['type'] == type_filter for record in
               get_response.json()['results'])


@pytest.mark.parametrize("limit_filter", [1, 10, 100])
def test_get_activities_filtering_by_limit(limit_filter):
    filters = {"limit": limit_filter}
    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 200
    assert len(get_response.json()['results']) == limit_filter


@pytest.mark.parametrize("limit_filter", [1, 10, 100])
def test_get_activities_filtering_by_limit(limit_filter):
    filters = {"limit": limit_filter}
    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 200
    assert len(get_response.json()['results']) == limit_filter


def test_get_activities_filter_by_date():
    filters = {"created_at__lte": "2023-04-19T08:19:38.670Z"}
    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 200
    assert len(get_response.json()['results']) > 0


@pytest.mark.parametrize("limit_filter", [0, 101, -10])
def test_get_activities_filtering_by_exceeding_boundary_limit(limit_filter):
    filters = {"limit": limit_filter}
    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 400
    validate_response_schema_and_fields(get_response.json(), error_schema)


@pytest.mark.parametrize("date_filter", ["created_at", "last_updated_at", "event_date_time"])
def test_get_activities_with_invalid_date_filter(date_filter):
    filters = {date_filter + "__gt": "1"}
    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 400
    validate_response_schema_and_fields(get_response.json(), error_schema)


def test_get_activities_using_invalid_filter_name():
    filters = "responsible_user_id__" + random_string(10)
    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 400
    validate_response_schema_and_fields(get_response.json(), error_schema)


def test_get_activities_using_select_with_wrong_property():
    filters = "select=wrong_filter"
    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 200
    json_response = get_response.json()['results']
    assert all("id" in item for item in json_response)
    assert all("responsible_user_id" in item for item in json_response)
    assert all("activity_group" in item for item in json_response)
    assert all("record_origin" in item for item in json_response)


@pytest.mark.parametrize("asc_prop", ["created_at", "type", "outcome_date"])
def test_get_activities_using_ascending_order(asc_prop):
    filters = "order=" + asc_prop + "&limit=100&select=" + asc_prop

    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 200
    property_values = [item[asc_prop] for item in get_response.json()['results'] if
                       asc_prop in item and item[asc_prop]]
    assert all(property_values[i] <= property_values[i + 1] for i in
               range(len(property_values) - 1)), f"Records are not in descending order by {asc_prop}"


@pytest.mark.parametrize("desc_prop", ["created_at", "type", "outcome_date"])
def test_get_activities_using_descending_order(desc_prop):
    filters = "order=-" + desc_prop + "&limit=100&select=" + desc_prop

    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 200
    property_values = [item[desc_prop] for item in get_response.json()['results'] if
                       desc_prop in item and item[desc_prop]]
    assert all(property_values[i] >= property_values[i + 1] for i in
               range(len(property_values) - 1)), f"Records are not in descending order by {desc_prop}"


@pytest.mark.parametrize("nonexistent_value", [get_random_uuid()])
def test_get_activities_filtering_by_exceeding_boundary_limit(nonexistent_value):
    filters = {"candidate_id_eq": nonexistent_value}
    get_response = get_original_activity_with_filters_request(base_url, filters, headers)
    assert get_response.status_code == 200


def test_get_activities_unauthorized():
    get_response = get_original_activity_with_filters_request(base_url, None, None)
    assert get_response.status_code in (401, 403), f"Expected 401 or 403, but got {get_response.status_code}"

