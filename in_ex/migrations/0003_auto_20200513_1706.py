# Generated by Django 3.0.6 on 2020-05-13 16:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('in_ex', '0002_auto_20200513_1704'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expanse',
            new_name='Expense',
        ),
    ]
