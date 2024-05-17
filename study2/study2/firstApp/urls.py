from django.urls import path,include
from . import views as view

urlpatterns = [
    path('test', view.index),
    path('api/', include('firstApp.api.apiUrls'))
]
