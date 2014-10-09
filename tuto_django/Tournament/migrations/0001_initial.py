# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nb_team', models.IntegerField()),
                ('nb_joueur', models.IntegerField()),
                ('nom', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=10)),
                ('etat', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('jeu', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=30)),
                ('template', models.CharField(max_length=30)),
                ('prix', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
