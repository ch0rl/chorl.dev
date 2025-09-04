from django.db import models


class Article(models.Model):
    title = models.TextField(primary_key=True),
    desc = models.TextField()
    template = models.FilePathField()
