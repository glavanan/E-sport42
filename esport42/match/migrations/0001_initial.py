# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0002_auto_20150611_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score_t1', models.IntegerField(default=0)),
                ('score_t2', models.IntegerField(default=0)),
                ('end', models.BooleanField(default=False)),
                ('level', models.IntegerField(default=0)),
                ('match_number', models.IntegerField(default=0)),
                ('phase', models.ForeignKey(related_name='phase', to='tournoi.Phase')),
                ('team1', models.ForeignKey(related_name='team1', to='tournoi.Teams', null=True)),
                ('team2', models.ForeignKey(related_name='team2', to='tournoi.Teams', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
