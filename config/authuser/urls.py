from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('nutrition-advice/', NutritionAdviceListCreateView.as_view(), name='nutrition-advice-list-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('nutrition-advice/list', NutritionAdviceListView.as_view(), name='nutrition-advice-list'),
    path('nutrition-advice/<int:pk>/', NutritionAdviceDetailView.as_view(), name='nutrition-advice-detail'),
    path('nutrition-advice/trimester/<int:trimester>/', NutritionAdviceByTrimesterListView.as_view(), name='nutrition-advice-by-trimester'),
    path('babies/', BabyListCreateView.as_view(), name='baby-list-create'),
    path('babies/<int:pk>/', BabyDetailView.as_view(), name='baby-detail'),
    path('babies/week/<int:week>/', BabyByWeekView.as_view(), name='baby-by-week'),
    path('events/', save_event, name='save_event'),
    path('events/date/<str:date>/', get_events_by_date, name='get_events_by_date'),

]