from django.contrib import admin
from .models import AuthUser,NutritionAdvice,Baby


admin.site.register(AuthUser)
admin.site.register(NutritionAdvice)
admin.site.register(Baby)

