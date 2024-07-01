from django.urls import path, include
from .views import index, kinks, terminology

urlpatterns = [
    path("", index, name="projects-index"),
    path("kinks", kinks, name="kinks"),
    path("terms", terminology, name="terms"),
]
