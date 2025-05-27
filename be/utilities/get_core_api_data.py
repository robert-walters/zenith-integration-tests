import requests


from src.be.utilities.useful_functions import *

base_url = get_config_value("core_api")
command_url = get_config_value("command_url")
remit = get_config_value("remit")
boundary = "----WebKitFormBoundary" + random_string(16)
headers = {
    "Authorization": get_token()
}
multipart_headers = {
        "Authorization": get_token(),
        "Content-Type": f"multipart/form-data; boundary={boundary}"
    }
candidates_url = command_url + "candidates/"
jobs_url = command_url + "jobs/"
organisations_url = command_url + "organisations/"
clients_url = command_url + "clients/"
contracts_url = command_url + "organisations/v2/terms-conditions/contracts"


def get_core_api_data(endpoint, params):
    response = requests.get(base_url + endpoint, params, headers=headers)
    return response


def get_client_id_from_core_api():
    return get_core_api_data("clients", "").json()['results'][0]['id']


def get_client_by_id_from_core_api(client_id):
    return get_core_api_data("clients/" + client_id, "")


def get_user_id_from_core_api():
    return get_core_api_data("users", "filter[location_remit][$eq]=" + remit).json()['results'][0]['id']


def get_team_id_from_core_api():
    return get_core_api_data("users", "filter[location_remit][$eq]=" + remit).json()['results'][0]['primary_team']


def get_candidates_by_id_from_core_api(candidate_id):
    return get_core_api_data("candidates/" + candidate_id, "populator=core_candidate")


def get_organisation_id_from_core_api(location_id):
    return get_core_api_data("organisation/locations/" + location_id, "").json()['organisation']


def get_location_id_from_core_api():
    return get_core_api_data("organisation/locations", "").json()['results'][0]['id']


def get_job_id_from_core_api():
    return get_core_api_data("jobs", "").json()['results'][0]['id']


def get_organisations_by_id_from_core_api(org_id):
    return get_core_api_data("organisations/" + org_id, "")


def get_job_by_id_from_core_api(job_id):
    return get_core_api_data("jobs/" + job_id, "")


def add_activity_to_organisation(org_id):
    payload = {"event_date": get_today_date(),
               "responsible_user_id": get_user_id_from_core_api(),
               "responsible_team_id": get_team_id_from_core_api(),
               "type": "email_sent",
               "client_contact_id": get_client_id_from_core_api()}
    url = organisations_url + org_id + "/activity"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202, f"Response {res.json()}"


def add_alert_to_organisation(org_id):
    payload = {"type": "caution",
               "reason": random_string(10),
               "expiry_date": get_today_date()}
    url = organisations_url + org_id + "/alert"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202, f"Response {res.json()}"


def add_location_to_organisation(org_id):
    payload = {"name": random_string(10),
               "country": "ALB",
               "city_id": "00000000-0000-0000-0000-000000000000",
               "other_city": get_random_city(),
               "is_primary": False,
               "address_line_1": random_string(10),
               "address_line_2": random_string(10),
               "address_line_3": random_string(10),
               "province": random_string(10),
               "postcode": "",
               "contacts": []}
    url = organisations_url + org_id + "/location"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202, f"Response {res.json()}"


def add_activity_to_client(client_id):
    payload = {"event_date": get_today_date(),
               "responsible_user_id": get_user_id_from_core_api(),
               "responsible_team_id": get_team_id_from_core_api(),
               "type": "client_call",
               "organisation_id": get_organisation_id_from_core_api(get_location_id_from_core_api())}
    url = clients_url + client_id + "/activity"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202, f"Response {res.json()}"


def add_alert_to_client(client_id):
    payload = {"type": "caution",
               "reason": random_string(10),
               "expiry_date": get_today_date()}
    url = clients_url + client_id + "/alert"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202, f"Response {res.json()}"


def add_review_to_client(client_id):
    payload = {"client_id": client_id,
               "review_date": get_today_date(),
               "responsible_user_id": get_user_id_from_core_api(),
               "responsible_team_id": get_team_id_from_core_api(),
               "notes": random_string(10)}
    url = clients_url + "review"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202, f"Response {res.json()}"


def add_activity_to_candidate(candidate_id):
    payload = {
        "event_date": "2024-08-09",
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "type": "candidate_call"
    }
    url = candidates_url + candidate_id + "/activity"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202, f"Response {res.json()}"
    return res.json()['id']


def get_activity_for_candidate(candidate_id):
    res = requests.get(base_url + "activities?filter[candidate][$eq]=" + candidate_id, headers=headers)
    assert res.status_code == 200
    return res


def get_activity_for_client(client_id):
    res = requests.get(base_url + "activities?filter[clients][$contains]=" + client_id, headers=headers)
    assert res.status_code == 202, f"Response: {res.json()}"
    return res


def add_activity_to_job(job_id):
    payload = {
        "event_date": get_today_date(),
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "type": "email_sent",
        "organisation_id": get_organisation_id_from_core_api(get_location_id_from_core_api())}
    url = jobs_url + job_id + "/activity"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202, f"Response {res.json()}"


def add_alert_to_job(job_id):
    payload = {
        "type": "caution",
        "reason": random_string(10),
        "expiry_date": get_today_date()}
    url = jobs_url + job_id + "/alert"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202, f"Response {res.json()}"


def add_candidate_to_job(candidate_id, job_id):
    payload = {"type": "longlist",
               "candidate_ids": [candidate_id],
               "responsible_user_id": get_user_id_from_core_api(),
               "responsible_team_id": get_team_id_from_core_api()}
    url = jobs_url + job_id + "/activity/application"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202, f"Response {res.json()}"


def add_contact_to_candidate(candidate_id):
    payload = {
        "value": "www.test.coms",
        "type": "url",
        "is_primary": True,
        "created_at": "2024-08-09T11:29:27.485Z"
    }
    url = candidates_url + candidate_id + "/contacts"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202


def get_contacts_for_candidate(candidate_id):
    res = requests.get(base_url + "candidate/contacts?filter[candidate][$eq]=" + candidate_id, headers=headers)
    assert res.status_code == 200
    return res


def add_alert_to_candidate(candidate_id):
    payload = {
        "type": "caution",
        "reason": "test alert",
        "expiry_date": get_today_date()
    }
    url = candidates_url + candidate_id + "/alert"
    res = requests.post(url, json=payload, headers=headers)
    assert res.status_code == 202


def get_alerts_for_candidate(candidate_id):
    res = requests.get(base_url + "candidate/alert?filter[candidate][$eq]=" + candidate_id, headers=headers)
    assert res.status_code == 200
    return res


def add_suitability_industry_to_candidate(candidate_id):
    payload = {"industries": [{"industry": "Education", "type": "Private"}]}
    res = requests.patch(candidates_url + candidate_id, json=payload, headers=headers)
    assert res.status_code == 202
    return res


def add_suitability_language_to_candidate(candidate_id):
    payload = {"languages": [{"language": "zho", "level": "Basic"}, {"language": "abk", "level": "Basic"}]}
    res = requests.patch(candidates_url + candidate_id, json=payload, headers=headers)
    assert res.status_code == 202
    return res


def add_suitability_location_to_candidate(candidate_id):
    payload = {"locations": [{"country": "Romania", "region": "Bucharest", "city": "Bucharest", "city_area": "center"}]}
    res = requests.patch(candidates_url + candidate_id, json=payload, headers=headers)
    assert res.status_code == 202
    return res


def add_qualification_to_candidate(candidate_id):
    payload = {
        "name": get_random_qualification(),
        "institution": get_random_organisation(),
        "date_issued": get_today_date(),
        "grade": "A2",
        "created_at": get_today_date() + "T00:00:00.000Z"
    }
    res = requests.post(candidates_url + candidate_id + "/qualifications", json=payload, headers=headers)
    assert res.status_code == 202, f"Response: {res.status_code}{res.json()}"


def add_review_to_candidate(candidate_id):
    payload = {
        "candidate_id": candidate_id,
        "review_date": get_today_date(),
        "review_completed": False,
        "responsible_user_id": get_user_id_from_core_api(),
        "responsible_team_id": get_team_id_from_core_api(),
        "notes": random_string(40)}
    res = requests.post(candidates_url + "review", json=payload, headers=headers)
    assert res.status_code in [409, 202], f"Response: {res.status_code} {res.json()}"


def add_interview_notes_to_candidate(candidate_id):
    payload = {
        "background_information": random_string(50),
        "traits_skills": random_string(50),
        "people_skills": random_string(50),
        "language_skills": random_string(50),
        "work_education_description": random_string(50),
        "salary_availability_description": random_string(50),
        "desired_jobs_description": random_string(50),
        "candidate_national_id": candidate_id,
        "responsible_user_id": get_user_id_from_core_api()
    }
    res = requests.put(candidates_url + "v2/interview-notes", json=payload, headers=headers)
    assert res.status_code == 200


def add_contract_to_organisation(org_id):
    payload = (
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"name\"\r\n\r\n{random_string(10)}\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"organisation\"\r\n\r\n{org_id}\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"document_type\"\r\n\r\nTERMS_OF_BUSINESS_PSA\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"contract_type_role\"\r\n\r\nsingle_role\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"contract_type_terms\"\r\n\r\nclient_terms\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"responsible_user\"\r\n\r\n{get_user_id_from_core_api()}\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"responsible_team\"\r\n\r\n{get_team_id_from_core_api()}\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"start_date\"\r\n\r\n2030-08-29\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"end_date\"\r\n\r\n2030-08-30\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"is_valid_until_terminated\"\r\n\r\nfalse\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"non_solicitation_note\"\r\n\r\n\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"portal_note\"\r\n\r\n\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"rules_of_engagement_note\"\r\n\r\n\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"fees[]\"\r\n\r\n{{\"country\": \"GBR\", \"roles\": []}}\r\n"
        f"--{boundary}--\r\n"
    )
    response = requests.post(contracts_url, data=payload, headers=multipart_headers)
    assert response.status_code == 201, f"Response: {response.json()}"


def get_contract_by_org_id(org_id):
    url = base_url + "terms-conditions/contracts?filter[organisation][id][$eq]=" + org_id
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Response: {response.json()}"
    return response


def get_email_id_core_api():
    url = base_url + "activities?populator=email&filter[email][id][$exists]=true"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Response: {response.json()}"
    return response.json()['results'][0]['email_id']


def get_meeting_id_core_api():
    url = base_url + "activities?filter[meeting_id][$ne]=null&filter[type][$eq]=candidate_call"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Response: {response.json()}"
    return response.json()['results'][0]['meeting_id']


def get_fee_id_from_core_api():
    url = base_url + "fees/"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Response: {response.json()}"
    return response.json()['results'][0]['id']


def get_1000_organisation_ids(entity):
    url = base_url + entity + "?limit=100"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Response: {response.status_code}"
    ids = [record['id'] for record in response.json()['results']]
    return ids
