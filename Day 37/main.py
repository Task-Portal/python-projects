import datetime as dt

import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""
GRAPH_ID = ""
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url = pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)



# Post data to the Reader graph


create_data = {
    "date": dt.datetime.now().strftime("%Y%m%d"),
    "quantity": "3"
}

# response = requests.post(url=f"{graph_endpoint}/{GRAPH_ID}", json=create_data, headers=headers)
# print(response.text)

# update pixel
quantity ={
    "quantity":"12"
}
# response = requests.put(url=f"{graph_endpoint}/{GRAPH_ID}/{dt.datetime.now().strftime('%Y%m%d')}", json=quantity, headers=headers)
# print(response.text)

# delete pixel
# response = requests.delete(url=f"{graph_endpoint}/{GRAPH_ID}/{dt.datetime.now().strftime('%Y%m%d')}",  headers=headers)
# print(response.text)

