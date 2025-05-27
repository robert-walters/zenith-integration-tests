export ENV=stage
pytest -v -s --alluredir=allure-results
allure serve allure-results