from django.urls import path

from . import views

app_name = 'economy_partner'
urlpatterns = [
    path('', views.index , name='index')
]