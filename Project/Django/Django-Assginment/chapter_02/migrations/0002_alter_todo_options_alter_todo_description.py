# Generated by Django 5.1 on 2024-08-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter_02', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'To-Do', 'verbose_name_plural': 'To-Do list'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(null=True),
        ),
    ]