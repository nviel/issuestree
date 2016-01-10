# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='project',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='creation_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='modification_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='parent',
            field=models.ForeignKey(blank=True, to='ticket.Ticket', null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='workload',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
