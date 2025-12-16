from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="backend-home"),
    path('chat/', views.chat, name="backend-chat"),
]
