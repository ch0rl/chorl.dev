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


def browser(request: HttpRequest):
    in_req = {
        "ip": request.headers.get("X-Forwarded-For", "n/a"),
        "user_agent": request.headers.get("User-Agent", "n/a"),
        "cookies": json.dumps(request.COOKIES, indent=4),
        "referrer": request.headers.get("Referer", "n/a"),
        "via": request.headers.get("Via", "n/a"),
    }
    revealed = ...

    return render(request, "projects/browser.html", context={"in_req": in_req, "revealed": revealed})
