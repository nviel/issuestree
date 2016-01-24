# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Ticket(models.Model):
    # identifiant ajouté automatiquement par django:
    # id = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    workload    = models.FloatField(null=True, blank=True)
    order       = models.IntegerField(null=True, blank=True)
    parent      = models.ForeignKey('self', null=True, blank=True)
    creation_date     = models.DateTimeField(null=True, blank=True)
    modification_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
