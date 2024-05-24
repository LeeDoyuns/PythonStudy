from django.urls import path
from .crolling.CrollingTest import *
from .automation.WebAutomation import *
from .mailing.MailSendTest import *


urlpatterns = [
    path('weatherTest', weatherTest),
    path('seleniumTest1', seleniumTest1),
    path('gmailTest', gmailSendTest),
]