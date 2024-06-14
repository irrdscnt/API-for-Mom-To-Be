from django.shortcuts import render

from rest_framework import generics
from .models import AuthUser,NutritionAdvice
from .serializers import RegisterSerializer,NutritionAdviceSerializer

class RegisterView(generics.CreateAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = RegisterSerializer

class NutritionAdviceListCreateView(generics.ListCreateAPIView):
    queryset = NutritionAdvice.objects.all()
    serializer_class = NutritionAdviceSerializer


class NutritionAdviceListView(generics.ListAPIView):
    queryset = NutritionAdvice.objects.all()
    serializer_class = NutritionAdviceSerializer

class NutritionAdviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NutritionAdvice.objects.all()
    serializer_class = NutritionAdviceSerializer

class NutritionAdviceByTrimesterListView(generics.ListAPIView):
    serializer_class = NutritionAdviceSerializer

    def get_queryset(self):
        trimester = self.kwargs['trimester']
        return NutritionAdvice.objects.filter(trimester=trimester)