# Generated by Django 3.1 on 2021-08-19 12:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0043_skill_expertise_update_for_new_functionality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personskill',
            name='category',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300, null=True), blank=True, default=list, null=True, size=None),
        ),
    ]