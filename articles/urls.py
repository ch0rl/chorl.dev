from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="articles"),
    path("article/<str:template>", article, name="article")
]
