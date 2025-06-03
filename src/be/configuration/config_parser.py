import os
from configparser import ConfigParser
import requests
import base64
from src.be.utilities.logger import logger

script_dir = os.path.dirname(os.path.abspath(__file__))


def get_config_value(value):
    default_env = 'stage'  # 'dev' or 'stage'
    file_name = f"{os.getenv('ENV', default_env)}-config.cfg" if os.getenv('ENV') in ['dev', 'stage'] else \
        f"{default_env}-config.cfg"
    config = ConfigParser()
    config_path = os.path.join(script_dir, file_name)
    config.read(config_path)
    return config.get("config_properties", value)


def get_token():
    remit = get_config_value("remit")
    username = get_config_value(f"{remit.lower()}_username")
    password = get_config_value(f"{remit.lower()}_password")
    payload = {
        "client_id": get_config_value("client_id"),
        "username": username,
        "password": password,
        "scope": get_config_value("scope") + " openid offline_access",
        "grant_type": "password"}

    client_id = get_config_value("client_id")
    secret_key = get_config_value("secret_key")
    encoded = base64.b64encode(f"{client_id}:{secret_key}".encode('utf-8')).decode('utf-8')
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + encoded}
    post_response = requests.post(get_config_value("auth_host") + "/oauth2/token", data=payload, headers=headers)
    logger.info("Running tests on " + str(os.getenv("ENV")) + " environment.")
    return "Bearer " + post_response.json()['access_token']


def assert_by_auth_type(response, config):
    """
    Assert the response status code based on the 'xapi' setting in config.
    Args:
        response: The HTTP response object with a status_code attribute.
        config: Dict-like object with 'xapi' key (expects 'on' or 'off').
    Raises:
        AssertionError if the response status code does not match expected.
    """
    xapi_setting = config.get("xapi")
    if xapi_setting == "on":
        expected_status = 403
    else:
        expected_status = 404
    assert response.status_code == expected_status, (
        f"Expected status {expected_status} for xapi='{xapi_setting}', "
        f"but got {response.status_code}"
    )

