from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    desc = models.TextField()
    template = models.FilePathField()
    updated = models.DateTimeField(auto_now=True)
