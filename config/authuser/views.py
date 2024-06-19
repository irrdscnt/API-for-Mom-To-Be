from django.shortcuts import render
from django.utils.dateparse import parse_date  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate,get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

class NutritionAdviceUpdateAPIView(generics.UpdateAPIView):
    queryset = NutritionAdvice.objects.all()
    serializer_class = NutritionAdviceSerializer
    permission_classes = [AllowAny]

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
    
@api_view(['POST'])
def save_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_events_by_date(request, date):
    try:
        parsed_date = parse_date(date)
        if parsed_date is None:
            raise ValueError('Invalid date format. Use YYYY-MM-DD.')
        events = Event.objects.filter(date=parsed_date)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            # Если пользователь аутентифицирован, генерируем JWT access и refresh токены
            refresh = RefreshToken.for_user(user)

            return Response({
                'email': user.email,
                'name': user.name,
                'phone': user.phone,
                'pregnancy_week': user.pregnancy_week,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        else:
            return Response({'error': 'Неправильные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)
        
class TokenRefresh(APIView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh')

        serializer = TokenRefreshView.serializer_class(data={'refresh': refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            return Response({'error': 'Неправильный refresh токен'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            'access': str(serializer.validated_data['access']),
        })
    
class NutritionAdviceDeleteAPIView(generics.DestroyAPIView):
    queryset = NutritionAdvice.objects.all()
    serializer_class = NutritionAdviceSerializer
    permission_classes = [AllowAny]

@api_view(['POST'])
def create_fitness(request):
    if request.method == 'POST':
        serializer = FitnessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_fitness(request, pk):
    try:
        fitness = Fitness.objects.get(pk=pk)
    except Fitness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        fitness.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FitnessByTrimesterListView(generics.ListAPIView):
    serializer_class = FitnessSerializer

    def get_queryset(self):
        trimester = self.kwargs['trimester']
        return Fitness.objects.filter(trimester=trimester)