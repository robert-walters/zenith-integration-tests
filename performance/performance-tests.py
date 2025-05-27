import random
import time

import gevent
from locust import TaskSet, task, between, FastHttpUser

from src.be.utilities.get_core_api_data import get_1000_organisation_ids
from src.performance.requests import DeleteClientRequests, PostClientRequests, PutClientRequests, GetClientRequests, \
    DeleteCandidateRequests, PostCandidateRequests, PutCandidateRequests, GetCandidateRequests, GetJobsRequests, \
    PostJobsRequests, PutJobsRequests, DeleteJobsRequests, GetOrganisationsRequests, PostOrganisationsRequests, \
    PutOrganisationsRequests, DeleteOrganisationsRequests, GetActivitiesRequests, PostActivitiesRequests, \
    PutActivitiesRequests, DeleteActivitiesRequests, GetActivitiesByEntityIdRequests, GetActivitiesWithFiltersRequests

interval = 120
priority1 = 100
priority2 = 10
s_time = time.time()  # Track the start time of the test
candidate_order = 3
client_order = 2
job_order = 6
org_order = 4
activities_order = 5
filtered_activity_order = 1


class CandidatesRequests(TaskSet):

    @task(priority1)
    def execute_get_candidate_requests(self):
        current_time = time.time()
        if interval * (candidate_order - 1) < current_time - s_time < interval * candidate_order:
            candidate_task = GetCandidateRequests(self.parent)
            candidate_task.get_candidates()

    @task(priority2)
    def execute_put_candidate_requests(self):
        current_time = time.time()
        if interval * (candidate_order - 1) < current_time - s_time < interval * candidate_order:
            candidate_task = PutCandidateRequests(self.parent)
            candidate_task.put_candidates()

    @task(priority2)
    def execute_post_candidate_requests(self):
        current_time = time.time()
        if interval * (candidate_order - 1) < current_time - s_time < interval * candidate_order:
            candidate_task = PostCandidateRequests(self.parent)
            candidate_task.post_candidates()

    @task(priority2)
    def execute_delete_candidate_requests(self):
        current_time = time.time()
        if interval * (candidate_order - 1) < current_time - s_time < interval * candidate_order:
            candidate_task = DeleteCandidateRequests(self.parent)
            candidate_task.delete_candidates()


class ClientsRequests(TaskSet):
    @task(priority1)
    def execute_get_client_requests(self):
        current_time = time.time()
        if interval * (client_order - 1) < current_time - s_time < interval * client_order:
            client_task = GetClientRequests(self.parent)
            client_task.get_clients()

    @task(priority2)
    def execute_put_client_requests(self):
        current_time = time.time()
        if interval * (client_order - 1) < current_time - s_time < interval * client_order:
            client_task = PutClientRequests(self.parent)
            client_task.put_clients()

    @task(priority2)
    def execute_post_client_requests(self):
        current_time = time.time()
        if interval * (client_order - 1) < current_time - s_time < interval * client_order:
            client_task = PostClientRequests(self.parent)
            client_task.post_clients()

    @task(priority2)
    def execute_delete_client_requests(self):
        current_time = time.time()
        if interval * (client_order - 1) < current_time - s_time < interval * client_order:
            client_task = DeleteClientRequests(self.parent)
            client_task.delete_clients()


class JobsRequests(TaskSet):
    @task(priority1)
    def execute_get_jobs_requests(self):
        current_time = time.time()
        if interval * (job_order - 1) < current_time - s_time < interval * job_order:
            job_task = GetJobsRequests(self.parent)
            job_task.get_jobs()

    @task(priority2)
    def execute_post_jobs_requests(self):
        current_time = time.time()
        if interval * (job_order - 1) < current_time - s_time < interval * job_order:
            job_task = PostJobsRequests(self.parent)
            job_task.post_jobs()

    @task(priority2)
    def execute_put_jobs_requests(self):
        current_time = time.time()
        if interval * (job_order - 1) < current_time - s_time < interval * job_order:
            job_task = PutJobsRequests(self.parent)
            job_task.put_jobs()

    @task(priority2)
    def execute_delete_jobs_requests(self):
        current_time = time.time()
        if interval * (job_order - 1) < current_time - s_time < interval * job_order:
            job_task = DeleteJobsRequests(self.parent)
            job_task.delete_jobs()


class OrganisationsRequests(TaskSet):
    @task(priority1)
    def execute_get_organisations_requests(self):
        current_time = time.time()
        if interval * (org_order - 1) < current_time - s_time < interval * org_order:
            org_task = GetOrganisationsRequests(self.parent)
            org_task.get_organisations()

    @task(priority2)
    def execute_post_organisations_requests(self):
        current_time = time.time()
        if interval * (org_order - 1) < current_time - s_time < interval * org_order:
            org_task = PostOrganisationsRequests(self.parent)
            org_task.post_organisations()

    @task(priority2)
    def execute_put_organisations_requests(self):
        current_time = time.time()
        if interval * (org_order - 1) < current_time - s_time < interval * org_order:
            org_task = PutOrganisationsRequests(self.parent)
            org_task.put_organisations()

    @task(priority2)
    def execute_delete_organisations_requests(self):
        current_time = time.time()
        if interval * (org_order - 1) < current_time - s_time < interval * org_order:
            org_task = DeleteOrganisationsRequests(self.parent)
            org_task.delete_organisations()


class ActivitiesRequests(TaskSet):
    @task(priority1)
    def execute_get_activities_requests(self):
        current_time = time.time()
        if interval * (activities_order - 1) < current_time - s_time < interval * activities_order:
            act_task = GetActivitiesRequests(self.parent)
            act_task.get_activities()

    @task(priority2)
    def execute_post_activities_requests(self):
        current_time = time.time()
        if interval * (activities_order - 1) < current_time - s_time < interval * activities_order:
            act_task = PostActivitiesRequests(self.parent)
            act_task.post_activities()

    @task(priority2)
    def execute_put_activities_requests(self):
        current_time = time.time()
        if interval * (activities_order - 1) < current_time - s_time < interval * activities_order:
            act_task = PutActivitiesRequests(self.parent)
            act_task.put_activities()

    @task(priority2)
    def execute_delete_activities_requests(self):
        current_time = time.time()
        if interval * (activities_order - 1) < current_time - s_time < interval * activities_order:
            act_task = DeleteActivitiesRequests(self.parent)
            act_task.delete_activities()


class ActivitiesWithFiltersRequests(TaskSet):
    @task(priority1)
    def execute_get_activities_with_filter0(self):
        current_time = time.time()
        ids = get_1000_organisation_ids("candidates")
        candidate_id = random.choice(ids)
        if interval * (filtered_activity_order - 1) < current_time - s_time < interval * filtered_activity_order:
            act_task = GetActivitiesByEntityIdRequests(self.parent)
            act_task.get_activities_with_filters("candidates_id__eq=", candidate_id)

    @task(priority1)
    def execute_get_activities_with_filter1(self):
        current_time = time.time()
        ids = get_1000_organisation_ids("organisations")
        org_id = random.choice(ids)
        if interval * (filtered_activity_order - 1) < current_time - s_time < interval * filtered_activity_order:
            act_task = GetActivitiesByEntityIdRequests(self.parent)
            act_task.get_activities_with_filters("organisation_id__eq=", org_id)

    @task(priority1)
    def execute_get_activities_with_filter2(self):
        current_time = time.time()
        if interval * (filtered_activity_order - 1) < current_time - s_time < interval * filtered_activity_order:
            act_task = GetActivitiesWithFiltersRequests(self.parent)
            act_task.get_activities_with_filters("record_origin__in=client__job__candidate")

    @task(priority1)
    def execute_get_activities_with_filter3(self):
        current_time = time.time()
        if interval * (filtered_activity_order - 1) < current_time - s_time < interval * filtered_activity_order:
            act_task = GetActivitiesWithFiltersRequests(self.parent)
            act_task.get_activities_with_filters("outcome__eq=event_did_not_happen")

    @task(priority1)
    def execute_get_activities_with_filter4(self):
        current_time = time.time()
        if interval * (filtered_activity_order - 1) < current_time - s_time < interval * filtered_activity_order:
            act_task = GetActivitiesWithFiltersRequests(self.parent)
            act_task.get_activities_with_filters("event_date__lte=2024-01-01")

    @task(priority1)
    def execute_get_activities_with_filter5(self):
        current_time = time.time()
        if interval * (filtered_activity_order - 1) < current_time - s_time < interval * filtered_activity_order:
            act_task = GetActivitiesWithFiltersRequests(self.parent)
            act_task.get_activities_with_filters("type__like=%call")

    @task(priority1)
    def execute_get_activities_with_filter6(self):
        current_time = time.time()
        if interval * (filtered_activity_order - 1) < current_time - s_time < interval * filtered_activity_order:
            act_task = GetActivitiesWithFiltersRequests(self.parent)
            act_task.get_activities_with_filters("created_at__lte=2024-01-01&created_at__gte=2023-01-01")


class MyUser(FastHttpUser):
    wait_time = between(0.2, 1)
    tasks = [CandidatesRequests, ClientsRequests, JobsRequests, OrganisationsRequests, ActivitiesRequests,
             ActivitiesWithFiltersRequests]
