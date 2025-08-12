from django.urls import path
from .views import index, terminology, browser, terms_api, trans, trans_dhsc, trans_ehrc

urlpatterns = [
    path("", index, name="projects-index"),
    # path("kinks", kinks, name="kinks"),
    path("terms", terminology, name="terms"),
    path("browser", browser, name="browser"),
    path("api/terms", terms_api, name="api-terms"),
    path("trans", trans, name="trans"),
    path("trans/dhsc", trans_dhsc, name="trans-dhsc"),
    path("trans/ehrc", trans_ehrc, name="trans-ehrc")
]
