from django.urls import path
from .crolling.CrollingTest import *


urlpatterns = [
    path('weatherTest', weatherTest),
    path('webtoonTitleTest', webtoonTitleTest)
]