# Generated by Django 3.1 on 2021-03-04 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20210124_1557'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
    ]