from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Carlist, Review, Showroom  # or ..models if inside subfolder


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Carlist
        fields = '__all__'

    def get_discount_price(self, obj):
        return max(obj.price - 500, 0)

    def get_reviews(self, obj):
        reviews = Review.objects.filter(car=obj)
        return ReviewSerializer(reviews, many=True).data

    def validate_price(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be greater than 20000.00")
        return value

    def validate(self, data):
        if data.get('name') == data.get('desc'):
            raise serializers.ValidationError("Name and description must be different.")
        return data


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = '__all__'
