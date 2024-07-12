from django.db import models


class Terms(models.Model):
    old = models.TextField()
    new = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
