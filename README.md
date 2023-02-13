# PagerDuty Testing
Python and PagerDuty API testing
- Utilizes requests module

## Required file/variables
- Requires an personal_secrets.py file that contains the following lines of code:
    - PROD_API = "Token token=SOURCE FULL ACCESS KEY"
    - NEW_PROD_API = "Token token=TARGET PERSONAL ACCESS KEY"
- View the test_slack_data.csv file and copy/paste services, teams, and priority ids into the columns to perform the transform
- slack_connections.json is an example breakdown of the payload (used only for testing/display)
