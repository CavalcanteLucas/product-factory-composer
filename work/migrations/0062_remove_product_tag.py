# Generated by Django 3.1 on 2021-03-16 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0061_auto_20210316_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
    ]