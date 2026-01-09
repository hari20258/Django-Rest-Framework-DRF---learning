from rest_framework.viewsets import ModelViewSet
from .model import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    """
    A viewset is a class that groups all the CRUD operations of a model into one. While function based views are more hectic to code. And then the GenericViewAPI's reduces it, we still write classes for different operations with multiple urls.. But ViewSets simplies it even more.
    ModelViewSet is a ready-made ViewSet that includes: list, retrieve, create,etc. Internally, it uses Mixins and GenericAPIView.
    
    Methods -> function calls
    get -> list of items -> queryset
    get -> retrieve an items -> Product instance detail view.
    post -> create new item
    put -> to update item
    patch -> partial update
    delete -> to destory
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default