# Generated by Django 3.1 on 2021-03-04 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0010_comment2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment2',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
    ]