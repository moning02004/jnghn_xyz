# Generated by Django 2.1.7 on 2019-03-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coffee', '0002_auto_20190311_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentcommunity',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
