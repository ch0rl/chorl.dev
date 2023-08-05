from django.urls import path, include
from .views import index, kinks

urlpatterns = [
    path("", index, name="projects-index"),
    path("kinks", kinks, name="kinks")
]
