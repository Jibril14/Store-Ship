from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Review, Order, OrderedItem, ShippingAddress


class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        #serializer = ReviewSerializer(reviews, many=True)
        #return serializer.data
