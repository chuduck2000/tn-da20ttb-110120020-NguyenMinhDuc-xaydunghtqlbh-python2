# Generated by Django 5.0.4 on 2024-06-10 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_promotions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
