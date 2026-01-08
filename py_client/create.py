import requests
endpoint = "http://127.0.0.1:8000/api/products/"

data={"title": "Apple iPhone 13","content": " ","price": "10000000"}

get_response = requests.post(endpoint, json=data)

print(get_response.json()) 