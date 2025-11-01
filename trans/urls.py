from django.urls import path
from trans.views import *

urlpatterns = [
    path('', index, name='trans'),
    path('/email/<str:template>', email, name='email'),
    path('/category/<str:template>', category, name='category')
]
