import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "jshfguolaojebbf"
USERNAME = "kristoferkoza"
GRAPHID = "graph1"
TODAY = dt.datetime.now().strftime("%Y%m%d")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

posting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
posting_config = {
    "date": "20230920",
    "quantity": "10.7",
}

requests.post(url=posting_endpoint, json=posting_config, headers=headers)
