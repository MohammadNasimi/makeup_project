# Generated by Django 4.0.2 on 2022-02-04 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('Date', models.DateTimeField()),
                ('Time', models.DateTimeField()),
                ('Agent', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Agent', to='Agent.agent', verbose_name='Agent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
