# Generated by Django 2.1.7 on 2019-02-20 13:00

import app_admin.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=app_admin.models.file_path)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='me',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.Me'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='archive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.Me'),
        ),
    ]
