from rest_framework import serializers
from Apps.api.models import Product

class ProductSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    weight = serializers.IntegerField()
    price = serializers.FloatField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
