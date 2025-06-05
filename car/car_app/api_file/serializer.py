from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name= serializers.CharField()
    desc=serializers.CharField()
    status=serializers.BooleanField(read_only=True)