from rest_framework import serializers
from ..models import Carlist

def alpanumeric(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("Only alpha numric charaters are required")
class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name= serializers.CharField()
    desc=serializers.CharField()
    status=serializers.BooleanField(read_only=True)
    vechile=serializers.CharField(validators=[alpanumeric])
    price=serializers.DecimalField(max_digits=9,decimal_places=2)

    def create(self, validated_data):
        return Carlist.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.desc=validated_data.get('desc', instance.desc)
        instance.active=validated_data.get('active', instance.active)  #instance mean previous data 
        instance.vehiclenum=validated_data.get('vehiclenum',instance.vehiclenum) 
        instance.price=validated_data.get('price',instance.price)
        instance.save()
        return instance
    
    def validate_price(self, value):  #field validators 
        if value<=20000.00:
            raise serializers.ValidationError("Price must be greater than 200000")
        return value
    
       # object level validation 
    def validate(self, data):
        if data['name'] == data['desc']:
            raise serializers.ValidationError("Name and description must be different.")
        return data