from django.urls import path
from .views import base, login_view, logout_view, signup, verify_otp, resend_otp,profile_view

urlpatterns = [
    path('', base, name='base'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('resend-otp/', resend_otp, name='resend_otp'),
    path('profile/', profile_view, name='profile'),

]
