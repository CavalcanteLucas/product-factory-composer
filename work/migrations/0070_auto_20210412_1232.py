# Generated by Django 3.1 on 2021-04-12 12:32

from django.db import migrations


def update_task_product(apps, schema_editor):
    Task = apps.get_model("work", "Task")
    ProductTask = apps.get_model("work", "ProductTask")

    for t in Task.objects.all():
        product_task = ProductTask.objects.filter(task=t).first()
        if product_task:
            t.product_id = product_task.product_id
            t.save()


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0069_task_product'),
    ]

    operations = [
        migrations.RunPython(update_task_product)
    ]