from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.response import Response
# Create your views here.
from django.contrib.auth.models import User
from . serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
from .models import Product, Review, Order, OrderedItem, ShippingAddress

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UsersTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        #data['username'] = self.user.username
        #data['email'] = self.user.email
        serializer = UserSerializerWithToken(self.user).data # We get more info such as isAdmin, token etc
        for x, y in serializer.items(): 
           data[x] = y
        return data
                                                    # TokenObtainPairSerializer autho get the current login user from
                                                    # TokenObtainPairView which autho provide login form
class UsersTokenObtainPairView(TokenObtainPairView): # When a user login(follow) this route we generate a refresh, an access token, username & email
    serializer_class = UsersTokenObtainPairSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user # current login user, this can now be access with a token
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def all_users(request):
    allusers = User.objects.all()
    serializer = UserSerializer(allusers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def index(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)