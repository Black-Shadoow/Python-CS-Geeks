import requests

endpoint = "http://127.0.0.1:8000/car/list"
response = requests.get(endpoint)

print(response.status_code)
print(response.json())
print(response.status_code)