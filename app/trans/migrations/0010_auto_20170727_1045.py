# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-27 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0009_auto_20170707_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frozen', models.BooleanField(default=False)),
                ('note', models.TextField(default='')),
                ('extra_country1', models.CharField(max_length=6, blank=True)),
                ('extra_country2',models.CharField(max_length=6, blank=True)),
                ('contest', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='trans.Contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.User')),
            ],
        ),
        migrations.AlterField(
            model_name='attachment',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='uploaded_file',
            field=models.FileField(upload_to='images/'),
        ),
    ]