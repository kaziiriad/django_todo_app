# Generated by Django 4.2.4 on 2023-10-06 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0013_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status', 'priority', 'created_at'], 'verbose_name': 'Task'},
        ),
    ]