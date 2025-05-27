from locust import TaskSet
import threading
import time

from locust import TaskSet
from src.be.configuration.config_parser import get_token, get_config_value
from src.be.definitions.activity_definitions import get_activity_id
from src.be.definitions.candidates_definitions import get_candidate_id
from src.be.definitions.jobs_definitions import get_job_id
from src.be.definitions.organisations_definitions import get_organisation_id
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_activity_payload import \
    create_candidate_activity_original_full_payload, create_candidate_activity_full_payload
from src.be.utilities.candidates_utilities.request_payloads.create_candidate_payloads import \
    create_candidate_full_payload
from src.be.definitions.clients_definitions import get_client_id
from src.be.utilities.candidates_utilities.request_payloads.update_candidate_activity_payload import \
    update_candidate_activity_original_full_payload
from src.be.utilities.clients_utilities.request_payloads.create_client_payload import create_client_full_payload
from src.be.utilities.clients_utilities.request_payloads.update_client_payload import update_client_full_payload
from src.be.utilities.job_utilities.request_payloads.create_job_activity_payload import create_job_activity_full_payload
from src.be.utilities.job_utilities.request_payloads.create_job_payload import create_job_full_payload
from src.be.utilities.job_utilities.request_payloads.update_job_payload import update_job_full_payload
from src.be.utilities.organisations_utilities.request_payloads.create_organisation_payloads import \
    create_organisation_full_payload
from src.be.utilities.organisations_utilities.request_payloads.update_organisation_payloads import \
    update_organisation_full_payload
from typing import Final

from src.be.utilities.useful_functions import standard_headers, delete_headers

token = get_token()
base_url = get_config_value("base_url")
headers: Final = standard_headers()
delete_headers: Final = delete_headers()

candidate_id: Final = get_candidate_id()
client_id: Final = get_client_id(base_url, "clients/", headers)
job_id: Final = get_job_id(base_url, "jobs/", create_job_full_payload(), headers)
org_id: Final = get_organisation_id(base_url, "organisations/", create_organisation_full_payload(), headers)
act_id: Final = get_activity_id(base_url, "candidates/", candidate_id, create_candidate_activity_full_payload(),
                                headers)
lock = threading.Lock()
s_time = time.time()  # Track the start time of the test
requests_made = 0


class GetCandidateRequests(TaskSet):
    def get_candidates(self):
        with self.client.get(f"/integrations/api/v1/candidates/{candidate_id}", headers=headers,
                             name="Candidates", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class PutCandidateRequests(TaskSet):
    payload = create_candidate_full_payload()

    def put_candidates(self):
        with self.client.put(f"/integrations/api/v1/candidates/16011a2e-ff68-4259-bcbd-49408ea16388",
                             json=create_candidate_full_payload(), headers=headers, name="Candidates",
                             catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class PostCandidateRequests(TaskSet):
    def post_candidates(self):
        with self.client.post(f"/integrations/api/v1/candidates/",
                              json=create_candidate_full_payload(), headers=headers, name="Candidates",
                              catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class DeleteCandidateRequests(TaskSet):
    def delete_candidates(self):
        with self.client.delete(f"/integrations/api/v1/candidates/" + get_candidate_id(), headers=delete_headers,
                                name="Candidates", catch_response=True) as response:
            if response.status_code != 204:
                response.failure(f"Expected status code 204 but got {response.status_code}")
            else:
                response.success()


class GetClientRequests(TaskSet):
    def get_clients(self):
        with self.client.get(f"/integrations/api/v1/clients/" + client_id, headers=headers,
                             name="Clients", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class PutClientRequests(TaskSet):
    def put_clients(self):
        with self.client.put(f"/integrations/api/v1/clients/{client_id}", json=update_client_full_payload(),
                             headers=headers,
                             name="Clients", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class PostClientRequests(TaskSet):
    def post_clients(self):
        with self.client.post(f"/integrations/api/v1/clients/", json=create_client_full_payload(),
                              headers=headers,
                              name="Clients", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class DeleteClientRequests(TaskSet):
    def delete_clients(self):
        client = get_client_id(base_url, "clients/", headers)
        with self.client.delete(
                f"/integrations/api/v1/clients/{client}",
                headers=delete_headers, name="Clients", catch_response=True) as response:
            if response.status_code != 204:
                response.failure(f"Expected status code 204 but got {response.status_code}")
            else:
                response.success()


class PostJobsRequests(TaskSet):
    def post_jobs(self):
        with self.client.post(f"/integrations/api/v1/jobs/", json=create_job_full_payload(),
                              headers=headers,
                              name="Jobs", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class GetJobsRequests(TaskSet):
    def get_jobs(self):
        with self.client.get(f"/integrations/api/v1/jobs/" + job_id, headers=headers,
                             name="Jobs", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class PutJobsRequests(TaskSet):
    def put_jobs(self):
        with self.client.put(f"/integrations/api/v1/jobs/" + job_id, json=update_job_full_payload(),
                             headers=headers,
                             name="Jobs", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class DeleteJobsRequests(TaskSet):
    def delete_jobs(self):
        j_id = get_job_id(base_url, "jobs/", create_job_full_payload(), headers)
        with self.client.delete(f"/integrations/api/v1/jobs/" + j_id, headers=delete_headers,
                                name="Jobs", catch_response=True) as response:
            if response.status_code != 204:
                response.failure(f"Expected status code 204 but got {response.status_code}")
            else:
                response.success()


class PostOrganisationsRequests(TaskSet):
    def post_organisations(self):
        with self.client.post(f"/integrations/api/v1/organisations/", json=create_organisation_full_payload(),
                              headers=headers,
                              name="Organisations", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class GetOrganisationsRequests(TaskSet):
    def get_organisations(self):
        with self.client.get(f"/integrations/api/v1/organisations/" + org_id, headers=headers,
                             name="Organisations", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class PutOrganisationsRequests(TaskSet):
    def put_organisations(self):
        with self.client.put(f"/integrations/api/v1/organisations/" + org_id,
                             json=update_organisation_full_payload(),
                             headers=headers,
                             name="Organisations", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class DeleteOrganisationsRequests(TaskSet):
    def delete_organisations(self):
        organisation_id = get_job_id(base_url, "organisations/", create_organisation_full_payload(), headers)
        with self.client.delete(f"/integrations/api/v1/organisations/" + organisation_id, headers=delete_headers,
                                name="Organisations", catch_response=True) as response:
            if response.status_code != 204:
                response.failure(f"Expected status code 204 but got {response.status_code}")
            else:
                response.success()


class PostActivitiesRequests(TaskSet):
    def post_activities(self):
        with self.client.post(f"/integrations/api/v1/activities/",
                              json=create_candidate_activity_original_full_payload(candidate_id),
                              headers=headers,
                              name="Activities", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got "
                                 f"{response.status_code}\n{response.request.url}\n{response.request.body}")
            else:
                response.success()


class GetActivitiesRequests(TaskSet):
    def get_activities(self):
        with self.client.get(f"/integrations/api/v1/activities/" + act_id, headers=headers,
                             name="Activities", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class PutActivitiesRequests(TaskSet):
    def put_activities(self):
        with self.client.put(f"/integrations/api/v1/activities/" + act_id,
                             json=update_candidate_activity_original_full_payload(candidate_id), headers=headers,
                             name="Activities", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class DeleteActivitiesRequests(TaskSet):
    def delete_activities(self):
        j_id = get_job_id(base_url, "jobs/", create_job_full_payload(), headers)
        with self.client.delete(f"/integrations/api/v1/activities/" + get_activity_id(base_url, "jobs/", j_id,
                                                                                      create_job_activity_full_payload(),
                                                                                      headers), headers=delete_headers,
                                name="Activities", catch_response=True) as response:
            if response.status_code != 204:
                response.failure(f"Expected status code 204 but got {response.status_code}")
            else:
                response.success()


class GetActivitiesWithFiltersRequests(TaskSet):
    def get_activities_with_filters(self, custom_filter):
        with self.client.get(f"/integrations/api/v1/activities?" + custom_filter,
                             headers=headers, name="Activities->" + custom_filter, catch_response=True) as response:
            if response.status_code != 200:
                print(response.json())
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()


class GetActivitiesByEntityIdRequests(TaskSet):
    def get_activities_with_filters(self, custom_filter, entity_id):
        with self.client.get(f"/integrations/api/v1/activities?" + custom_filter + entity_id,
                             headers=headers, name="Activities->" + custom_filter, catch_response=True) as response:
            if response.status_code != 200:
                print(response.json())
                response.failure(f"Expected status code 200 but got {response.status_code}")
            else:
                response.success()
