# Generated by Django 3.2 on 2023-01-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('FL', 'flower'), ('BQ', 'bouquet'), ('IP', 'indoor_plants')], max_length=2, null=True),
        ),
    ]