from rest_framework import serializers
from .models import AuthUser,NutritionAdvice
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['email', 'name', 'phone', 'pregnancy_week', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class NutritionAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionAdvice
        fields = ['id','photo', 'description', 'trimester']
        read_only_fields = ['id']
