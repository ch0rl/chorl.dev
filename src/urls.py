"""
URL configuration for site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import basic

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", basic.index, name="index"),
    path("contact", basic.contact, name="contact"),
    path("about", basic.about, name="about"),
    path("about-site", basic.site, name="about-site"),
    path("credits", basic.credits, name="credits"),
    path("projects/", include("src.projects.urls")),
    path("robots.txt", basic.robots, name="robots"),
]
