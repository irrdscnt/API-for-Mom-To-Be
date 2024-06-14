# Generated by Django 5.0.6 on 2024-06-14 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField(blank=True, max_length=2000, null=True)),
                ('phone', models.TextField(blank=True, max_length=2000, null=True)),
                ('pregnancy_week', models.IntegerField()),
            ],
        ),
    ]
