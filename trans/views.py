from django.http import HttpRequest
from django.shortcuts import render


def acronym(short, long):
    return f'<abbr title="{long}">{short}</abbr>'


ACRONYMS = {
    "ehrc": acronym("EHRC", "Equality and Human Rights Commission"),
    "dhsc": acronym("DHSC", "Department of Health and Social Care"),
    "wpath": acronym("WPATH", "World Professional Association for Transgender Health"),
    "iesogi": acronym("IESOGI", "Independent Expert on protection against violence and discrimination based on Sexual Orientation and Gender Identity")
}


def index(request: HttpRequest):
    return render(request, "trans-index.html", context={
        "acronyms": ACRONYMS
    })


def email(request: HttpRequest, template: str):
    return render(request, f"emails/{template}.html", context={
        "acronyms": ACRONYMS
    })


def category(request: HttpRequest, template: str):
    return render(request, f"categories/{template}.html", context={
        "acronyms": ACRONYMS
    })