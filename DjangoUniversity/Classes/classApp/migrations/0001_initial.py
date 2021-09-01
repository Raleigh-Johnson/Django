# Generated by Django 3.2.6 on 2021-09-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=60)),
                ('course_number', models.IntegerField(blank=True)),
                ('instructor', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
