# Generated by Django 4.2.4 on 2023-10-06 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0011_alter_task_managers_remove_task_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['priority', 'created_at', '-status'], 'verbose_name': 'Task'},
        ),
    ]
