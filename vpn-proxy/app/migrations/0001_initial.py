# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 14:12
from __future__ import unicode_literals

import app.models
import app.tunnels
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forwarding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dst_addr', models.GenericIPAddressField(protocol='IPv4', validators=[app.models.check_ip])),
                ('dst_port', models.IntegerField()),
                ('loc_port', models.IntegerField(unique=True)),
                ('src_addr', models.GenericIPAddressField(protocol='IPv4')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tunnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('server', models.GenericIPAddressField(protocol='IPv4', unique=True, validators=[app.models.check_ip])),
                ('client', models.GenericIPAddressField(protocol='IPv4', validators=[app.models.check_ip])),
                ('key', models.TextField(default=app.tunnels.gen_key, unique=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='forwarding',
            name='tunnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tunnel'),
        ),
    ]
