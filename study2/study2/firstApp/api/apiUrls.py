from django.urls import path
from .crolling.CrollingTest import *
from .automation.WebAutomation import *


urlpatterns = [
    path('weatherTest', weatherTest),
    path('seleniumTest1', seleniumTest1),
]