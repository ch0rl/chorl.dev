import json

import django.core.cache
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.conf import settings
from .models import Terms


def index(request: HttpRequest):
    return render(request, "projects.html")


def kinks(request: HttpRequest):
    # categories = [
    #     {
    #         "title": "Test",
    #         "items": [
    #             "a",
    #             "b",
    #             "abcsdeifjjkalf"
    #         ]
    #     }
    # ]
    # return render(request, "projects/kinks.html", {"categories": categories})
    return HttpResponse("This doesn't exist yet... (sorry)", status=404, content_type="text/plain")


def terminology(request: HttpRequest):
    return render(request, "terms.html")

#
# def get_terms():
#     # Only read file once
#     # TODO: When updated to use DB, will have to read each time for live updates
#     with open(settings.BASE_DIR / "projects/terms.csv") as f:
#         __raw_terms = f.read().splitlines()[1:]
#
#     for line in __raw_terms:
#         parts = [i.strip() for i in line.split("|")]
#         if len(parts) == 3:
#             yield parts
#         else:
#             print(f"[!] failed parsing '{line}' into three '|'-seperated parts.")
#
#
# # Import terms into DB on load
# Terms.objects.bulk_create([
#     Terms(old=i[0], new=i[1], description=i[2]) for i in get_terms() if not Terms.objects.filter(old=i[0]).exists()
# ])


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

    return render(request, "browser.html", context={"in_req": in_req, "revealed": revealed})
