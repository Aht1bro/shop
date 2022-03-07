# from django.contrib.contenttypes import fields
# from rest_framework import serializers

# from ..models import Category,Customer, Order, Sweatshirt, Hoodie, T_shirt, Headdress, Shoe, Cover

# class CategorySerializers(serializers.ModelSerializer):

#     name = serializers.CharField(required=True)
#     slug = serializers.SlugField()

#     class Meta:
#         model = Category
#         fields = [
#             'id', 'name', 'slug'
#         ]


# class BaseProductSerializer:
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
#     title = serializers.CharField(required=True)
#     slug = serializers.SlugField(required=True)
#     image = serializers.ImageField(required=True)
#     description = serializers.CharField(required=False)
#     price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)            


# class SweatshirtSerializer(BaseProductSerializer, serializers.ModelSerializer):

#     class Meta:
#         model = Sweatshirt
#         fields = '__all__'


# class HoodieSerializer(BaseProductSerializer, serializers.ModelSerializer):

#     class Meta:
#         model = Hoodie
#         fields = '__all__'        


# class T_shirtSerializer(BaseProductSerializer, serializers.ModelSerializer):

#     class Meta:
#         model = T_shirt
#         fields = '__all__'        


# class HeaddressSerializer(BaseProductSerializer, serializers.ModelSerializer):

#     class Meta:
#         model = Headdress
#         fields = '__all__'        


# class ShoeSerializer(BaseProductSerializer, serializers.ModelSerializer):

#     class Meta:
#         model = Shoe
#         fields = '__all__'        


# class CoverSerializer(BaseProductSerializer, serializers.ModelSerializer):

#     class Meta:
#         model = Cover
#         fields = '__all__'        

# class OrderSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Order
#         fields = '__all__'        


# class CustomerSerializer(serializers.ModelSerializer):

#     orders = OrderSerializer(many=True)

#     class Meta:
#         model = Customer
#         fields = '__all__'        

