from django.contrib import admin
from django.urls import path,include
from .views import RegisterView,NutritionAdviceListCreateView,NutritionAdviceListView,NutritionAdviceDetailView,NutritionAdviceByTrimesterListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('nutrition-advice/', NutritionAdviceListCreateView.as_view(), name='nutrition-advice-list-create'),
    path('nutrition-advice/list', NutritionAdviceListView.as_view(), name='nutrition-advice-list'),
    path('nutrition-advice/<int:pk>/', NutritionAdviceDetailView.as_view(), name='nutrition-advice-detail'),
    path('nutrition-advice/trimester/<int:trimester>/', NutritionAdviceByTrimesterListView.as_view(), name='nutrition-advice-by-trimester'),

]