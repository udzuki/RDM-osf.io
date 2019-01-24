# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import osf.models.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('osf', '0046_add_weko_addon'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(db_index=True, default=osf.models.base.generate_object_id, max_length=24, unique=True)),
                ('deleted', models.BooleanField(default=False)),
                ('service_list', models.TextField(blank=True, null=True)),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addons_jupyterhub_node_settings', to='osf.AbstractNode')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
