from django.urls import path
from . import views

urlpatterns = [
    path('adoption/', views.adoption_list, name='adoption_section'),  # name must match
    path("adopt/<int:pet_id>/", views.adopt_pet, name="adopt_pet"),
    path("sponsor/<int:pet_id>/", views.sponsor_pet, name="sponsor_pet"),
]
