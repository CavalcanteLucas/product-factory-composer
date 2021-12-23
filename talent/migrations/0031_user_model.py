# Generated by Django 3.1 on 2021-06-15 12:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0030_auto_20210402_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='username_ptr',
        ),
        migrations.RemoveField(
            model_name='person',
            name='uuid',
        ),
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]