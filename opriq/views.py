from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.conf import settings
from opriq.models import *


def index(request):
    return render(request, "home.html.django", context={
        "items": Item.objects.all(),
        "mods": Modifier.objects.all(),
        "inferences": Inference.objects.all()
    })


def about(request):
    return render(request, "about.html.django", context={
        "faqs": FAQ.objects.all()
    })


def get_items(request):
    return JsonResponse([{
        "id": i.id,
        "name": i.name,
        "base sensitivity": i.base_sensitivity
    } for i in Item.objects.all()], safe=False)


def get_item(request, _id):
    i = Item.objects.get(id=_id)

    if i is None:
        return HttpResponseNotFound()
    else:
        return JsonResponse({
            "name": i.name,
            "base sensitivity": i.base_sensitivity
        })


def get_mods(request):
    _id = request.GET.get("id")

    if _id is None:
        return JsonResponse([{
            "item id": i.item_id,
            "value": i.value,
            "modifier": i.multiplier
        } for i in Modifier.objects.all()], safe=False)
    else:
        return JsonResponse([{
            "value": i.value,
            "modifier": i.multiplier
        } for i in Modifier.objects.filter(item_id=_id)], safe=False)


def get_opriq(request):
    return HttpResponse(open(settings.BASE_DIR / "static/opriq.mathml").read(), content_type="text/xml")