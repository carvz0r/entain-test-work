# Entain Test Work

## Project Overview

Automated tests for the web application using Playwright and Pytest with Allure reporting.

## Installation (Local)

1. Ensure Python 3.10+ is installed.
2. Clone the repository:

```
git clone <repo_url>
cd <repo_folder>
```

3. Create a virtual environment:

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

4. Install dependencies:

```
pip install -r requirements.txt
playwright install
```

## Running Tests Locally

```
pytest --headed  # run tests in headed mode
pytest  # run tests headless by default
```

## Running Tests via Docker

1. Build the image:

```
docker build -t tests-image .
```

2. Run the container:

```
docker run --rm tests-image
```

## Allure Reporting

1. Run tests with Allure results:

```
pytest --alluredir=allure-results
```

2. Generate or serve report:

```
allure serve allure-results
# or generate static report
allure generate allure-results -o allure-report
```

## Test Scenarios Covered

* Header navigation visibility
* Registration form negative validation
* Login with invalid credentials
* Language switching via UI
* Promotions page filtering and content validation

## Known Limitations

* Some pages or actions are blocked, preventing switching languages or refreshing/navigating pages from the test environment.
* Promotions page may not provide a full list of promotions
* Certain UI elements might be hidden or delayed, requiring manual waits

## Test Rationale

* Focused on critical paths that affect user interaction
* Negative tests for login and registration to validate form handling
* Language switch tests to ensure multi-locale support
* Promotions page to verify filtering and content display

## Future Improvements

* Add tests for additional pages
* Expand positive test cases for registration and login
* Add cross-browser testing