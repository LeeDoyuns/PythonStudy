from django.urls import path
from .crolling.CrollingTest import * 


urlpatterns = [
    path('crollingTest', colTest)
]