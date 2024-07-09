import json
from random import shuffle
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, resolve_url
from .user_agents import BLOCK_ALL


def index(request: HttpRequest):
    return render(request, "index.html")


def contact(request: HttpRequest):
    return render(request, "contact.html")


def about(request: HttpRequest):
    label_list = [
        ["Queer", "An umbrella term for being part of the LGBTQIA+ community."],
        ["Autistic", "A person with <a href=\"https://autism.org.uk/advice-and-guidance/what-is-autism\" target=\"_blank\">Autism Spectrum Disorder</a>."],
        ["Socialist", "A general term for views regarding the collective ownership of capital by the people or the state, and other associated social policy; the polar opposite of capitalism."],
        ["Anarchist", "Similar to how Chomsy defines anarchism: the anti-authoritarian wing of socialism."],
        ["Trans", "[Generally] someone who's gender assigned at birth does not align with their gender identity."],
        ["Non-binary", "Someone who's gender identity does not fit the typical binary of male/female."],
        ["Gender Fluid", "Someone who's gender identity is not constant."],
        ["Republican (UK)", "Someone who does not agree with the notion of a monarch/monarchy."],
        ["Environmentalist", "Someone who advocates for the protection of the environment."],
        ["Activist", "Someone who partakes in activism."]
    ]
    shuffle(label_list)

    interests = [
        ["Cyber Security", """
            I'm interested in all parts of cyber security, but my some of my key interests are in:
            <ul>
                <li>human behaviours,</li>
                <li>penetration testing,</li>
                <li><abbr>OSINT</abbr> (OpenSource INTelligence) / <abbr>OPSEC</abbr> (OPerational SECurity),</li>
                <li>physical security,</li>
                <li>ethics and morals, and</li>
                <li>hacktivism.</li>
            </ul>
        """],
        ["Human Rights", """
            Specifically, I'm interested in:
            <ul>
                <li>the international context and application of human rights and IHL (International Humanitatian Law),</li>
                <li>the right to protest,</li>
                <li>police and state responsibilities, and</li>
                <li><abbr>LGBTQIA+</abbr> rights, especially for gender-queer people.</li>
            </ul>
        """],
        ["Research", f"""
            I tend to enjoy random research projects, and just learning in general; see also <a href="{resolve_url('projects-index')}">projects</a>.
        """],
        ["Safety &ndash; First-Aid, etc.", """
            I find the following topics interesting, in the context of safety, first-aid, etc.
            <ul>
                <li>rope systems,</li>
                <li>first aid,</li>
                <li>preparation,</li>
                <li>regulatory compliance, and</li>
                <li>safety &ldquo;on the water&rdquo;, &ldquo;at height&rdquo;, etc.</li>
            </ul>
        """]
    ]
    shuffle(interests)

    return render(request, "about.html", context={"label_list": label_list, "interests": interests})


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
