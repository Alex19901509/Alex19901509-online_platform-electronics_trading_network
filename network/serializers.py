from rest_framework import serializers
from .models import Supplier, Product, NetworkNode


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('debt', None)  # Удаляем задолженность из обновляемых данных
        return super().update(instance, validated_data)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = '__all__'
