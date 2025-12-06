from django.urls import path
from . import views

urlpatterns = [
    path('volunteer/', views.volunteer_apply, name='volunteer_apply'),
]
