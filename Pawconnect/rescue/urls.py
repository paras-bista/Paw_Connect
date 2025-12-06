from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_rescue_request, name='submit_rescue_request'),
]
