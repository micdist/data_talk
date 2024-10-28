import requests

url = 'http://localhost:9696/predict'
customer = {"job": "management", "duration": 400, "poutcome": "success"}
response = requests.post(url, json=customer).json()

keys = (list(response.keys()))
print(f'{keys[0]} {response.get(keys[0])} \n{keys[1]} {response.get(keys[1]):.3f}')