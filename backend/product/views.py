from django.shortcuts import render
from rest_framework import generics, mixins # here we are emoving permissions and authentication because we are using a mixin.
from . models import Product
from . serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# from . permissions import IsStaffEditorPermission -> we dont need this anymore becasue we are using a mixin.
# from .. api.authentication import TokenAuthentication -> we dont need this anymore becasue we are using a mixin.
from api.mixins import StaffEditorPermissionMixin


class ProductDetailAPIView(generics.RetrieveAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all() #this is the queryset we want to use.
    serializer_class = ProductSerializer #this is the serializer we want to use.
    lookup_field = 'pk' #this is the lookup field we see in the queryset.

class ProductCreateAPIView(generics.CreateAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save()
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content == None:
            content = "Beeeeyaaacchchh"
        return serializer.save(content=content)

# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# we dont have to use this because we can just modify the create view itself to Create and List.

class ProductListCreateAPIView(generics.ListCreateAPIView, StaffEditorPermissionMixin): #this is a class based view that handles both list and create.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsStaffEditorPermission] we dont need this anymore because we are using a mixin. #this permission allows me to read the data but not post.
    # authentication_classes  = [              # we dont need this anymore because we have it in settings.
    #     authentication.SessionAuthentication,
    #     TokenAuthentication
    # ]
    
    def perform_create(self, serializer): # this is a function based view that handles the create operation.
        print(serializer.validated_data)
        serializer.save()
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content == None:
            content = "Beeeeyaaacchchh"
        return serializer.save(content=content)

class ProductUpdateAPIView(generics.UpdateAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDeleteAPIView(generics.DestroyAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        queryse = Product.objects.all()
        super().perform_destroy(instance)

product_list_create_view = ProductListCreateAPIView.as_view()
# product_list_view = ProductListAPIView.as_view()
product_detail_view = ProductDetailAPIView.as_view()
product_create_view = ProductCreateAPIView.as_view()
product_update_view = ProductUpdateAPIView.as_view()
product_delete_view = ProductDeleteAPIView.as_view()

class ProductMixinView( # This is a class based view that is gonna do something similar to the product_alt_view function based view. #->In the function based view we are using the if else condition to check if the request method is GET or POST. Like we need to write it fro every method. In class based view we write functions (which are methods of the class).
    #But in the class based view we can use the get method to handle the GET request. and so on.
    mixins.ListModelMixin, # -> this makes the list view, this makes us write the code similar to the generic view api.
    mixins.CreateModelMixin,
    generics.GenericAPIView): 
    queryset = Product.objects.all() # these are the attributes of the generic view api. Not mixin.
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        return self.list(request, *args, **kwargs) #-> list method is coming from mixin module. Now if i want to post it instead of get, i can just change the get to post and nothing else.
    # def post(self, request, *args, **kwargs):  
    #     return self.list(request, *args, **kwargs)
#custom function based view for create and list and retrive.
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
@api_view(["GET","POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET": #we can use this to list the products based on the pk value. If the input parameters has pk value it is retiveAPI else it is listAPI.
        if 'pk' is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        #list all
        queryset = Product.objects.all()# this is list all view
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method =="POST": # this is a function based view that handles the create operation.
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content == None:
                content = "Beeeeyaaacchchh"
            return Response(serializer.data)
        print("Invalid Data",serializer.data)
        return Response(serializer.errors)