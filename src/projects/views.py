from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.conf import settings


def index(request: HttpRequest):
    return render(request, "projects/index.html")


def kinks(request: HttpRequest):
    return render(request, "projects/kinks.html")


def get_terms():
    # Only read file once
    # TODO: When updated to use DB, will have to read each time for live updates
    with open(settings.BASE_DIR / "src/projects/terms.csv") as f:
        __raw_terms = f.read().splitlines()[1:]

    for line in __raw_terms:
        parts = [i.strip() for i in line.split("|")]
        if len(parts) == 3:
            yield parts
        else:
            print(f"[!] failed parsing '{line}' into three '|'-seperated parts.")


TERMS = list(get_terms())


def terminology(request: HttpRequest):
    return render(request, "projects/terms.html", context={"terms": TERMS})

