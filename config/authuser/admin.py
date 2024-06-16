from django.contrib import admin
from .models import *


admin.site.register(AuthUser)
admin.site.register(NutritionAdvice)
admin.site.register(Baby)
admin.site.register(Event)

