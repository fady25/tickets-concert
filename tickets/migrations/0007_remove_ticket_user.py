# Generated by Django 5.0.1 on 2024-02-10 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_alter_ticket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
    ]
