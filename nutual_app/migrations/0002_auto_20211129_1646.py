# Generated by Django 3.1.2 on 2021-11-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutual_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pisos',
            name='price_m',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pisos',
            name='total_area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pisos',
            name='total_prince',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pisos',
            name='year_of_construction',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pisos',
            name='year_of_renovation',
            field=models.IntegerField(),
        ),
    ]
