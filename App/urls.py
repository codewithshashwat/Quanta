from django.urls import path
from . import views

urlpatterns = [
    path('', views.quanta_view, name='quanta_chat'),
]