__author__ = 'DELL'

from django.urls import path
from .import views

app_name="Images"

urlpatterns = [

    path('test',views.test,name="test"),
    path('Jsondata',views.data,name="data"),
]
