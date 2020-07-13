from django.urls import path
from . import views

app_name = 'greeting'

urlpatterns = [
  path('', views.index, name='index')
]