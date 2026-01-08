import json
from django.forms.models import model_to_dict #this is a function that takes a model instance and returns a python dictionary
from product.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer
#from django.http import JsonResponse, HttpResponse #Json Response takes a dictionary as an argument and returns a JSON response. But a HTTPSResponse expects a string as an argument.
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
@api_view(["POST"]) #this is a decorator that takes a list of HTTP methods as an argument and returns a function that can handle those methods. Instead of writing if request.method == "GET" or request.method == "POST" we can use this decorator.
def api_home(request, *args, **kwargs): #decorators (like @api_view) act as "wrappers" that modify the specific function or class defined immediately after them. They are essentially syntax sugar for function = decorator(function). When you put the docstring between the decorator and the function definition, it breaks the connection:
    """
    This is a DRF API view.
    """
    #data = request.data 
    #retrun Response(data) # these two line just returns the data back to the client.
    #Here we are validating the data instead of just sending the data back to the client.
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        #data = serializer.save() # we can save the data to an variable and use it later, here serializer.save() which is data is a model instance.
        # So this line creates an instance.
        print("Valid Data",serializer.data)
        return Response(serializer.data)
    else:
        print("Invalid Data",serializer.data)
        return Response(serializer.errors)
    #The below are the old methods we used before for instance(serialization)
    #model_data was the variable we used before instance(serialization)
    # instances = Product.objects.all().order_by('?').first()
    # data = {}
    # if instances: 
    #     #data = model_to_dict(instances, fields = ['id', 'title', 'price', 'sale_price']) # we can choose which field we want to see/print or send to the client.
    #     #The sale price is not shown up by default in model_data as its a property. This is why we need to use model seralizers.
    #     data = ProductSerializer(instances).data # ProductSerializer(instances) makes it a class of that instance and .data is a property that returns the serialized data anc .data is the data passed through that instance.
    # return Response(data)
    # data['id'] = model_data.id
    # data['title'] = model_data.title
    # data['content'] = model_data.content
    # data['price'] = model_data.price
        #In this we are taking a model instance and truning it into a python dictionary. And then we are sending it as a JSON response to the client. This is normal.
    #return JsonRespone(data)


