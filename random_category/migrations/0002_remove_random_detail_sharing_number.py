# Generated by Django 4.0 on 2021-12-22 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('random_category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='random_detail',
            name='sharing_number',
        ),
    ]