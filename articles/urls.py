from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="articles"),
    path("<int:_id>", article, name="article"),
    path("sub/rhse-annex", rhse_annex, name="rhse-annex")
]
