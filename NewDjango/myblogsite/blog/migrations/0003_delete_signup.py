# Generated by Django 5.1.2 on 2024-10-27 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]