# Generated by Django 4.2.4 on 2023-10-05 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0007_alter_task_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['priority', 'created_at', '-status'], 'verbose_name': 'Task'},
        ),
    ]
