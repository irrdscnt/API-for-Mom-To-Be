from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


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
    
class BabyListCreateView(generics.ListCreateAPIView):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

class BabyDetailView(generics.RetrieveAPIView):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

class BabyByWeekView(generics.ListAPIView):
    serializer_class = BabySerializer

    def get_queryset(self):
        week = self.kwargs['week']
        return Baby.objects.filter(week=week)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "No data found for the specified week."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)