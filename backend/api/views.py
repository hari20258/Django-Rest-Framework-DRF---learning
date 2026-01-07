from django.shortcuts import render
import json
from django.http import JsonResponse

# def api_home(request, *args, **kwargs):
#     #request -> HttpRequest -> Django not python request
#     #JSON data is from the request.body
#     body = request.body #byte string of JSON data - to change this to a python dictionary we use json.loads() from the json package
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)
