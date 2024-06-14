from django.db import models

class AuthUser(models.Model):
    email=models.EmailField(max_length=150,unique=True)
    join_date=models.DateTimeField(auto_now_add=True)
    name=models.TextField(max_length=2000,blank=True,null=True)
    phone=models.TextField(max_length=2000,blank=True,null=True)
    pregnancy_week=models.IntegerField()
    password = models.CharField(max_length=128,default=0)  
    @property
    def is_authenticated(self):
        return True

    def __str__(self) -> str:
        return self.email


class NutritionAdvice(models.Model):
    photo = models.ImageField(upload_to='nutrition_photos/')
    description = models.TextField(max_length=2000)
    trimester = models.PositiveIntegerField()

    def __str__(self):
        return f"Trimester {self.trimester} - {self.description[:50]}"
