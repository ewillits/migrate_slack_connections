# PagerDuty Testing
Python and PagerDuty API testing
- Utilizes requests module

## Required file/variables
- Requires an personal_secrets.py file that contains the following lines of code:
    - PROD_API = "Token token=SOURCE PERSONAL API KEY"
    - NEW_PROD_API = "Token token=TARGET PERSONAL API KEY"
- Update line 6 of get_slack_connections.py with the workspace id you wish to run the script on
- View the test_slack_data.csv file and copy/paste services, teams, and priority ids into the columns to perform the transform
- slack_connections.json is an example breakdown of the payload (used only for testing/display)

## Common Errors
- {'error': {'message': 'Not Found'}} - this indicates the connection could not be created by the API. This could be the output for two reasons:
    1. Connection to a private Slack channel - Slack admins will have to manually add the PagerDuty bot to the channel to complete the connection.
    2. Ghost Connection - the Slack channel no longer exists, but the configuration is still visible and stored in the PagerDuty UI.
