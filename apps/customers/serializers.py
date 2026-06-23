from rest_framework import serializers
from apps.customers.models import Customer


class RegisterCustomerSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    name = serializers.CharField()
    phone = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    house_number = serializers.CharField(required=False, allow_blank=True)
    coins = serializers.IntegerField(required=False, allow_null=True)

    image = serializers.ImageField(required=False)


class CustomerSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, write_only=True)

    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'phone',
            'address',
            'house_number',
            'coins',
            'premium',
            'avatar_url',
            'avatar_path',
            'image',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['avatar_url', 'avatar_path', 'created_at', 'updated_at']

    """Sobrescreve os métodos create e update para remover 
    o campo "image" antes de criar ou atualizar a instância"""

    def create(self, validated_data):
        validated_data.pop("image", None)
        return super().create(validated_data)
        
    def update(self, instance, validated_data):
        validated_data.pop("image", None)
        return super().update(instance, validated_data)