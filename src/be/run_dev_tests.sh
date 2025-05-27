export ENV=dev
pytest -v -s --alluredir=allure-results
allure serve allure-results