# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0004_match_looser_braket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='level',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
