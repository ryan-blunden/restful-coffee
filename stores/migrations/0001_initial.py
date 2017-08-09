# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_last_updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('coffee', models.CharField(max_length=100)),
                ('expires', models.DateTimeField(blank=True, default=None)),
                ('is_complete', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_last_updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Store'),
        ),
    ]
