# Generated by Django 3.1 on 2021-03-04 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_auto_20210304_1304'),
        ('work', '0047_auto_20210302_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comments_start',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comment'),
        ),
    ]