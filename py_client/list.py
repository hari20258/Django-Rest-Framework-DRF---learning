import requests
endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.get(endpoint)

print(get_response.json()) 

#in the same url we can list and also create just by changing the method (POST and Get)