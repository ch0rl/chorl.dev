import json

import django.core.cache
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.conf import settings
from .models import Terms


def index(request: HttpRequest):
    return render(request, "projects/index.html")


def kinks(request: HttpRequest):
    return render(request, "projects/kinks.html")


def terminology(request: HttpRequest):
    return render(request, "projects/terms.html")


def terms_api(request: HttpRequest):
    return HttpResponse(json.dumps(
        [{
            "t": i.old,
            "r": i.new,
            "e": i.description
        } for i in Terms.objects.all()]
    ), content_type="application/json")


