# Generated by Django 3.1.7 on 2021-06-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210601_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='icon',
            field=models.CharField(default='04d', max_length=200),
        ),
    ]
