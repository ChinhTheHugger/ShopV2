# Generated by Django 4.2.7 on 2023-11-25 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_contract_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='phone',
        ),
    ]