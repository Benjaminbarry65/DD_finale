# Generated by Django 5.0.4 on 2024-05-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_app', '0009_rename_baby_info_pickup_baby_name_delete_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='time_arrival',
            field=models.TimeField(),
        ),
    ]
