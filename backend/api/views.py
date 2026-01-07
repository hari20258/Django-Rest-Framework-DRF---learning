import json
from django.form.models import model_to_dict #this is a function that takes a model instance and returns a python dictionary
from product.models import Productm
from django.http import JsonResponse, HttpResponse #Json Response takes a dictionary as an argument and returns a JSON response. But a HTTPSResponse expects a string as an argument.
# The JsonResponse is a Django class, it simplifies the process of creating a JSON response, it also sets the content type to application/json. Because in client side while using HttpResponse it will not set the content type to application/json and be as string, so we need to manually convert the data types to JSON fro every field in the dictionary.
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
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data: 
        data = model_to_dict(model_data, fields = ['id', 'title', 'price']) # we can choose which field we want to see/print or send to the client.
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        #In this we are taking a model instance and truning it into a python dictionary. And then we are sending it as a JSON response to the client. This is normal.
    return JsonResponse(data)


