# Generated by Django 5.1.2 on 2024-11-04 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.login')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquiry', models.TextField()),
                ('response', models.TextField(blank=True, null=True)),
                ('login', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.login')),
            ],
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.login')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('seat_number', models.CharField(max_length=10)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.flight')),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.login')),
            ],
        ),
        migrations.CreateModel(
            name='Logout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logout_time', models.DateTimeField()),
                ('login', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.login')),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signup_date', models.DateTimeField(auto_now_add=True)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.login')),
            ],
        ),
    ]
