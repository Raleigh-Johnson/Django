# Generated by Django 3.2.6 on 2021-08-25 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('treats', 'treats'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
