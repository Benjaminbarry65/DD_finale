# Generated by Django 5.0.4 on 2024-05-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daystar_app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='nin',
            field=models.CharField(max_length=100),
        ),
    ]