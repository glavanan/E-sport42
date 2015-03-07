# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20150305_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
