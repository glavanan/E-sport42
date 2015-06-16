# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0002_auto_20150611_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phase',
            old_name='tmp_name',
            new_name='name',
        ),
    ]
