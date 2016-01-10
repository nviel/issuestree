# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('workload', models.FloatField()),
                ('order', models.IntegerField()),
                ('creation_date', models.DateTimeField()),
                ('modification_date', models.DateTimeField()),
                ('parent', models.ForeignKey(to='ticket.Ticket')),
                ('project', models.ForeignKey(to='ticket.Project')),
            ],
        ),
    ]
