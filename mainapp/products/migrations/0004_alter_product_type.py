# Generated by Django 3.2.6 on 2021-08-25 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('drinks', 'drinks'), ('treats', 'treats')], max_length=60),
        ),
    ]
