# Generated by Django 4.0.2 on 2022-02-05 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_service_cost_alter_service_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='cost',
            field=models.PositiveIntegerField(blank=True, verbose_name='Price_Service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='time',
            field=models.PositiveIntegerField(blank=True, default=1, verbose_name='Time_Service'),
        ),
    ]
