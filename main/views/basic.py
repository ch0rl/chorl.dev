import json
from random import shuffle
from typing import List

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, resolve_url
from .user_agents import BLOCK_ALL
from django.templatetags.static import static


def index(request: HttpRequest):
    return render(request, "index.html")


def contact(request: HttpRequest):
    return render(request, "contact.html")


def about(request: HttpRequest):
    label_list: List[List[str]] = [
        ["Queer", "An umbrella term for being part of the LGBTQIA+ community."],
        ["Autistic",
         "A person with <a href=\"https://autism.org.uk/advice-and-guidance/what-is-autism\" target=\"_blank\">Autism Spectrum Disorder</a>."],
        ["Socialist",
         "A general term for views regarding the collective ownership of capital by the people or the state, and other associated social policy; the polar opposite of capitalism."],
        ["Anarchist", "Similar to how Chomsky defines anarchism: the anti-authoritarian wing of socialism."],
        ["Trans", "[Generally] someone who's gender assigned at birth does not align with their gender identity."],
        ["Non-binary", "Someone who's gender identity does not fit the typical binary of male/female."],
        ["Gender Fluid", "Someone who's gender identity is not constant."],
        ["Republican (UK)", "Someone who rejects the notion of a monarch/monarchy."],
        ["Environmentalist", "Someone who advocates for the protection of the environment."],
        ["Activist", "Someone who partakes in activism."]
    ]
    shuffle(label_list)

    return render(request, "about.html", context={"label_list": label_list})


def credits(request: HttpRequest):
    return render(request, "credits.html")


def robots(request: HttpRequest):
    return HttpResponse(
        (
            "User-agent: *\n"
            "Disallow: /\n"
            f"User-agent: {request.headers.get('User-Agent')}\n"
            "Disallow: /\n"
        ) + BLOCK_ALL,
        request
    )


def disclaimer(request: HttpRequest):
    return render(request, "email-disclaimer.html")


def teapot(_):
    return HttpResponse("I'm a teapot", status=418)


def privacy(request: HttpRequest):
    return render(request, "privacy.html")