import requests 

#endpoint = "http://httpbin.org/anything"# this ecohes whatever what i send to it
#endpoint = "http://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"
#requests.get() #Application programming interface (request library is a form of API) but a library api is not a form of api
# REST API is a form of API (a web API)

# get_response = requests.get(endpoint) -> this gives us a response object
get_response = requests.get(endpoint, params={"abc":123},json={"query": "hello"}) #-> we can pass our own json data to the api.
#params is used to pass query parameters (basicially params are the query parameters which we see in url after ?, ex: http://127.0.0.1:8000/api/?abc=123)
#print(get_response.text)
print(get_response.json()) # this gives us a actual python dictionary.


# HTTPS request gives us the raw form which is the HTML
# While a REST API HTTP request gives us the data in JSON, which is usable.
#JSON -> Javascipt Object Notation is almost a python dictionary.