from django.http import HttpRequest, HttpResponseForbidden
from django.shortcuts import render
from .models import *


def index(request: HttpRequest):
    return render(request, "articles.html", context={"articles": Article.objects.all()})


def article(request: HttpRequest, template: str):
    if "/" in template or not template.endswith(".html"):
        return HttpResponseForbidden()
    else:
        return render(request, template)