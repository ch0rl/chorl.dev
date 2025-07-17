from django.urls import path, include
from .views import index, kinks, terminology, browser, terms_api

urlpatterns = [
    path("", index, name="projects-index"),
    # path("kinks", kinks, name="kinks"),
    path("terms", terminology, name="terms"),
    path("browser", browser, name="browser"),
    path("api/terms", terms_api, name="api-terms"),
]
