# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosestStore',
            fields=[
                ('store_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stores.Store')),
                ('origin_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('origin_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('distance', models.CharField(max_length=25)),
                ('time', models.CharField(max_length=25)),
            ],
            options={
                'managed': False,
            },
            bases=('stores.store',),
        ),
        migrations.RenameField(
            model_name='order',
            old_name='coffee',
            new_name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='metadata',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
