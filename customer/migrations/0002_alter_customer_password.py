# Generated by Django 4.0.2 on 2022-02-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
