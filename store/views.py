from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from . serializers import ProductSerializer
from .models import Product, Review, Order, OrderedItem, ShippingAddress

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UsersTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['username'] = self.user.username
        data['email'] = self.user.email
        return data

class UsersTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsersTokenObtainPairSerializer


@api_view(['GET'])
def index(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)