# Generated by Django 5.0.6 on 2024-06-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='password',
            field=models.CharField(default=0, max_length=128),
        ),
    ]
