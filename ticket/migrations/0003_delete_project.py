# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20151122_1155'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
    ]
