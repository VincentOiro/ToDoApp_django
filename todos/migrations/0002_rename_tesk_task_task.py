# Generated by Django 5.0.4 on 2024-04-05 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tesk',
            new_name='task',
        ),
    ]