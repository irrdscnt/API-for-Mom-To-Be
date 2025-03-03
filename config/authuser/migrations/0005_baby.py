# Generated by Django 5.0.6 on 2024-06-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0004_nutritionadvice_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trimester', models.PositiveIntegerField()),
                ('week', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='baby/')),
            ],
        ),
    ]
