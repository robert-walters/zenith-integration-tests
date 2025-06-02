Zenith Backend Automation Tests (Pytest)

This project contains backend Integrations API tests for the Zenith platform, written in Python using Pytest.

------------------------------------------------------------
Prerequisites:
- Python 3.6 or higher
- pip (Python package installer)

------------------------------------------------------------
Setup Instructions:

1. Clone the repository:
   git clone https://github.com/robert-walters/zenith-integration-tests.git
   cd zenith-integration-tests

2. Create and activate a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate       # On Windows: .venv\Scripts\activate

3. Install dependencies:
   pip install -r src/be/requirements.txt

------------------------------------------------------------
Project Structure:

src/
├── be/
│   ├── configuration/        -> environment config files
│   ├── tests/                -> test cases organized by endpoint
│   ├── utilities/            -> helper functions, logger, etc.
│   ├── pytest.ini            -> pytest configuration
│   ├── requirements.txt      -> dependencies for BE tests
│   ├── run_dev_tests.sh      -> shell script to run all tests on dev environment
│   └── run_stage_tests.sh    -> shell script to run all tests on stage environment
├── .gitignore
└── README.md

------------------------------------------------------------
Running Tests:

Before running tests, set the environment variable `ENV` to specify the target environment (e.g. dev, stage).

Example:
   export ENV=dev

Run all tests with:
   pytest --alluredir=allure-results

Generate an Allure report from the results:
   allure generate --clean -o report allure-results

Open the generated report:
   allure open report

------------------------------------------------------------
Guidelines for Writing Tests:

- Place test cases under src/be/tests/
- Use src/be/utilities/ for reusable functions
- Follow Pytest naming conventions (e.g. test_*.py, functions starting with test_)

------------------------------------------------------------

~ Thank you ~
