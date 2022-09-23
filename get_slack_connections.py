import requests
import json
import csv
import personal_secrets

url = "https://app.pagerduty.com/integration-slack/workspaces/T021UQ5QY3U/connections"
# Add "include[]":"integrations" to querystring for integration information
querystring = {"limit": "5", "offset": 0}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Authorization": personal_secrets.PROD_API,
}

# Looping through API calls and offsetting until false
list_of_slack_connections = []
while True:
    response = requests.request("GET", url, headers=headers, params=querystring)
    list_of_slack_connections.extend(response.json()["slack_connections"])
    if response.json()["more"] is False:
        break
    querystring["offset"] += 5

# CSV reader - loops through list of slack connections and data in csv to replace source and priority values
with open("test_slack_data.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for each_row in reader:
        for each_slack_connection in list_of_slack_connections:
            if each_slack_connection["source_id"] == each_row["old"]:
                each_slack_connection["source_id"] = each_row["new"]
            if each_slack_connection["config"]["priorities"] is None:
                continue
            else:
                for i in range(len(each_slack_connection["config"]["priorities"])):
                    if each_slack_connection["config"]["priorities"][i] == each_row["old"]:
                        each_slack_connection["config"]["priorities"][i] = each_row["new"]


# Modify list by adding a new dictionary with value matching POST request
modified_list = []
for each_extracted_connection in list_of_slack_connections:
    modified_list.append({"slack_connection": each_extracted_connection})

# Serializing and writing to slack_connections.json - used for testing display only
json_object = json.dumps(modified_list, indent=4)
with open("slack_connections.json", "w") as outfile:
    outfile.write(json_object)

# Post the changed slack connection with new source/priority values - new headers
modified_headers = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Authorization": personal_secrets.NEW_PROD_API,
}
for each_modified_connection in modified_list:
    #print(each_modified_connection)
    post_response = requests.request("POST", url, json=each_modified_connection, headers=modified_headers)
    print(post_response.json())