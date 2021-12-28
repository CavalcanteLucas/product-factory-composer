# Generated by Django 3.1 on 2021-01-09 20:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_task_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='capability',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='initiative',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]