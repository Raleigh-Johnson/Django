# Generated by Django 3.2.6 on 2021-08-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('drinks', 'drinks'), ('appetizers', 'appetizers'), ('treats', 'treats')], max_length=60),
        ),
    ]