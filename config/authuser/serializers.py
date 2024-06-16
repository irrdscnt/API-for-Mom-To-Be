from rest_framework import serializers
from .models import *
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
        fields = ['id','photo', 'description', 'trimester','week']
        read_only_fields = ['id']

class BabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_date(self, value):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                raise serializers.ValidationError("Date must be in format YYYY-MM-DD")
        return value

    def validate_time(self, value):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%H:%M:%S').time()
            except ValueError:
                raise serializers.ValidationError("Time must be in format HH:MM:SS")
        return value

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()