# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_event', models.PositiveIntegerField()),
                ('id_payer', models.PositiveIntegerField()),
                ('type_event', models.CharField(max_length=25, choices=[(b'Tournament', b'Tournament')])),
                ('type_payer', models.CharField(max_length=25, choices=[(b'MyUser', b'User'), (b'Teams', b'Teams')])),
                ('verified', models.BooleanField(default=False)),
                ('txn_id', models.CharField(max_length=50, blank=True)),
                ('payment_to', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
