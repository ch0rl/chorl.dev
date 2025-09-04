from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render
from pathlib import Path
from .models import *


def index(request: HttpRequest):
    return render(request, "articles.html", context={"articles": Article.objects.all()})


def article(request: HttpRequest, _id: int):
    _article = Article.objects.get(id=_id)
    if _article is None:
        return HttpResponseNotFound()
    else:
        return render(request, _article.template, context={"article": _article})