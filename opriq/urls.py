from django.urls import path
from opriq.views import *

urlpatterns = [
    path('', index, name='opriq-index'),
    path('about', about, name='opriq-about'),
    path('api/i', get_items, name='opriq-get_items'),
    path('api/i/<int:_id>', get_item, name='opriq-get_item'),
    path('api/m', get_mods, name='opriq-get_mods'),
    path('api/opriq', get_opriq, name='opriq-get_opriq'),
]
