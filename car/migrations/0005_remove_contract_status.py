# Generated by Django 4.2.7 on 2023-11-25 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_remove_contract_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='status',
        ),
    ]
