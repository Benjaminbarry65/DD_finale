# Generated by Django 5.0.4 on 2024-05-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_app', '0007_alter_baby_amount_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='time_arrival',
            field=models.DateTimeField(),
        ),
    ]
