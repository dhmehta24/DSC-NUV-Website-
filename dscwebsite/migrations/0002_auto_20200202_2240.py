# Generated by Django 3.0.2 on 2020-02-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dscwebsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='ev_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hof',
            name='hof_yr',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='tm_ph',
            field=models.IntegerField(),
        ),
    ]