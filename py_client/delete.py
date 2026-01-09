import requests

id = input("What is the id you want to delete?\n")
if id:
    try:
        id = int(id)
    except:
        print(f'{id} is not a valid id')

endpoint = f"http://127.0.0.1:8000/api/products/{id}/delete/"

get_response = requests.delete(endpoint)

print(get_response.status_code,get_response.status_code==204) #this is to check if the delete was successful or not. 