# Generated by Django 3.2.9 on 2021-11-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=1000)),
                ('twitter', models.CharField(max_length=100)),
                ('youtube', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('eth_address', models.CharField(max_length=50)),
                ('charity', models.BooleanField(default=False)),
            ],
        ),
    ]
