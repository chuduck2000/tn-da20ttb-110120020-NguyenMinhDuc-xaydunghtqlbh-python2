# Generated by Django 5.0.4 on 2024-07-05 09:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_product_options_alter_reviewrating_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Điểm đánh giá'),
        ),
    ]