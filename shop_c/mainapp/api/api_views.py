# from collections import OrderedDict

# from rest_framework.response import Response
# from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
# from rest_framework.filters import SearchFilter
# from rest_framework.pagination import PageNumberPagination
# from .serializers import CategorySerializers, CustomerSerializer, SweatshirtSerializer, HoodieSerializer, T_shirtSerializer, HeaddressSerializer, ShoeSerializer, CoverSerializer
# from ..models import Category, Customer, Sweatshirt, Hoodie, T_shirt, Headdress, Shoe, Cover


# class CategoryPagination(PageNumberPagination):

#     page_size = 2
#     page_query_param = 'page_size'
#     max_page_size = 10

#     def get_paginated_response(self, data):
#         return Response(OrderedDict([
#             ('objects_count', self.page.paginator.count),
#             ('next', self.get_next_link()),
#             ('previous', self.get_previous_link()),
#             ('item', data)
#         ]))

# class CategoryAPIView(ListCreateAPIView, RetrieveUpdateAPIView):

#     serializer_class = CategorySerializers
#     pagination_class = CategoryPagination
#     queryset = Category.objects.all()
#     lookup_field = 'id'


# class SweatshirtListAPIView(ListAPIView):
#     serializer_class = SweatshirtSerializer
#     queryset = Sweatshirt.objects.all()
#     filter_backends = [SearchFilter]
#     search_fields = ['price', 'title']


# class HoodieListAPIView(ListAPIView):
#     serializer_class = HoodieSerializer
#     queryset = Hoodie.objects.all()
#     filter_backends = [SearchFilter]
#     search_fields = ['price', 'title']


# class T_shirtListAPIView(ListAPIView):
#     serializer_class = T_shirtSerializer
#     queryset = T_shirt.objects.all()
#     filter_backends = [SearchFilter]
#     search_fields = ['price', 'title']        


# class HeaddressListAPIView(ListAPIView):
#     serializer_class = HeaddressSerializer
#     queryset = Headdress.objects.all()
#     filter_backends = [SearchFilter]
#     search_fields = ['price', 'title']


# class ShoeListAPIView(ListAPIView):
#     serializer_class = ShoeSerializer
#     queryset = Shoe.objects.all()
#     filter_backends = [SearchFilter]
#     search_fields = ['price', 'title']


# class CoverListAPIView(ListAPIView):
#     serializer_class = CoverSerializer
#     queryset = Cover.objects.all()
#     filter_backends = [SearchFilter]
#     search_fields = ['price', 'title']


# class SweatshirtDetailAPIView(RetrieveAPIView):

#     serializer_class = SweatshirtSerializer
#     queryset = Sweatshirt.objects.all()
#     lookup_field = 'id'


# class CustomerListAPIView(ListAPIView):

#     serializer_class = CustomerSerializer
#     queryset = Customer.objects.all()