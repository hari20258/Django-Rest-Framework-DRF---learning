from django.shortcuts import render
from rest_framework import generics
from . models import Product
from . serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() #this is the queryset we want to use.
    serializer_class = ProductSerializer #this is the serializer we want to use.
    lookup_field = 'pk' #this is the lookup field we see in the queryset.

class ProductCreateAPIView(generics.CreateAPIView):
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

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# we dont have to use this because we can just modify the create view itself to Create and List.

class ProductListCreateAPIView(generics.ListCreateAPIView): #this is a class based view that handles both list and create.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer): # this is a function based view that handles the create operation.
        print(serializer.validated_data)
        serializer.save()
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content == None:
            content = "Beeeeyaaacchchh"
        return serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()
product_list_view = ProductListAPIView.as_view()
product_detail_view = ProductDetailAPIView.as_view()
product_create_view = ProductCreateAPIView.as_view()

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