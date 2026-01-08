from rest_framework import serializers
from .models import Product
#one of the use of the serializers is to add custom fields to the model, and also turn JSON data to python dictionary and python dictionary to JSON data.
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount' #this is the custom field name we want to use.
        ]
    def get_my_discount(self, obj): #i
        if not hasattr(obj, 'discount'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.discount() #this is a instance method thats why we use ()
#here we are adding a custom field to the model serializer called discount but it is not a field in the model. so we need to define it in the serializer, by creating a function. But this needs to satrt with get_ as it is a method field.
   
