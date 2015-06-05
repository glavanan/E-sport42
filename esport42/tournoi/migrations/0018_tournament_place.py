# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0017_auto_20150605_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='place',
            field=models.CharField(default='Ecole 42. 96 boulevard Bessieres, 75017 Paris, France', max_length=256),
            preserve_default=False,
        ),
    ]
