import requests
endpoint = "http://127.0.0.1:8000/api/products/1/update/"

data = {
    "title": "Updated Title",
    "content": "Updated Content",
    "price": 12
}
get_response = requests.put(endpoint, json=data)

print(get_response.json()) 